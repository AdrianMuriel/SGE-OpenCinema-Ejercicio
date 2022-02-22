# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Film(models.Model):
    _name = 'opencinema.film'
    _description = 'Peliculas Open Cinema'
    name = fields.Char()
    description = fields.Text()
    release_date = fields.Date(string='Release')
    year = fields.Char(required=True)
    duration = fields.Integer()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
