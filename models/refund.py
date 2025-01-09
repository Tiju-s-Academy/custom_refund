from odoo import api, fields, models,_


class Refund(models.Model):
    """
    The Refund model stores information about refund requests made by students.
    
    Fields:
        - fullname: Full name of the person requesting a refund.
        - admission_no: Admission number of the student.
        - email: Email address of the student.
        - phone: Contact phone number of the student.
        - address: Residential address of the student.
        - batch: Class or batch of the student.
        - refund_reason: Reason for the refund, linked to the Refund Reason model.
        - request_date: Date when the refund was requested (default: today).
        - status_id: Status of the refund process, linked to the Reasons Handler model.
        - payment_date: Date the refund payment was made.
        - payment_method: Method used to process the refund (either 'cash' or 'bank', default: 'bank').
        - total_amount_paid: Total amount paid and eligible for a refund.
        - payment_receipts: Uploadable document (binary field) as proof of payment.
    """
    _name = 'refund'
    _description = 'Refund'
    _rec_name = 'fullname'
    _inherit = ['mail.thread','mail.activity.mixin']

    fullname = fields.Char(string="Full Name",trackinget=True)
    admission_no = fields.Char(string="Admission No")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone",trackinget=True)
    address = fields.Char(string="Address")

    batch = fields.Char(string="Class",trackinget=True)
    refund_reason = fields.Many2one('refund.reason', string="Refund Reason",trackinget=True)
    request_date = fields.Date(string="Request Date",default=fields.Date.today())

    status_id = fields.Many2one('reasons.handler', string="Current Status",trackinget=True)

    payment_date = fields.Date(string="Payment Date",trackinget=True)
    payment_method = fields.Selection([('cash', 'Cash'),('bank', 'Bank')], string="Payment Method",default='bank')

    total_amount_paid = fields.Float(string="Total Amount Paid",default="",trackinget=True)

    payment_receipts = fields.Binary(string="Payment Receipts")

    state = fields.Selection([('draft', 'Draft'),('submitted', 'Submitted'),
                              ('move_to_verification', 'Move To Verification'),
                              ('verified', 'Verified'),
                              ('sales_verified','Sales Verified'),
                              ('in_progress','In Progress'),
                              ('approved','Approved'),
                              ('paid','Paid'),
                              ('canceled','Canceled')], string="Status",default='draft',trackinget=True)

    is_sales_person = fields.Boolean(compute='_compute_is_sales_person',strore=True)

    def action_submit(self):
        self.write({'state':'submitted'})

    def action_move_to_verification(self):
        self.write({'state':'move_to_verification'})

    def action_verify(self):
        self.write({'state':'verified'})

    def action_sales_verify(self):
        self.write({'state': 'sales_verified'})

    def action_partial_approve(self):
        self.write({'state':'in_progress'})

    def action_approve(self):
        self.write({'state':'approved'})

    def action_paid(self):
        self.write({'state':'paid'})

    @api.depends('state')
    def _compute_is_sales_person(self):
        for record in self:
            if self.env.user.id == record.status_id.manage_id.id and record.state == 'verified':
                print("hello")
                record.is_sales_person = True
            else:
                record.is_sales_person = False













