from odoo.http import Controller, request, route

class StudentRefundController(Controller):
    @route('/student_refund', auth='public', website=True)
    def student_refund(self, **kwargs):
        status_id = request.env['reasons.handler'].sudo().search([])
        print("status_id: ", status_id)
        refund_reason = request.env['refund.reason'].sudo().search([])
        print("refund_reason: ", refund_reason)
        values = {
            'status_id': status_id,
            'refund_reason': refund_reason,
        }
        return request.render('custom_refund.student_refund_template',values)

    @route('/student_refund/submit', type='http', auth='public', website=True,
           methods=['POST'])
    def student_refund_submit(self, **post):

        refund = request.env['refund'].sudo().create({
            'fullname': post.get('fullname'),
            'admission_no': post.get('admission_number'),
            'phone': post.get('phone_number'),
            'address': post.get('address'),
            'batch': post.get('class'),
            'status_id': int(post.get('status_id')),
            'refund_reason': int(post.get('refund_reason')),
            'state': 'submitted',
        })
        print(refund)
        return request.redirect('/refund_thanks')

    @route('/refund_thanks', auth='public', website=True)
    def refund_thanks(self,**kwargs):
        return request.render('custom_refund.refund_thanks_web_form_template')

