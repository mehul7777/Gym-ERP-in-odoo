from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
import re


class GymInfo(models.Model):
    _inherit = 'res.partner'
    _rec_name = 'gym_name'

    gym_name = fields.Char("Gym Name")
    joining_date = fields.Date("Joining Date")

    gym_ids = fields.One2many(comodel_name='gym.records', inverse_name='gym_schedule_id')
    gym_schedule_ids = fields.One2many(comodel_name='gym.records', inverse_name='gym_schedule_id2')  # This is of no use

    total_amount_id = fields.Many2one(comodel_name='gym.records') # This is of no use
    total_amount = fields.Float(string="Total", compute='_compute_total')

    @api.depends('gym_ids', 'total_amount')
    def _compute_total(self):
        total =0
        for record in self.gym_ids:
            print("gym_ids", self.gym_ids)
            print(record.id,record.price)
            total += record.price
        self.total_amount = total

    cust_birth_date = fields.Date(string="BirthDate")
    cust_age = fields.Char(string="Age")

    @api.onchange('cust_birth_date')
    def _onchange_birth_date(self):
        if self.cust_birth_date:
            d1 = datetime.strptime(str(self.cust_birth_date), "%Y-%m-%d").date()

            d2 = date.today()

            self.cust_age = relativedelta(d2, d1).years

    # @api.onchange('website')
    # def email_check(self):
    #     Pattern = re.compile("[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+\.[A-Z|a-z]{2,}")
    #     if Pattern.match(str(self.email)):
    #         print("True")
    #     else:
    #         print("False")
    #         raise ValidationError("Email is not valid")


class GymRecords(models.Model):
    _name = 'gym.records'

    date = fields.Date("Date")
    gym_schedule_id = fields.Many2one(comodel_name='res.partner')
    in_time = fields.Datetime("In Time")
    out_time = fields.Datetime("Out Time")
    gym_schedule_id2 = fields.Many2one(comodel_name='gym.schedule')
    is_massage = fields.Boolean("Massage")
    is_supplement = fields.Boolean("Supplement")
    price = fields.Float("Total", compute='_compute_add_total', store=True)
    total_amount = fields.Float("Total") # This is of no use

    @api.depends('is_massage', 'is_supplement', 'price')
    def _compute_add_total(self):
        if (self.is_massage == False) and (self.is_supplement == False):
            self.price = 0
        elif (self.is_massage == True) and (self.is_supplement == True):
            self.price = 100
        elif self.is_massage == True and self.is_supplement == False:
            self.price = 50.0
        elif self.is_supplement == True and self.is_massage == False:
            self.price = 50.0


class GymSchedule(models.Model):
    _name = 'gym.schedule'
    _rec_name = 'exercise_name'

    exercise_name = fields.Char("Exercise Name")
    gym_sets = fields.Integer("Sets")
    gym_reps = fields.Integer("Reps")
