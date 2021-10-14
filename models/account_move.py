from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class AccountMove(models.Model):
    _inherit = 'account.move'

    cust_or_comp = fields.Char(string="Customer or Company")

    @api.onchange('partner_id')
    def _check_partner(self):
        if self.partner_id.is_company == True:
            self.cust_or_comp = "Company PO"
        elif self.partner_id.is_company == False:
            self.cust_or_comp = "Customer PO"

    def unlink(self):
        if self.amount_total > 10000:
            raise ValidationError("Amount is Greater then 10,000, You can not delete this.")
        return super(AccountMove, self).unlink()


class AccountPayment(models.TransientModel):
    _inherit = 'account.payment.register'

    def action_create_payments(self):
        active_id = self.env['account.move'].search([('id', '=', self.env.context.get('active_id'))])

        if active_id.cust_or_comp == "Company PO" and self.amount <= 1000:
            raise ValidationError("Amount must be more then 1000")
        else:
            payments = self._create_payments()

            if self._context.get('dont_redirect_to_payments'):
                return True

            action = {
                'name': _('Payments'),
                'type': 'ir.actions.act_window',
                'res_model': 'account.payment',
                'context': {'create': False},
            }
            if len(payments) == 1:
                action.update({
                    'view_mode': 'form',
                    'res_id': payments.id,
                })
            else:
                action.update({
                    'view_mode': 'tree,form',
                    'domain': [('id', 'in', payments.ids)],
                })
            return action
