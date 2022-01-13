"""Primary analysis script."""

__author__ = "Matt Shields"
__copyright__ = "Copyright 2022, National Renewable Energy Laboratory"
__maintainer__ = "Matt Shields"
__email__ = "matt.shields@nrel.gov"

import numpy as np
import pandas as pd
import datetime as dt
from copy import deepcopy

from ORBIT import ProjectManager
from configs import configs
from ORBIT.core.library import initialize_library
from semisub_pontoon_design import CustomSemiSubmersibleDesign


initialize_library("data")


TRANSPORT_COSTS = 1e6 / 5000  # $/t
PROJECT_kW = 300 * 1000
WEATHER_FILES = {
    "US_east_coast": "data/weather/vineyard_wind_weather_1983_2017_orbit.csv",
    # Additional site weather profiles go here
}
WEATHER = {k: pd.read_csv(v, parse_dates=["datetime"]).set_index("datetime")
           for k, v in WEATHER_FILES.items()}
START_MONTH = 4


def run():

    bos_capex = {}
    total_capex = {}
    breakdowns = {}
    installation_times = {}

    ProjectManager._design_phases.append(CustomSemiSubmersibleDesign)

    for name, config in configs.items():

        print(f"Running config '{name}'")
        _times = {}
        weather = config.pop("weather", None)
        if weather:
            print(f"\tUsing weather from '{WEATHER_FILES[weather]}'")
            weather = WEATHER[weather]

        yrs = 0
        for yr in np.unique(weather.index.year):
            start = dt.date(yr, START_MONTH, 1)
            sub = weather.loc[start:]
            
            try:
                project = ProjectManager(config, weather=sub)
                project.run()
                yrs += 1

            except:
                continue
                
            _times[yr] = project.project_time
            test_capex_breakdown(name, project)
            total, bos, breakdown = append_transport_capex(name, project)

        print(f"\tRan {yrs} simulations")

        # Collect Results
        bos_capex[name] = bos
        total_capex[name] = total
        breakdowns[name] = breakdown
        installation_times[name] = _times

    # Aggregate Results
    bos_capex = pd.Series(bos_capex)
    total_capex = pd.Series(total_capex)
    breakdowns = pd.DataFrame(breakdowns)
    times = pd.DataFrame(installation_times)

    # Save Results
    totals = pd.concat([
        bos_capex.rename("BOS"),
        total_capex.rename("Total")
    ], axis=1)
    totals.index = totals.index.rename("")

    totals.to_csv("outputs/scenario_capex.csv")
    totals.divide(PROJECT_kW).to_csv("outputs/scenario_capex_perkW.csv")
    breakdowns.to_csv("outputs/breakdown.csv")
    breakdowns.divide(PROJECT_kW).to_csv("outputs/breakdown_perkW.csv")
    times.to_csv("outputs/installation_times.csv")


def append_transport_capex(name, project):
    """
    Ability to add transportation Capex for importing international components
    :param name:
    :param project:
    :return:
    """

    if "international" in name:
        mass = project.phases["SemiSubmersibleDesign"].total_substructure_mass
        cost = TRANSPORT_COSTS * mass
        breakdown = deepcopy(project.capex_breakdown)
        breakdown["Substructure Transportation"] = cost
        total = project.total_capex + cost
        bos = project.bos_capex + cost

    else:
        breakdown = deepcopy(project.capex_breakdown)
        total = project.total_capex
        bos = project.bos_capex

    return total, bos, breakdown

def test_capex_breakdown(name, project):

    expected_capex_categories = [
        "Array System",
        "Export System",
        "Substructure",
        "Mooring System",
        "Offshore Substation",
        "Array System Installation",
        "Export System Installation",
        "Substructure Installation",
        "Mooring System Installation",
        "Offshore Substation Installation",
        "Turbine",
        "Soft",
        "Project"
    ]

    missing = [c for c in expected_capex_categories if c not in project.capex_breakdown.keys()]
    if missing:
        print(f"Missing results for {missing} in {name}.")


if __name__ == "__main__":

    run()
