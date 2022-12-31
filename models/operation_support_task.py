# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from datetime import datetime
from odoo.tools import date_utils, float_compare, float_is_zero
from odoo.exceptions import UserError, ValidationError

class OperationSupportTask(models.Model):
    # ------------ Private Attributes -------------
    _name = "operation.support.task"
    _description = "Operation Support Task"
    _order = "start_time"
        
    def _datetime_today(self):
        return fields.datetime.now()
    # ------------ Fields Declaration -------------

    # Basic
    name = fields.Char(string='Task Reference', required=True,
                         readonly=True, default=lambda self: _('New'))
    start_time = fields.Datetime("Start time", default=lambda self: self._datetime_today(), required=True)
    action = fields.Text("Action")
    end_time = fields.Datetime("End time", default=lambda self: self._datetime_today())
    usage_time = fields.Float("Usage time", default=1.0)

   # Special
    active = fields.Boolean("Active", default=True)

    # Relational
    ticket_id = fields.Many2one("operation.support", string="Ticket ID")
    user_id = fields.Many2one("res.users", string="User name")

    # ------------------ Constrains and Onchanges --------------------
 
    @api.onchange('start_time', 'end_time')
    @api.depends('start_time', 'end_time')
    def _onchange_usage_time(self):
        t = self.end_time - self.start_time
        self.usage_time = float(t.days)*24 + (float(t.seconds)/3600)
 
    @api.constrains("start_time", "end_time")
    def _check_startend_difference(self):
        for times in self:
            if (
                times.end_time.strftime('%Y-%m-%d %H:%M:%S') <= times.start_time.strftime('%Y-%m-%d %H:%M:%S')
            ):
                raise ValidationError(
                    "The start time must be happen before end time! "
                    + "You must change start or end time."
                )

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'operation.support.task.id') or _('New')
        res = super(OperationSupportTask, self).create(vals)
        return res
