# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Operation Support Managment",
    "summary": """
        Operation Support Management""",
    "version": "1.0.0.0.1",
    "license": "AGPL-3",
    "author": "Odoo Community Association (OCA)",
    "depends": ["base"],
    "data": [
        'security/ir.model.access.csv',
        'views/operation_support_project_views.xml',
        'views/operation_support_menus.xml',
    ],
    "application": True,
    "installable": True,
}
