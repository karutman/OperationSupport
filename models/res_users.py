# -*- coding: utf-8 -*-

from odoo import fields, models


class ResUsers(models.Model):

    # ---------------------------------------- Private Attributes ---------------------------------

    _inherit = "res.users"
 

    # --------------------------------------- Fields Declaration ----------------------------------

    # Relational
    task_ids = fields.One2many(
        "operation.support.task", "user_id", string="Tasks"
    )