# -*- coding: utf-8 -*-

from odoo import models, fields, api


class pb_lead(models.Model):
     _inherit = 'crm.lead'

     center_number = fields.Char(string='Center Number')
