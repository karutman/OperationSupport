# -*- coding: utf-8 -*-

from odoo import fields, models

class OperationSupportEngineer(models.Model):
    # ------------ Private Attributes -------------
    _name = "operation.support.engineer"
    _description = "Operation Support Engineer"
    
    # ------------ Fields Declaration -------------

    # Basic
    name = fields.Char("Engineer Name", required=True)
    email = fields.Char("Email")
    telephone = fields.Char("Telephone")
    department_id = fields.Integer("Department")

    # Special
    active = fields.Boolean("Active", default=True)
    
    # Relational
    support_ids = fields.One2many(
        "operation.support", "engineer_ids", string="Engineer ID." , domain=[("state", "in", ["notstarted","inprogress","waiting","deferred"])]
    )