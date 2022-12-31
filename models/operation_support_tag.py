# -*- coding: utf-8 -*-

from odoo import fields, models


class OperationSupportTag(models.Model):

    # ---------------------------------------- Private Attributes ---------------------------------

    _name = "operation.support.tag"
    _description = "Operation Support Tag"
    _order = "name"
    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "The name must be unique"),
    ]

    # --------------------------------------- Fields Declaration ----------------------------------

    # Basic
    name = fields.Char("Name", required=True)
    color = fields.Integer("Color Index")