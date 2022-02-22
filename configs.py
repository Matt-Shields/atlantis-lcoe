"""Collection of configuration files."""

__author__ = "Matt Shields"
__copyright__ = "Copyright 2022, National Renewable Energy Laboratory"
__maintainer__ = "Matt Shields"
__email__ = "matt.shields@nrel.gov"

# Import baseline configuration details for all scenarios
from common import base


# Site Data
# Shared config information
US_east_coast = {
    # All placeholder values for now
    "site": {
        "depth": 150,
        "distance": 100,
        "distance_to_landfall": 100
    },
    "port": {
        "monthly_rate": 1e6,
    },
    "project_parameters": {
        "turbine_capex": 1020
    },
    "turbine": "15MW",
    "weather": "US_east_coast"
}

# Define specific scenario inputs
AquaVentus_comp = {
    **base,
    **US_east_coast,
    # "turbine": "6MW",
    "design_phases": [
        'ArraySystemDesign',
        'ExportSystemDesign',
        "MooringSystemDesign",
        'OffshoreSubstationDesign',
        "SemiSubmersibleDesign",
    ],

}

IEA15MW_steel = {
    **base,
    **US_east_coast,
    "design_phases": [
        'ArraySystemDesign',
        'ExportSystemDesign',
        "MooringSystemDesign",
        'OffshoreSubstationDesign',
        "CustomSemiSubmersibleDesign",
    ],
    "semisubmersible_design": {
        "column_diameter": 12.5,
        "wall_thickness": 0.065,
        "column_height": 35,
        "pontoon_length": 51.75,
        "pontoon_width": 12.5,
        "pontoon_height": 7,
        "strut_diameter": 0.9,
        # "steel_density": "kg/m^3 (optional, default: 8050)",
        # "ballast_mass": "tonnes (optional, default 2540)",
        # "steel_cost_rate": "$/tonne (optional, default: 3120)",
        # "ballast_cost_rate": "$/tonne (optional, default: 150)"
    },
}

IEA15MW_concrete = {
    **base,
    **US_east_coast,
    "design_phases": [
        'ArraySystemDesign',
        'ExportSystemDesign',
        "MooringSystemDesign",
        'OffshoreSubstationDesign',
        "CustomSemiSubmersibleDesign",
    ],
    "semisubmersible_design": {
        "column_diameter": 12.5,
        "wall_thickness": 0.065,
        "column_height": 35,
        "pontoon_length": 51.75,
        "pontoon_width": 12.5,
        "pontoon_height": 7,
        "strut_diameter": 0.9,
        # "steel_density": "kg/m^3 (optional, default: 8050)",
        # "ballast_mass": "tonnes (optional, default 2540)",
        "steel_cost_rate": 1000,
        # "ballast_cost_rate": "$/tonne (optional, default: 150)"
    },

}


configs = {
    "Aqua Ventus": AquaVentus_comp,
    "IEA15MW (Steel)": IEA15MW_steel,
    "IEA15MW (Concrete)": IEA15MW_concrete
    # "US_10MW_shallow": us_15MW_shallow,
    # "US_15MW_deep": us_10MW_deep,
    # "US_15MW_shallow": us_15MW_shallow,
    # "US_10MW_deep": us_10MW_deep,
}
