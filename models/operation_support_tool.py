# -*- coding: utf-8 -*-

from odoo import api, fields, tools, models

class OperationSupportTool(models.Model):
    # ------------ Private Attributes -------------
    _name = "operation.support.tool"
    _description = "Operation Support tool"
            
    # ------------ Fields Declaration -------------

    # Basic
    name = fields.Text("SELECT", required=True)
    ost_from = fields.Text("FROM", required=True)
    ost_where = fields.Text("WHERE")
    ost_group_by = fields.Text("GROUP BY")

    ost_output = fields.Text("Output", readonly=True)

    def action_query(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute("""CREATE or REPLACE VIEW %s as (
            %s
            %s
            %s
        )""" % (self._table, self._select(), self._from(), self._group_by()))
        self.ost_output = self.env.cr.dictfetchall()

    def _select(self):
        select_str = """
            SELECT
            self.name
        """
        return select_str

    def _from(self):
        from_str = """
            FROM
            self.ost_from
        """
        return from_str

    def _group_by(self):
        group_by_str = """
            GROUP BY
            self.ost_where
        """
        return group_by_str
    