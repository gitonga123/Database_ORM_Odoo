# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Amodel(models.Model):
	_name = "amodel.name"
	name = fields.Char(string="Enter your Name", help="First Last Others", default="First Last Others")
	total = fields.Float(compute="_compute_total", store="True")
	value = fields.Float(string="Enter The value?")
	tax = fields.Float(string="Enter the tax %?")

	@api.depends('value','tax')
	def _compute_total(self):
		record.total = record.value * record.tax


class Course(models.Model):
	_name='openacademy.course'

	name = fields.Char(string="Title", required=True)
	description = fields.Text()
		
