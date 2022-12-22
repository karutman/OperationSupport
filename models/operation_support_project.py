# -*- coding: utf-8 -*-

from odoo import fields, models

class OperationSupportProject(models.Model):
    # ------------ Private Attributes -------------
    _name = "operation.support.project"
    _description = "project start"
    
    # ------------ Fields Declaration -------------

    # Basic
    project_name = fields.Char("Title", required=True)
    project_description = fields.Text("Description")
    project_customer = fields.Char("Title", required=True)
    project_date_availability = fields.Date("Available From")
    project_date_expired = fields.Date("Available To")
