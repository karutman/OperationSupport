# -*- coding: utf-8 -*-

from odoo import api, fields, models

class OperationSupportProject(models.Model):
    # ------------ Private Attributes -------------
    _name = "operation.support.project"
    _description = "Operation Support Project"
    _order = "name"
    _sql_constraints = [
        ("check_end_date", "CHECK(end_date <= start_date)", "The expected project' end date must after project's start"),
    ]
    
    # ------------ Fields Declaration -------------

    # Basic
    name = fields.Char("Project MA Name", required=True)
    customer = fields.Char("Customer Name", required=True)
    start_date = fields.Date("MA Start Date", required=True)
    end_date = fields.Date("MA Expired Date", required=True)
    description = fields.Text("Project MA Description")

    # Special
    active = fields.Boolean("Active", default=True)

    # Relational
    project_ids = fields.One2many("operation.support", "project_id", string="Project no.")