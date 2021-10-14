from odoo import api, fields, models


class CompanyInfo(models.Model):
    _inherit = 'sale.order'

    company_check = fields.Boolean('Company check')

    @api.onchange('partner_id')
    def company_info(self):
        print('company')
        if self.partner_id.is_company == True:
            self.company_check = True
        else:
            self.company_check = False

    is_customer_10per = fields.Boolean("10% Discount")  # No use
    is_customer_5per = fields.Boolean("5% Discount")   # No use
    discount = fields.Float("Discount")

    customer_10per_5per = fields.Selection([('is_10per', '10% Discount'),
                                            ('is_5per', '5% Discount')], string="Discount")

    @api.onchange('customer_10per_5per')
    def on_change_state(self):
        if self.customer_10per_5per == 'is_10per':
            self.discount = self.amount_untaxed * 10 / 100
            self.amount_total = self.amount_untaxed - self.discount + self.amount_tax
        elif self.customer_10per_5per == 'is_5per':
            self.discount = self.amount_untaxed * 5 / 100
            self.amount_total = self.amount_untaxed - self.discount + self.amount_tax
        else:
            self.discount = 0

    def copy(self, default=None):
        print("Successfully Overided")
        if default is None:
            default = {}
        if not default.get('partner_id'):
            print(not default.get('partner_id'))
            default['partner_id'] = 43
            # for rec in self.order_line:
            lines = [(5, 0, 0)]
            val = {
                'product_id': 53
            }
            lines.append((0, 0, val))
            self.order_line = lines
        return super(CompanyInfo, self).copy(default)
