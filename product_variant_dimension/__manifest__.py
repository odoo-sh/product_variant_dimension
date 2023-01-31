# Copyright 2022 Sodexis
# License OPL-1 (See LICENSE file for full copyright and licensing details).

{
    "name": "Product Variant Dimension",
    "summary": """This module is used for display the Dimensions - Length, Width, Height and Dimensions UoM fields 
                  in both Product Template and Product variants""",
    "version": "15.0.1.0.0",
    "category": "Uncategorized",
    "website": "http://sodexis.com/",
    "author": "Sodexis",
    "license": "OPL-1",
    "installable": True,
    "application": False,
    "depends": [
        'sale',
    ],
    "data": [
        "views/product_views.xml",
    ],
    "cloc_exclude": [
        "**/*", # can be used to ignore an entire module.
    ],
}
