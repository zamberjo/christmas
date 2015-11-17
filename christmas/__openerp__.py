# -*- encoding: utf-8 -*-

{
    'name': 'Snow!',
    'version': '1.0',
    'description':
        """
Easter Egg for Odoo.
====================

        """,
    'depends': ['web'],
    'auto_install': True,
    'author': 'Jose Zambudio Bernabeu',
    'website': 'http://www.josezambudiobernabeu.com',
    'data': [
        'views/webclient_templates.xml',
    ],
    'application': True,
    'installable': True,
    'bootstrap': True,
}
