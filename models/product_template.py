from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    is_company = fields.Selection([('person', 'Individual'),
                                   ('company', 'Company')], "Is Company: ")
