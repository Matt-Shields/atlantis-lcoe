"""Plotting script."""

__author__ = "Matt Shields"
__copyright__ = "Copyright 2022, National Renewable Energy Laboratory"
__maintainer__ = "Matt Shields"
__email__ = "matt.shields@nrel.gov"


import os

import pandas as pd
import matplotlib.pyplot as plt


SCENARIO_MAP = {
    "US_10MW_shallow": "Shallow water, 10 MW turbine",
    "US_15MW_deep": "Deep water, 15 MW turbine"
}

FIGDIR = os.path.join(os.getcwd(), "figures")
PROJECT_kW = 600 * 1000  # TODO: Update hard-coded project capacity


TOTALS = pd.read_csv("outputs/scenario_capex.csv").rename(columns={
    "Unnamed: 0": "scenario",
    "0": "Total CapEx"
})

TOTALS['scenario'] = TOTALS['scenario'].apply(lambda x: SCENARIO_MAP[x])
TOTALS = TOTALS.set_index("scenario")

print(TOTALS)


BREAKDOWNS = pd.read_csv("outputs/breakdown.csv").rename(columns={
    "Unnamed: 0": "Category",
})
BREAKDOWNS = BREAKDOWNS.set_index("Category")
BREAKDOWNS.columns = BREAKDOWNS.columns.map(lambda x: SCENARIO_MAP[x])



def total_capex_plots(df):
    """"""

    # Raw CapEx
    fig = plt.figure(figsize=(6, 4), dpi=200)
    ax = fig.add_subplot(111)

    df.plot(kind='bar', ax=ax)

    ax.set_xlabel("")
    ax.set_ylabel("CapEx ($)")

    fig.savefig(os.path.join(FIGDIR, "total_capex.png"))

    # CapEx per kW
    fig = plt.figure(figsize=(6, 4), dpi=200)
    ax = fig.add_subplot(111)

    df.divide(PROJECT_kW).plot(kind='bar', ax=ax)

    ax.set_xlabel("")
    ax.set_ylabel("CapEx ($/kW)")

    fig.savefig(os.path.join(FIGDIR, "total_per_kW.png"))

    # LCOE
    opex = 130
    fcr = .058
    ncf = 0.38

    fig = plt.figure(figsize=(6, 4), dpi=200)
    ax = fig.add_subplot(111)

    df_lcoe = 1000*(fcr * df['Total'].divide(PROJECT_kW) + opex) / (ncf * 8760)
    print(df_lcoe)
    df_lcoe.plot(kind='bar', ax=ax, rot=45)
    ax.set_xlabel("")
    ax.set_ylabel("LCOE ($/MWh)")
    plt.tight_layout()



    fig.savefig(os.path.join(FIGDIR, "LCOE.png"))

def capex_breakdown_plots(df):
    """"""

    # Raw CapEx
    fig = plt.figure(figsize=(6, 4), dpi=200)
    ax = fig.add_subplot(111)

    df.T.plot(kind='bar', stacked=True, ax=ax)

    ax.set_xlabel("")
    ax.set_ylabel("CapEx ($)")

    fig.savefig(os.path.join(FIGDIR, "capex_breakdown.png"))

    # Raw CapEx
    fig = plt.figure(figsize=(6, 4), dpi=200)
    ax = fig.add_subplot(111)

    df.divide(PROJECT_kW).T.plot(kind='bar', stacked=True, ax=ax)

    ax.set_xlabel("")
    ax.set_ylabel("CapEx ($/kW)")

    fig.savefig(os.path.join(FIGDIR, "breakdown_per_kW.png"))


def installation_time_plots(df):
    """"""

    pass


if __name__ == "__main__":

    total_capex_plots(TOTALS)
    capex_breakdown_plots(BREAKDOWNS)