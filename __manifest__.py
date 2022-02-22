# -*- coding: utf-8 -*-
{
    'name': "Open Cinema",

    'summary': """ Módulo de almacenamiento de películas """,

    'description': """
        Este módulo tiene como finalidad el almacenamiento de
	peliculas indicando su Titulo, Descripción y Año de Estreno
    """,

    'author': "Adrián Muriel Zamora",
    'website': "https://www.google.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
	'security/security.xml',
        'views/opencinema.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application' : True,
}
