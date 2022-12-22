# -*- coding: utf-8 -*-

from odoo import fields, models

class OperationSupportProject(models.Model):
    # ------------ Private Attributes -------------
    _name = "operation.support.project"
    _description = "project start"
    
    # ------------ Fields Declaration -------------

    # Basic
    projectname = fields.Char("Title", required=True)
    projectdescription = fields.Text("Description")
    projectcustomer = fields.Char("Title", required=True)
    projectdate_availability = fields.Date("Available From")
    projectdate_expired = fields.Date("Available To")
