# Odoo 19+ 生态集成项目 - 上下文简报

## 项目状态
**日期**：$(date +%Y-%m-%d)
**阶段**：第一阶段 - 项目初始化与基础框架搭建
**当前目标**：完成项目骨架搭建，明确模块边界，并实现`integration_hub`事件总线原型。

## 核心聚焦任务
1.  定义并实现`integration_hub`中的基础事件（如`sale.order.confirmed`, `payment.required`）。
2.  完成`domain_payment`中`PaymentTransaction`核心模型与状态机的草稿设计。
3.  制定首个支付适配器(`adapter_payment_wechat`)与领域层的接口契约。

## 最近关键决策 (ADR)
1.  **ADR-001：采用“集成总线+适配器”架构**：所有集成通过事件驱动，禁止直接修改Odoo核心模块。
2.  **ADR-002：支付领域统一模型**：所有支付渠道必须映射到`domain_payment`的统一状态机。

## 本次会话目标
[在此填写本次与AI讨论的具体目标，例如：评审`payment.required`事件的数据负载设计。]
