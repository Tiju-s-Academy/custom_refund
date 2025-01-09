from odoo import models,fields


class ReasonsHandler(models.Model):
    """
    This model is used to handle and store reasons or statuses for specific operations.
    It includes the name of the status and the user who resolved it.
    """
    _name = 'reasons.handler'
    _description = 'Reasons Handler'

    # The name or status of the reason (e.g., Class Not Attend , Class Attended)
    name = fields.Char(string='Status', required=True)
    
    # Reference to the user who resolved or managed the reason
    manage_id = fields.Many2one('res.users', string='Resolved By')