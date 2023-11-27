# -*- coding: utf-8 -*-

from odoo import models, fields, api


class pb_lead(models.Model):
     _inherit = 'crm.lead'
     _name = 'pb_lead.pb_lead'
     _description = 'pb_lead.pb_lead'

     center_number = fields.Char(string='Center Number')
