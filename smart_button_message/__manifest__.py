# -*- coding: utf-8 -*-
{
    'name': "smart_button_message",

    'summary': """
        Create smart button on res partner and crm lead to edit messages from chatter""",

    'description': """
        Create smart button on res partner and crm lead to edit messages from chatter
    """,

    'author': "Odoo S.A.",
    'website': "http://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'smart.button.message',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'crm'],

    # always loaded
    'data': [
        'views/res_partner.xml',
        'views/crm_lead.xml',
    ],
}