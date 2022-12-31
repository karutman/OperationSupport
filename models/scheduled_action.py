from odoo import models, fields
import logging

_logger = logging.getLogger(__name__)

class ScheduledAction(models.Model):
   _name = 'scheduled.action'
   def action_done(self):
       _logger.warning("Odoo Scheduled Action is running")
       