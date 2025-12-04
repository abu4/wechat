"""
鏂囨。鏅朵綋鎬荤储寮?(Crystal Index)
姝ゆ枃浠跺垪鍑轰簡鎵€鏈夊彲鐢ㄧ殑鏂囨。璁板繂鏅朵綋鍙婂叾鍏冩暟鎹€?
"""

import json

CRYSTAL_INDEX = {
    "source_document": "odoo.txt",
    "total_crystals": 20,
    "total_original_size_kb": 957.71,
    "total_encoded_size_kb": 327.65,
    "crystals": [
    {
        "encoded_size_kb":  20.93,
        "filename":  "doc_crystal_001.py",
        "preview":  "# 基于Odoo 19的微信支付与生态系统集成项目开发计划  ## 项目概述  本项目旨在为Odoo 19开发一套完整的支付与微信生态系统集成解决方案，包括微信支付、支付宝支付、云闪付支付、微信公众号",
        "original_size_kb":  45.43,
        "id":  1
    },
    {
        "encoded_size_kb":  17.89,
        "filename":  "doc_crystal_002.py",
        "preview":  "        # 发送请求         response = requests.post(url, json=data, headers=headers)                  if",
        "original_size_kb":  44.6,
        "id":  2
    },
    {
        "encoded_size_kb":  16.46,
        "filename":  "doc_crystal_003.py",
        "preview":  "    0% { transform: rotate(0deg); }     100% { transform: rotate(360deg); } }  .success-icon {     d",
        "original_size_kb":  47.33,
        "id":  3
    },
    {
        "encoded_size_kb":  19.44,
        "filename":  "doc_crystal_004.py",
        "preview":  "        # 创建支付方法         self.wechat_method = self.env[\u0027pos.payment.method\u0027].create({             \u0027n",
        "original_size_kb":  52.44,
        "id":  4
    },
    {
        "encoded_size_kb":  16.95,
        "filename":  "doc_crystal_005.py",
        "preview":  "#### **任务2：配置界面模板** ```xml \u003c!-- file: wechat_common/views/wechat_config_templates.xml --\u003e  \u003codoo\u003e   ",
        "original_size_kb":  56.86,
        "id":  5
    },
    {
        "encoded_size_kb":  17.3,
        "filename":  "doc_crystal_006.py",
        "preview":  "        # 检查requirements.txt         requirements_file = self.project_path / \u0027requirements.txt\u0027     ",
        "original_size_kb":  49.11,
        "id":  6
    },
    {
        "encoded_size_kb":  13.86,
        "filename":  "doc_crystal_007.py",
        "preview":  "#### **任务2：消息管理界面** ```xml \u003c!-- file: wechat_platform/static/src/xml/wechat_message.xml --\u003e  \u003ctempla",
        "original_size_kb":  49.7,
        "id":  7
    },
    {
        "encoded_size_kb":  18.47,
        "filename":  "doc_crystal_008.py",
        "preview":  "        # 消息类型分布         type_stats = {}         for msg in messages:             msg_type = msg.msg",
        "original_size_kb":  49.53,
        "id":  8
    },
    {
        "encoded_size_kb":  16.01,
        "filename":  "doc_crystal_009.py",
        "preview":  "#### **任务1：完善自动回复规则模型** ```python # file: wechat_platform/models/wechat_auto_reply.py  from odoo imp",
        "original_size_kb":  55.45,
        "id":  9
    },
    {
        "encoded_size_kb":  15.95,
        "filename":  "doc_crystal_010.py",
        "preview":  "#### **任务2：素材管理界面** ```xml \u003c!-- file: wechat_platform/views/wechat_material_views.xml --\u003e  \u003codoo\u003e   ",
        "original_size_kb":  53.19,
        "id":  10
    },
    {
        "encoded_size_kb":  17.03,
        "filename":  "doc_crystal_011.py",
        "preview":  "        # 4. 基于内容的简单检测         if not result[\u0027mime_type\u0027]:             if file_data.startswith(b\u0027\\xF",
        "original_size_kb":  48.08,
        "id":  11
    },
    {
        "encoded_size_kb":  13.39,
        "filename":  "doc_crystal_012.py",
        "preview":  "        # 热门菜单项         menu_stats = self.env[\u0027wechat.menu.stat\u0027].read_group([             (\u0027account",
        "original_size_kb":  51.8,
        "id":  12
    },
    {
        "encoded_size_kb":  14.92,
        "filename":  "doc_crystal_013.py",
        "preview":  "#### **任务1：数据可视化仪表盘界面** ```xml \u003c!-- file: wechat_platform/static/src/xml/wechat_dashboard.xml --\u003e  \u003c",
        "original_size_kb":  61.27,
        "id":  13
    },
    {
        "encoded_size_kb":  16.65,
        "filename":  "doc_crystal_014.py",
        "preview":  "            # 记录发送日志             self.env[\u0027wechat.template.send.log\u0027].create({                 \u0027temp",
        "original_size_kb":  51.86,
        "id":  14
    },
    {
        "encoded_size_kb":  16.87,
        "filename":  "doc_crystal_015.py",
        "preview":  "### 3.5 POS微信支付配置表 (`pos_payment_wechat_config`)  **表说明**: 存储POS端微信支付配置  | 字段名 | 类型 | 长度 | 可空 | 默认值 ",
        "original_size_kb":  32.52,
        "id":  15
    },
    {
        "encoded_size_kb":  13.88,
        "filename":  "doc_crystal_016.py",
        "preview":  "6. 日志记录  ### 10.2 运维人员培训 1. 安全配置管理 2. 漏洞管理 3. 应急响应 4. 备份恢复  ## 11. 附录  ### 11.1 安全工具清单 | 工具 | 用途 | 链",
        "original_size_kb":  29.35,
        "id":  16
    },
    {
        "encoded_size_kb":  15.43,
        "filename":  "doc_crystal_017.py",
        "preview":  "#### 7.3.2 店铺日报 - 总营业额 - 各支付方式占比 - 客单价分析 - 畅销商品排行 - 会员销售占比  ## 8. 系统维护  ### 8.1 日常检查  #### 8.1.1 上班前",
        "original_size_kb":  32.37,
        "id":  17
    },
    {
        "encoded_size_kb":  13.43,
        "filename":  "doc_crystal_018.py",
        "preview":  "                # 计算MD5和SHA256                 with open(file_path, \u0027rb\u0027) as f:                     ",
        "original_size_kb":  40.32,
        "id":  18
    },
    {
        "encoded_size_kb":  17.84,
        "filename":  "doc_crystal_019.py",
        "preview":  "#!/usr/bin/env python3 \u0027\u0027\u0027 常见问题解答生成器 自动生成项目的常见问题解答文档 \u0027\u0027\u0027  import json from datetime import datetime ",
        "original_size_kb":  57.96,
        "id":  19
    },
    {
        "encoded_size_kb":  14.95,
        "filename":  "doc_crystal_020.py",
        "preview":  "            \u0027completion_criteria\u0027: [                 \u0027所有基础配置完成\u0027,                 \u0027支付渠道配置完成并测试\u0027,     ",
        "original_size_kb":  48.54,
        "id":  20
    }
]
}

def list_all_crystals():
    print("Document Crystal List:")
    for c in CRYSTAL_INDEX["crystals"]:
        print(f"  [{c['id']:03d}] {c['encoded_size_kb']:6.1f}KB | {c['preview'][:50]}...")

if __name__ == "__main__":
    list_all_crystals()