from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning
from odoo import api, fields, models


class Product(models.Model):
    _inherit = 'purchase.order.line'

    @api.onchange('product_qty')
    def _check_something(self):
        for record in self:
            if record.product_qty > 20:
                raise UserError(("Your product quantity is grater than 20 : %s" % record.product_qty))


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    is_company = fields.Selection([('person', 'Individual'),
                                   ('company', 'Company')], "Is Company: ", related='partner_id.company_type')