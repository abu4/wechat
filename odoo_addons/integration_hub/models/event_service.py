# -*- coding: utf-8 -*-

from odoo import models, api
import json
import logging

_logger = logging.getLogger(__name__)

class IntegrationEventService(models.Model):
    _name = 'integration_hub.event_service'
    _description = 'Central service for publishing and routing integration events'

    @api.model
    def publish_payment_required(self, event_data):
        """
        公开发布 'payment.required' 事件。
        这是系统其他模块（如销售订单）调用的统一入口。
        """
        _logger.info(f"Publishing payment.required event: {event_data.get('reference')}")

        # 1. 验证事件数据基本结构（此处应更严谨）
        required_fields = ['reference', 'amount', 'currency_id', 'partner_id', 'callback_url']
        for field in required_fields:
            if field not in event_data:
                raise ValueError(f"Missing required field in event data: {field}")

        # 2. 封装标准事件格式
        standardized_event = {
            'event_type': 'payment.required',
            'timestamp': fields.Datetime.now(),
            'payload': event_data,
            'event_id': self.env['ir.sequence'].next_by_code('integration.event.sequence') or f"evt_{int(time.time())}"
        }

        # 3. 关键：触发Odoo内部事件系统，供其他模块订阅
        # 使用 bus.bus 进行实时通知（适用于Web客户端）
        self.env['bus.bus']._sendone(
            'integration_hub',
            'payment.required',
            standardized_event
        )

        # 4. 同时，也放入队列作业，供后端处理器消费（更可靠）
        self.env['queue.job'].create_job(
            self._process_event_subscribers,
            args=(standardized_event,),
            description=f"Process payment.required for {event_data['reference']}"
        )

        _logger.info(f"Event {standardized_event['event_id']} published and queued.")
        return standardized_event['event_id']

    def _process_event_subscribers(self, event):
        """
        内部方法：处理事件订阅者。
        此方法由队列作业异步执行，查找并通知所有订阅了此事件类型的适配器。
        """
        # 这里简化实现：实际应查找所有注册的适配器
        _logger.info(f"Processing subscribers for event {event['event_id']}")
        # 后续将实现适配器的动态发现和调用
        pass
