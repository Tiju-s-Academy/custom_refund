from odoo.http import Controller, request, route
from odoo import http,fields
from datetime import datetime, timedelta

class StudentRefundController(Controller):
    @route('/student_refund', auth='public', website=True)
    def student_refund(self, **kwargs):
        status_id = request.env['reasons.handler'].sudo().search([])
        refund_reason = request.env['refund.reason'].sudo().search([])
        values = {
            'status_id': status_id,
            'refund_reason': refund_reason,
        }
        return request.render('custom_refund.student_refund_template',values)

    @http.route('/student_refund/submit', type='http', auth='public', website=True, methods=['POST'])
    def student_refund_submit(self, **post):
        refund_data = {
            'fullname': post.get('fullname'),
            'admission_no': post.get('admission_number'),
            'phone': post.get('phone_number'),
            'address': post.get('address'),
            'batch': post.get('class'),
            'status_id': int(post.get('status_id')) if post.get('status_id') else False,
            'refund_reason': int(post.get('refund_reason')) if post.get('refund_reason') else False,
            'study_mode': post.get('study_mode'),
            'student_department': post.get('student_department'),
            'team': post.get('team'),
            'state': 'submitted',
        }
        refund = request.env['refund'].sudo().create(refund_data)

        officer_group = request.env.ref('custom_refund.officer_refund')
        officers = request.env['res.users'].sudo().search([('groups_id', 'in', officer_group.id)])
        activity_type = request.env.ref('custom_refund.mail_activity_refund')
        for officer in officers:
            request.env['mail.activity'].sudo().create({
                'res_id': refund.id,
                'res_model_id': request.env['ir.model']._get('refund').id,
                'activity_type_id': activity_type.id,
                'user_id': officer.id,
                'note': 'Follow up on the refund request submitted by the student.',
                'date_deadline': fields.Date.today(),
            })
        return request.redirect('/refund_thanks')

    @route('/refund_thanks', auth='public', website=True)
    def refund_thanks(self,**kwargs):
        return request.render('custom_refund.refund_thanks_web_form_template')

