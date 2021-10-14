# from odoo import api, fields, models
#
#
# class OnlyCompany(models.Model):
#     _inherit = 'account.move'
#
#     partner_id = fields.Char("Customer")  # This is of mo use
#     partner_id_1 = fields.Many2one('res.partner')
#
#
# # class IsCompany(models.Model):
# #     _inherit = 'res.partner'
# #
# #     is_company = fields.Boolean("Is Company")  # This is of mo use
# #
# #     company_type = fields.Selection([('person', 'Individual'),
# #                                      ('company', 'Company')], 'Company Type')
