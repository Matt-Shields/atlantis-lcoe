"""Plotting script."""

__author__ = "Matt Shields"
__copyright__ = "Copyright 2022, National Renewable Energy Laboratory"
__maintainer__ = "Matt Shields"
__email__ = "matt.shields@nrel.gov"


import os

import pandas as pd
import matplotlib.pyplot as plt
from copy import deepcopy

SCENARIO_MAP = {
    # '2019 Aqua Ventus': 'Aqua Ventus (2019 report)',
    'Aqua Ventus': 'Aqua Ventus',
    'IEA 15MW': 'IEA 15 MW',
    'NASA Floater': 'NASA Floater'
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

# Installation times
INSTALL = pd.read_csv("outputs/installation_times.csv").rename(columns={
    "Unnamed: 0": "year",
})
INSTALL = INSTALL.set_index("year")
INSTALL.columns = INSTALL.columns.map(lambda x: SCENARIO_MAP[x])

def total_capex_plots(df):
    """"""

    # Raw CapEx
    fig = plt.figure(figsize=(6, 4), dpi=200)
    ax = fig.add_subplot(111)

    df.plot(kind='bar', ax=ax, rot=45)

    ax.set_xlabel("")
    ax.set_ylabel("CapEx ($)")

    fig.savefig(os.path.join(FIGDIR, "total_capex.png"), bbox_inches='tight')

    # CapEx per kW
    fig = plt.figure(figsize=(6, 4), dpi=200)
    ax = fig.add_subplot(111)

    df.divide(PROJECT_kW).plot(kind='bar', ax=ax, rot=45)
    print(df.divide(PROJECT_kW))

    ax.set_xlabel("")
    ax.set_ylabel("CapEx ($/kW)")

    fig.savefig(os.path.join(FIGDIR, "total_per_kW.png"), bbox_inches='tight')

    # LCOE - Match Aqua Ventus report (https://www.nrel.gov/docs/fy20osti/75618.pdf)
    opex = 40.1  # Inflated to $2021
    fcr = .0718
    ncf = 0.5086

    fig = plt.figure(figsize=(6, 4), dpi=200)
    ax = fig.add_subplot(111)

    df_lcoe = 1000*(fcr * df['Total'].divide(PROJECT_kW) + opex) / (ncf * 8760)
    print(df_lcoe)
    df_lcoe.plot(kind='bar', ax=ax, rot=45)
    ax.set_xlabel("")
    ax.set_ylabel("LCOE ($/MWh)")

    fig.savefig(os.path.join(FIGDIR, "LCOE.png"), bbox_inches='tight')

    # Opex and CapEx
    # mwh = ncf * 8760
    # opex_per_mwh = opex / mwh
    #
    # df_capex_opex = deepcopy(df)
    # df_capex_opex['BOS_per_MWh'] = (df_capex_opex['BOS'] / (PROJECT_kW / 1000) )/ (mwh )
    #
    # # capex_opex = {
    # #     'BOS': (df['BOS'] * 1000 / PROJECT_kW) / mwh
    # # }
    # #
    # print(df_capex_opex, mwh)
def capex_breakdown_plots(df):
    """"""

    # Raw CapEx
    fig = plt.figure(figsize=(6, 4), dpi=200)
    ax = fig.add_subplot(111)

    df.T.plot(kind='bar', stacked=True, ax=ax, rot=45).legend(bbox_to_anchor=(1.05, 1))

    ax.set_xlabel("")
    ax.set_ylabel("CapEx ($)")

    fig.savefig(os.path.join(FIGDIR, "capex_breakdown.png"), bbox_inches='tight')

    # Raw CapEx
    fig = plt.figure(figsize=(6, 4), dpi=200)
    ax = fig.add_subplot(111)

    df.divide(PROJECT_kW).T.plot(kind='bar', stacked=True, ax=ax, legend=False, rot=45)

    ax.set_xlabel("")
    ax.set_ylabel("CapEx ($/kW)")

    fig.savefig(os.path.join(FIGDIR, "breakdown_per_kW.png"), bbox_inches='tight')

    # Raw CapEx and Opex (all per MWH)
    mwh = 0.5086 * 8760
    opex = 40.1  # Inflated to $2021

    df_per_kw = (df * .058).divide(PROJECT_kW)
    df_per_kw.loc['Opex'] = [opex]*3
    df_per_mwh = (df_per_kw*1000) / mwh
    print( df_per_mwh.loc[['Substructure'], ['NASA Floater']] / df_per_mwh.sum()['NASA Floater'])
    print( df_per_mwh.loc[['Opex'], ['NASA Floater']] / df_per_mwh.sum()['NASA Floater'])

    fig = plt.figure(figsize=(6, 4), dpi=200)
    ax = fig.add_subplot(111)

    df_per_mwh.T.plot(kind='bar', stacked=True, ax=ax, rot=45).legend(bbox_to_anchor=(1.05, 1))

    ax.set_xlabel("")
    ax.set_ylabel("Project costs ($/MWh)")

    fig.savefig(os.path.join(FIGDIR, "breakdown_per_mwh.png"), bbox_inches='tight')


def installation_time_plots(df):
    """"""
    fig = plt.figure(figsize=(6, 4), dpi=200)
    ax = fig.add_subplot(111)

    df.divide(24*30).boxplot()

    ax.set_xlabel("")
    ax.set_ylabel("Installation time, months")

    fig.savefig(os.path.join(FIGDIR, "installation_times.png"), bbox_inches='tight')

def tmd_sensitivity():
    fig = plt.figure(figsize=(6, 4), dpi=200)
    ax = fig.add_subplot(111)

    tmd_cost = [1,2,4,6,8,10]
    lcoe = [60.4, 60.6, 61.1, 61.6, 62.1, 62.5]
    lcoe_diff = [100* (l - lcoe[0]) / lcoe[0] for l in lcoe]

    ax.plot(tmd_cost, lcoe_diff)

    ax.set_xlabel("Scaling factor for TMD cost")
    ax.set_ylabel("Percent change in LCOE")

    fig.savefig(os.path.join(FIGDIR, "tmd_sensitivity.png"), bbox_inches='tight')


if __name__ == "__main__":

    total_capex_plots(TOTALS)
    capex_breakdown_plots(BREAKDOWNS)
    installation_time_plots(INSTALL)
    tmd_sensitivity()
