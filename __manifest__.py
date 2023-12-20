# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'OpenBiblica',
    'version': '17.0.1.0',
    'category': 'Education',
    'description': "Bible Study and Translation Platform",
    'website': 'https://www.openbiblica.com',
    'summary': 'Study and translate bible',
    'author': 'OpenBiblica',
    'depends': ['web', 'website'],
    'data': ['data/ir_sequence.xml',
        'security/ir.model.access.csv',
        'data/language_data.xml',
        'views/dictionary_views.xml',
        'views/bible_views.xml',
        'views/menus.xml',
        'web/portal_templates.xml',
        'web/bible_templates.xml',
        'web/book_templates.xml',
        'web/chapter_templates.xml',
        'web/installer_templates.xml',
        'web/verse_templates.xml',
        'web/dictionary_templates.xml'],
    'qweb': ['static/src/xml/*.xml'], 
    'assets': {
        'web.assets_backend': [
            ('include', 'openbiblica/static/src/css/web_assets_backend.css'),
            ('include', 'openbiblica/static/src/js/web_assets_backend.js'),
        ],
        'web.assets_frontend': [
            ('include', 'openbiblica/static/src/css/web_assets_frontend.css'),
            ('include', 'openbiblica/static/src/js/web_assets_frontend.js'),
            ('include', 'openbiblica/static/src/js/temp.js'),
            ('include', 'openbiblica/static/src/js/transliterate.js'),
            ('include', 'openbiblica/static/src/js/website_openbiblica.js'),                                    
        ],
        'web.assets_common': [
            ('include', 'openbiblica/static/src/css/web_assets_common.css'),
            ('include', 'openbiblica/static/src/js/web_assets_common.js'),
        ],
    },
    'icon': '/openbiblica/static/description/icon.png',
    'images': [
        'static/description/banner.png',
    ],
    'external_dependencies': {
        'python': [
            'transliterate',
        ],        
      },  
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OPL-1',
}
