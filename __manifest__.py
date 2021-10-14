# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Gym ERP',
    'version': '1.0',
    'author': 'Mehul Darji',
    'category': 'Tutorials',
    'summary': 'Tutorials of gym ERP',
    'description': "We are learning what is odoo and development in odoo",
    'website': 'https://www.odoo.com',
    'depends': [
        'base', 'sale', 'account', 'purchase', 'product'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/gym_info_views.xml',
        'wizard/update_phone_wizard_view.xml',
        'wizard/sale_order_wizard_view.xml',
        'views/account_invoice_views.xml',
        'views/partner_is_company_views.xml',
        'views/purchase_order_views.xml',
        'views/product_template.xml',
        'views/saleorder_with_wizard.xml',


    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
