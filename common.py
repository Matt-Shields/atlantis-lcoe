"""Common functions and data across all scenarios."""

__author__ = "Matt Shields"
__copyright__ = "Copyright 2022, National Renewable Energy Laboratory"
__maintainer__ = "Matt Shields"
__email__ = "matt.shields@nrel.gov"


import pandas as pd


base = {
    ### Project, port and site information
    "plant": {
        "layout": "ring",
        # "num_turbines": 100,
        "turbine_spacing": 5,
        "row_spacing": 7,
        "substation_distance": 1,
        "capacity": 600
    },
    # "turbine": "10MW_generic",

    "port": {
        "sub_assembly_lines": 3,
        # "sub_storage": "int (optional, default: inf)",
        "turbine_assembly_cranes": 3,
        # "assembly_storage": "int (optional, default: inf)",
        # "monthly_rate": "USD/mo (optional)",
        # "name": "str (optional)",
    },

    ### Custom Moored Substructure Installation
    "substructure": {
        "takt_time": 168 * 2,
        # "towing_speed": "int | float (optional, default: 6 km/h)",
        # "unit_cost": "USD",
    },
    "support_vessel": "example_support_vessel",
    "towing_vessel": "example_towing_vessel",
    "towing_vessel_groups": {
        "towing_vessels": 2,
        "station_keeping_vessels": 3,
        "num_groups": 3,
    },
    # 'semisubmersible_design': {
    #     'stiffened_column_CR': '$/t (optional, default: 3120)',
    #     'truss_CR': '$/t (optional, default: 6250)',
    #     'heave_plate_CR': '$/t (optional, default: 6250)',
    #     'secondary_steel_CR': '$/t (optional, default: 7250)',
    #     'towing_speed': 'km/h (optional, default: 6)',
    #     'design_time': 'h, (optional, default: 0)',
    #     'design_cost': 'h, (optional, default: 0)'
    # },

    ### Mooring Installation
    "mooring_install_vessel": "example_anchor_handling_vessel",
    'mooring_system_design': {
        'num_lines': 3,
        'anchor_type': "Drag Embedment",
        # 'mooring_line_cost_rate': 'int | float (optional)',
        # 'drag_embedment_fixed_length': 'int | float (optional, default: .5km)'
    },

    # Electrical
    # 'substation_design': {
    #     'mpt_cost_rate': 'USD/MW (optional)',
    #     'topside_fab_cost_rate': 'USD/t (optional)',
    #     'topside_design_cost': 'USD (optional)',
    #     'shunt_cost_rate': 'USD/MW (optional)',
    #     'switchgear_cost': 'USD (optional)',
    #     'backup_gen_cost': 'USD (optional)',
    #     'workspace_cost': 'USD (optional)',
    #     'other_ancillary_cost': 'USD (optional)',
    #     'topside_assembly_factor': 'float (optional)',
    #     'oss_substructure_cost_rate': 'USD/t (optional)',
    #     'oss_pile_cost_rate': 'USD/t (optional)',
        'num_substations': 2,
    #     'design_time': 'h (optional)'
    # },
    'array_system_design': {
    #     'design_time': 'hrs (optional)',
        'cables': ["XLPE_66kV_1", "XLPE_66kV_2"],
    #     'touchdown_distance': 'm (optional, default: 0)',
    #     'average_exclusion_percent': 'float (optional)'
    },
    # 'array_system': {
    #     'num_strings': 'int (optional, default: 10)',
    #     'free_cable_length': 0.5
    # },
    'export_system_design': {
        'cables': 'XLPE_220kV_1',
        # 'num_redundant': 'int (optional)',
        # 'touchdown_distance': 'm (optional, default: 0)',
        # 'percent_added_length': 'float (optional)'
    },
    # 'export_system': {
    #     'interconnection_distance': 'km (optional); default: 3km',
    #     'interconnection_voltage': 'kV (optional); default: 345kV'
    # },
    # 'landfall': {
    #     'trench_length': 'km (optional)',
    #     'interconnection_distance': 'km (optional)'
    # },
    'array_cable_install_vessel': 'example_cable_lay_vessel',
    # 'array_cable_bury_vessel': 'str (optional)',
    # 'array_cable_trench_vessel': 'str (optional)',
    'export_cable_install_vessel': 'example_export_cable_lay_vessel',
    # 'export_cable_bury_vessel': 'str | dict (optional)',
    # 'export_cable_trench_vessel': 'str (optional)',
    'oss_install_vessel': 'example_support_vessel',
    'offshore_substation_substructure': {
        "mooring_cost": 2.5e6
    },

    # Project Finance
    # 'project_parameters': {
    #     # 'turbine_capex': 1100,
    #     # 'ncf': 0.5,
    #     # 'offtake_price': 80,
    #     # 'project_lifetime': 25,
    #     # 'discount_rate': 0.025,
    #     # 'opex_rate': 150,
    #     'construction_insurance': 30,
    #     'construction_financing': 124,
    #     'contingency': 196,
    #     'commissioning': 30,
    #     'decommissioning': 28,
    #     'site_auction_price': 52925529,
    #     'site_assessment_cost': 50486746,
    #     'construction_plan_cost': 28604389,
    #     'installation_plan_cost': 0
    # },

    # ORBIT Configuration

}
