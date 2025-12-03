# -*- coding: utf-8 -*-

from odoo import models, api, fields
import logging

_logger = logging.getLogger(__name__)

class PaymentEventHandlers(models.Model):
    _name = 'domain_payment.event_handlers'
    _description = 'Handlers for integration events related to payment'

    @api.model
    def handle_payment_required_event(self, event_payload):
        """
        订阅并处理 'payment.required' 事件的核心方法。
        此方法应由 integration_hub 的事件路由器调用。
        """
        _logger.info(f"Payment domain handling payment.required event for {event_payload.get('reference')}")

        # 1. 调用领域服务，创建统一的支付交易记录
        transaction = self.env['domain_payment.transaction'].create_from_event(event_payload)

        # 2. 记录日志
        _logger.info(f"Payment transaction {transaction.reference} created with ID {transaction.id}, state: {transaction.state}")

        # 3. 这里可以触发后续业务逻辑，例如更新订单状态、发送确认邮件等
        # 例如：transaction.source_document.write({'payment_state': 'pending'})

        return {
            'status': 'success',
            'transaction_id': transaction.id,
            'reference': transaction.reference,
            'state': transaction.state
        }
