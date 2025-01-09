from odoo import fields,models


class RefundReason(models.Model):
    """
    The RefundReason model represents reasons provided for processing refunds.
    
    Attributes:
        name (fields.Char): A mandatory field to specify the reason for a refund.
    """

    _name = 'refund.reason'
    _description = 'Refund Reason'

    
    name = fields.Char('Reason', required=True)
