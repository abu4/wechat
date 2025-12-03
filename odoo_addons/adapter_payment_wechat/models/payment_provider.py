# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class WeChatPaymentProvider(models.Model):
    _name = 'wechat.payment.provider'
    _description = 'WeChat Pay Payment Provider Adapter'
    _inherit = ['payment.provider']  # 继承Odoo标准支付提供商基类

    # 微信支付特定配置字段
    wechat_merchant_id = fields.Char(string='Merchant ID', required_if_provider='wechat', groups='base.group_user')
    wechat_api_v3_key = fields.Char(string='API v3 Key', groups='base.group_system')
    wechat_certificate = fields.Binary(string='API Certificate', help='微信支付API证书')
    wechat_certificate_filename = fields.Char(string='Certificate Filename')

    # 标记支持的支付方式
    supported_payment_methods = fields.Selection(
        selection_add=[('wechat_native', 'WeChat Native QR Code'),
                       ('wechat_jsapi', 'WeChat JSAPI'),
                       ('wechat_miniprogram', 'WeChat Mini Program')],
        ondelete={'wechat_native': 'set null'}
    )

    @api.model
    def _get_supported_currencies(self):
        """返回微信支付支持的货币列表"""
        return ['CNY', 'USD']  # 简化示例

    def _handle_payment_required_event(self, event_payload):
        """
        适配器入口：处理 payment.required 事件。
        此方法将被 integration_hub 调用。
        """
        _logger.info(f"WeChat Pay adapter processing event: {event_payload.get('reference')}")

        # 这里将实现：
        # 1. 调用微信统一下单API
        # 2. 生成支付参数（如二维码链接、JSAPI参数）
        # 3. 返回结果给调用方
        result = {
            'adapter': 'wechat',
            'action': 'redirect',
            'data': {
                'qrcode_url': 'https://api.mch.weixin.qq.com/v3/pay/transactions/native',
                'prepay_id': '模拟的预支付ID',
                'reference': event_payload.get('reference')
            }
        }
        return result
