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
    # "site": {
    #     "depth": 150,
    #     "distance": 100,
    #     "distance_to_landfall": 100
    # },
    "port": {
        "monthly_rate": 1e6,
    },
    'semisubmersible_design': {
        'stiffened_column_CR': 6000,
        'truss_CR': 5000,
        'heave_plate_CR': 6000,
        'secondary_steel_CR': 10000,
    },
    "project_parameters": {
        "turbine_capex": 1500
    },
    "weather": "US_east_coast"
}

# Define specific scenario inputs
us_10MW_shallow = {
    **base,
    **US_east_coast,
    "turbine": "10MW",
    "site": {
        "depth": 150,
        "distance": 50,
        "distance_to_landfall": 50
    }
}

us_15MW_deep = {
    **base,
    **US_east_coast,
    "turbine": "15MW",
    "site": {
        "depth": 400,
        "distance": 200,
        "distance_to_landfall": 200
    }

}

configs = {
    "US_10MW_shallow": us_10MW_shallow,
    "US_15MW_deep": us_15MW_deep
}
