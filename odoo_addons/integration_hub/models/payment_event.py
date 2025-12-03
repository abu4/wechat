# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PaymentRequiredEvent(models.Model):
    """
    定义 'payment.required' 事件的数据模型。
    此模型并非用于持久化存储，而是作为事件的数据结构和格式规范。
    实际事件通过Odoo的bus.bus、队列作业或自定义通道传递。
    """
    _name = 'integration_hub.payment_required_event'
    _description = 'Payment Required Event Structure'

    # 事件的唯一参考编号，通常对应销售订单编号
    reference = fields.Char(string='Reference', required=True, help='例如：销售订单号')
    # 支付金额和货币
    amount = fields.Float(string='Amount', digits=(12, 2), required=True)
    currency_id = fields.Many2one('res.currency', string='Currency', required=True)
    # 关联客户
    partner_id = fields.Many2one('res.partner', string='Customer', required=True)
    # 回调地址，支付平台将通知此URL
    callback_url = fields.Char(string='Callback URL', required=True)
    # 用于前端显示的描述信息
    subject = fields.Char(string='Subject', default='Order Payment')
    description = fields.Text(string='Description')
    # 附加数据，以JSON格式存储，供不同适配器存储特定信息（如微信的openid）
    adapter_data = fields.Json(string='Adapter Specific Data', default={})

    # 这是一个示例方法，用于演示如何发布此事件
    def _publish_payment_required_event(self):
        """
        发布 payment.required 事件的示例方法。
        在实际集成中，此方法将由销售订单的 action_confirm() 调用。
        """
        self.ensure_one()
        event_data = {
            'event_type': 'payment.required',
            'payload': {
                'reference': self.reference,
                'amount': self.amount,
                'currency_id': self.currency_id.id,
                'partner_id': self.partner_id.id,
                'callback_url': self.callback_url,
                'subject': self.subject,
                'description': self.description,
                'adapter_data': self.adapter_data,
            }
        }
        # TODO: 此处应调用实际的事件发布机制（如向 bus.bus 发送消息或放入队列）
        # 例如：self.env['bus.bus']._sendone('integration_hub', 'payment.required', event_data)
        _logger.info(f"Payment required event published: {self.reference}")
        return True
