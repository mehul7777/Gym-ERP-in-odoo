from odoo import models, fields, api


# class ResPartner(models.Model):
#     _inherit = 'res.partner'
#
#     passed_override_write_function = fields.Boolean(string='Has passed our super method')
#
#     @api.model
#     def create(self, values):
#         # Override the original create function for the res.partner model
#         record = super(ResPartner, self).create(values)
#         record['passed_override_write_function'] = True
#         print('Passed this function. passed_override_write_function value: ' +
#               str(record['passed_override_write_function']))
#         # Return the record so that the changes are applied and everything is stored.
#         return record

class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def create(self, values):
        # Override the original create function for the res.partner model
        record = super(ResPartner, self).create(values)
        for supplement in record.gym_ids:
            supplement['is_supplement'] = True
        # print('Passed this function. passed_override_write_function value: ' +
        #       str(record['is_supplement']))
        print("Create is working")
        # Return the record so that the changes are applied and everything is stored.
        return record

    # def write(self, values):
    #     print('Values', values)
    #     # print('Values', values.gym_ids)
    #     # print('Values', self.gym_ids)
    #     # if values:
    #     #     values.update({'is_supplement': False})
    #     # return super(ResPartner, self).write(values)
    #     for supplement in values.get('gym_ids'):
    #         # supplement['is_supplement'] = False
    #         print(supplement)
    #     print("Write is working")
    #     return super(ResPartner, self).write(values)

