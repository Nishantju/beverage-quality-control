"""
=========================================
Project Configuration
=========================================

Purpose:
    Store information about every dataset
    in one place.

Author: Nishant Kumar
"""

DATASETS = {

    "apple": {

        # Display name
        "display_name": "Apple Quality",

        # Dataset path
        "file_path": "datasets/apple_quality.csv",

        # Target column
        "target_column": "Quality",

        # Columns to remove
        "drop_columns": [
            "A_id"
        ],

        # Numerical columns
        "numeric_columns": [
            "Size",
            "Weight",
            "Sweetness",
            "Crunchiness",
            "Juiciness",
            "Ripeness",
            "Acidity"
        ]

    },
    "banana": {

        "display_name": "Banana Quality",

        "file_path": "datasets/banana_quality_dataset.csv",

        "target_column": "quality_category",

        "drop_columns": [
            "sample_id",
            "quality_score",
            "harvest_date"
        ],

        "numeric_columns": [
            "ripeness_index",
            "sugar_content_brix",
            "firmness_kgf",
            "length_cm",
            "weight_g",
            "tree_age_years",
            "altitude_m",
            "rainfall_mm",
            "soil_nitrogen_ppm"
        ],

        "categorical_columns": [
            "variety",
            "region",
            "ripeness_category"
        ]

    },


    "milk": {

        "file_path": "datasets/milk.csv",

        "drop_columns": [],

        "numeric_columns": [

            "pH",
            "Temprature",
            "Taste",
            "Odor",
            "Fat",
            "Turbidity",
            "Colour"

        ],

        "target_column": "Grade"

    },

    "orange": {

        "display_name": "Orange Quality",

        "file_path": "datasets/orange.csv",

        "target_column": "Quality (1-5)",

        "drop_columns": [],

        "numeric_columns": [

            "Size (cm)",
            "Weight (g)",
            "Brix (Sweetness)",
            "pH (Acidity)",
            "Softness (1-5)",
            "HarvestTime (days)",
            "Ripeness (1-5)"

        ],

        "categorical_columns": [

            "Color",
            "Variety",
            "Blemishes (Y/N)"

        ]

    }



}


FORM_OPTIONS = {

    "banana": {

        "variety": [
            "Blue Java",
            "Burro",
            "Cavendish",
            "Fehi",
            "Lady Finger",
            "Manzano",
            "Plantain",
            "Red Dacca"
        ],

        "region": [
            "Brazil",
            "Colombia",
            "Costa Rica",
            "Ecuador",
            "Guatemala",
            "Honduras",
            "India",
            "Philippines"
        ],

        "ripeness_category": [
            "Green",
            "Overripe",
            "Ripe",
            "Turning"
        ]
    },

    "milk": {

        "Taste": [
            "Bad",
            "Good"
        ],

        "Odor": [
            "Bad",
            "Good"
        ],

        "Fat": [
            "Low",
            "High"
        ],

        "Turbidity": [
            "Clear",
            "Cloudy"
        ],

        "Colour": {

            "⚫ Very Dark (240)": 240,
            "⚫ Dark (245)": 245,
            "◼ Medium Dark (246)": 246,
            "◼ Medium (247)": 247,
            "◻ Medium Bright (248)": 248,
            "⬜ Bright (250)": 250,
            "✨ Very Bright (253)": 253,
            "🤍 Almost White (254)": 254,
            "🤍 Pure White (255)": 255

        }

    },

    "orange": {

        "Color": [
            "Deep Orange",
            "Light Orange",
            "Orange",
            "Orange-Red",
            "Yellow-Orange"
        ],

        "Variety": [
            "Ambiance",
            "Blood Orange",
            "California Valencia",
            "Cara Cara",
            "Clementine",
            "Clementine (Seedless)",
            "Hamlin",
            "Honey Tangerine",
            "Jaffa",
            "Midsweet (Hybrid)",
            "Minneola (Hybrid)",
            "Moro (Blood)",
            "Murcott (Hybrid)",
            "Navel",
            "Navel (Early Season)",
            "Navel (Late Season)",
            "Ortanique (Hybrid)",
            "Satsuma Mandarin",
            "Star Ruby",
            "Tangelo (Hybrid)",
            "Tangerine",
            "Temple",
            "Valencia",
            "Washington Navel"
        ],

        "Blemishes (Y/N)": [
            "N",
            "N (Minor)",
            "N (Split Skin)",
            "Y (Bruise)",
            "Y (Bruising)",
            "Y (Minor Insect Damage)",
            "Y (Minor)",
            "Y (Mold Spot)",
            "Y (Scars)",
            "Y (Split Skin)",
            "Y (Sunburn Patch)",
            "Y (Sunburn)"
        ]

    }

}

REQUIRED_FIELDS = {

    "apple": [

        "size",
        "weight",
        "sweetness",
        "crunchiness",
        "juiciness",
        "ripeness",
        "acidity"

    ],

    "banana": [

        "variety",
        "region",
        "ripeness_index",
        "ripeness_category",
        "sugar_content_brix",
        "firmness_kgf",
        "length_cm",
        "weight_g",
        "tree_age_years",
        "altitude_m",
        "rainfall_mm",
        "soil_nitrogen_ppm"

    ],

    "milk": [
        "pH",
        "Temprature",
        "Taste",
        "Odor",
        "Fat",
        "Turbidity",
        "Colour"
    ],

    "orange": [

        "Size (cm)",
        "Weight (g)",
        "Brix (Sweetness)",
        "pH (Acidity)",
        "Softness (1-5)",
        "HarvestTime (days)",
        "Ripeness (1-5)",
        "Color",
        "Variety",
        "Blemishes (Y/N)"

    ]

}

FIELD_LABELS = {

    "size": "Size",
    "weight": "Weight",
    "sweetness": "Sweetness",
    "crunchiness": "Crunchiness",
    "juiciness": "Juiciness",
    "ripeness": "Ripeness",
    "acidity": "Acidity",

    "variety": "Variety",
    "region": "Region",
    "ripeness_index": "Ripeness Index",
    "ripeness_category": "Ripeness Category",
    "sugar_content_brix": "Sugar Content (°Brix)",
    "firmness_kgf": "Firmness (kgf)",
    "length_cm": "Length (cm)",
    "weight_g": "Weight (g)",
    "tree_age_years": "Tree Age (years)",
    "altitude_m": "Altitude (m)",
    "rainfall_mm": "Rainfall (mm)",
    "soil_nitrogen_ppm": "Soil Nitrogen (ppm)",


    "pH": "pH",
    "Temprature": "Temperature",
    "Taste": "Taste",
    "Odor": "Odor",
    "Fat": "Fat",
    "Turbidity": "Turbidity",
    "Colour": "Colour",


    "Size (cm)": "Size (cm)",

    "Weight (g)": "Weight (g)",

    "Brix (Sweetness)": "Brix (Sweetness)",

    "pH (Acidity)": "pH (Acidity)",

    "Softness (1-5)": "Softness (1-5)",

    "HarvestTime (days)": "Harvest Time (days)",

    "Ripeness (1-5)": "Ripeness (1-5)",

    "Color": "Color",

    "Variety": "Variety",

    "Blemishes (Y/N)": "Blemishes",

}

INPUT_FIELDS = {

    "apple": [

        "size",
        "weight",
        "sweetness",
        "crunchiness",
        "juiciness",
        "ripeness",
        "acidity"

    ],

    "banana": [

        "variety",
        "region",
        "ripeness_index",
        "ripeness_category",
        "sugar_content_brix",
        "firmness_kgf",
        "length_cm",
        "weight_g",
        "tree_age_years",
        "altitude_m",
        "rainfall_mm",
        "soil_nitrogen_ppm"

    ],

    "milk": [
        "pH",
        "Temprature",
        "Taste",
        "Odor",
        "Fat",
        "Turbidity",
        "Colour"
    ],

    "orange": [

        "Size (cm)",
        "Weight (g)",
        "Brix (Sweetness)",
        "pH (Acidity)",
        "Softness (1-5)",
        "HarvestTime (days)",
        "Ripeness (1-5)",
        "Color",
        "Variety",
        "Blemishes (Y/N)"

    ]

}
