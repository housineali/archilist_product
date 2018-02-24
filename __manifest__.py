# -*- coding: utf-8 -*-
{
    'name': "Products Managements",

    'summary': """
        That module is Product Managements""",
    'description': """
That module created for Product Managements.
======================================
Key Features:
------------
* Product Category.
* Product Generics.
* Product Variants.
""",
    'author': 'Binary Labs LLC & Mahmoud Elmenshawy',
    'website': '',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Real State',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'auth_signup', 'mail', 'web_planner', 'web', 'portal','product'],

    # always loaded
    'data': [
        # 'security/security.xml',
        # 'security/ir.model.access.csv',
        # 'data/data.xml',
        'views/product_views.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'application': True
}
