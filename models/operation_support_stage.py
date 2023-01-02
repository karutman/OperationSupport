# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class OperationSupportStage(models.Model):
    # ------------ Private Attributes -------------
    _name = "operation.support.stage"
    _description = "Operation Support Stage"
    _order = "sequence, id"
        
    # ------------ Fields Declaration -------------

    # Basic
    name = fields.Char(string='Name', required=True)
    sequence = fields.Integer("Sequence", required=True)
    closing_stage = fields.Boolean("Closing Stage", default=False)