# -*- coding: utf-8 -*-

from odoo import api, fields, tools, models
from datetime import datetime, date, time, timedelta

class OperationSupport(models.Model):
    # ------------ Private Attributes -------------
    _name = "operation.support"
    _description = "Operation Support"
    _order = "id desc"
        
    # ------------- Methods -----------------------

    def _generate_ticket_id(self):
        return "TK" + str(fields.Datetime.now()).replace(" ","").replace("-","").replace(":","")

    def _datetime_today(self):
        return fields.datetime.now()

    # ------------ Fields Declaration -------------

    # Basic
    name = fields.Char("Ticket ID", default=lambda self: self._generate_ticket_id(), readonly=True)
    open_case_date = fields.Datetime("Open case time", default=lambda self: self._datetime_today(), required=True)
    contact_persion = fields.Char("Customer name", required=True)
    contact_email_phone = fields.Char("Customer contact", required=True)
    respond_date = fields.Datetime("Respond time", default=lambda self: self._datetime_today(), required=True)
    request_detail = fields.Text("Issue Description", required=True)
    root_cause = fields.Text("Root Cause")
    cm_type = fields.Selection(
        selection=[
            ('1', 'Hardware'),
            ('2', 'Application'),
            ('3', 'Link'),
            ('4', 'Modifly Config'),
            ('5', 'Human Error'),
            ('6', 'Add/Move/Change'),
            ('7', 'Setup New PC/NB'),
            ('8', 'Unknown etc.')
            ],
            string="CM Type"
        )

    # Special
    state = fields.Selection(
        selection=[
            ('inprogress', 'In Progress'),            
            ('waiting', 'Waiting on someone else'),
            ('completed', 'Completed'),
            ('canceled', 'Canceled'),
            ],
            string="Case Status",
            default='inprogress',
        )
    case_complete_date = fields.Datetime("Completed time")
    
    # Relational
    project_id = fields.Many2one("operation.support.project", string="Project name")
    task_ids = fields.One2many("operation.support.task", "ticket_id", string="Tasks")
    tag_ids = fields.Many2many("operation.support.tag", string="Tags")
    user_id = fields.Many2many("res.users", string="Engineer Support")
    
    # Computed
    total_usage_time = fields.Float(
        "Total usage time", 
        default=0.0,
        compute="_compute_total_usage_time",
        help="Total usage time of all tasks in this ticket",
    )

    time_respond = fields.Float("Time to respond")
    time_ticket = fields.Float("Time from start to completed/cancel")
    
    # ---------------------- Compute methods -------------------
    @api.depends("task_ids.usage_time")
    def _compute_total_usage_time(self):
        for times in self:
            times.total_usage_time = sum(times.task_ids.mapped("usage_time"))

    # ----------------------- CRUD Methods ----------------------
    def unlink(self):
        if not set(self.mapped("state")) <= {'notstarted'}:
            raise UserError("Only Not Started can be deleted.")
        return super().unlink()

    # ----------------------- Action Methods ---------------------

    def action_completed(self):
        if "canceled" in self.mapped("state"):
            raise UserError("The Canceled ticket cannot be Completed.")
        self.case_complete_date = fields.Datetime.now()
        t = self.respond_date - self.open_case_date
        self.time_respond = (float(t.days)*24) + (float(t.seconds)/3600)
        t = self.case_complete_date - self.open_case_date
        self.time_ticket = (float(t.days)*24) + (float(t.seconds)/3600)
        return self.write({"state": "completed"})
    
    def action_waiting(self):
        if "canceled" in self.mapped("state"):
            raise UserError("The Canceled ticket cannot be Waiting.")
        return self.write({"state": "waiting"})
    
    def action_canceled(self):
        if "completed" in self.mapped("state"):
            raise UserError("The Completed ticket cannot be Canceled.")
        return self.write({"state": "canceled"})

    def action_inprogress(self):
        if "completed" in self.mapped("state"):
            raise UserError("The Completed ticket cannot be Inprogress.")
        return self.write({"state": "inprogress"})
