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
        "depth": 100,
        "distance": 52,
        "distance_to_landfall": 52
    },
    "port": {
        "monthly_rate": 1e6,
    },
    'project_parameters': {
        'turbine_capex': 1020,
        # 'ncf': 0.5,
        # 'offtake_price': 80,
        # 'project_lifetime': 25,
        # 'discount_rate': 0.025,
        # 'opex_rate': 150,
        'construction_insurance': 30,
        'construction_financing': 124,
        'contingency': 196,
        'commissioning': 30,
        'decommissioning': 28,
        'site_auction_price': 52925529,
        'site_assessment_cost': 50486746,
        'construction_plan_cost': 28604389,
        'installation_plan_cost': 0
    },
    "turbine": "15MW",
    "weather": "US_east_coast"
}

# Define specific scenario inputs
AquaVentus_match = {
    **base,
    **US_east_coast,
    # "turbine": "6MW",
    "design_phases": [
        "MooringSystemDesign",
        "SemiSubmersibleDesign",
    ],
    "install_phases": {
        "MooredSubInstallation": ("MooringSystemInstallation", 0.5),
        "MooringSystemInstallation": 0,
    },
}

AquaVentus_orbit = {
    **base,
    **US_east_coast,
    # "turbine": "6MW",
    "design_phases": [
        'ArraySystemDesign',
        'ExportSystemDesign',
        "MooringSystemDesign",
        "SemiSubmersibleDesign",
        'OffshoreSubstationDesign'
    ],
    "install_phases": {
        "MooredSubInstallation": ("MooringSystemInstallation", 0.5),
        "MooringSystemInstallation": 0,
        "ArrayCableInstallation": 0,
        "ExportCableInstallation": 0,
        "FloatingSubstationInstallation": 0
    },
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
    "install_phases": {
        "MooredSubInstallation": ("MooringSystemInstallation", 0.5),
        "MooringSystemInstallation": 0,
        "ArrayCableInstallation": 0,
        "ExportCableInstallation": 0,
        "FloatingSubstationInstallation": 0
    },
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
        "steel_cost_rate": 6000,
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
    "install_phases": {
        "MooredSubInstallation": ("MooringSystemInstallation", 0.5),
        "MooringSystemInstallation": 0,
        "ArrayCableInstallation": 0,
        "ExportCableInstallation": 0,
        "FloatingSubstationInstallation": 0
    },
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
        "steel_cost_rate": 0,
        "ballast_cost_rate": 0,
    },

}


configs = {
    # "2019 Aqua Ventus": AquaVentus_match,
    "Aqua Ventus": AquaVentus_orbit,
    "IEA 15MW": IEA15MW_steel,
    "NASA Floater": IEA15MW_concrete
    # "US_10MW_shallow": us_15MW_shallow,
    # "US_15MW_deep": us_10MW_deep,
    # "US_15MW_shallow": us_15MW_shallow,
    # "US_10MW_deep": us_10MW_deep,
}
