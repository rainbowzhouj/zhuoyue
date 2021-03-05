## 代码目录及介绍
文件 | 备注
---|---
test_group_buy_event.py | 营销中台拼课团的增删改查代码
test_event.py | 营销中台活动的增删改查代码
test_pkt.py | 初始拼课团代码


## 状态说明
### 支付状态说明

- 无需支付 NONE
- 待支付 UNPAID
- 支付处理中 PAY_PROCESSING
- 支付成功 PAY_SUCCESS
- 支付失败 PAY_FAILED
- 退款中 REFUNDING
- 已退款 REFUNDED
- 退款失败 REFUND_FAILED


### 拼课团状态说明

- 未开启 NOTOPEN
- 开启 OPEN
- 已结束 CLOSED





## 数据库表介绍
### article 物品，条款表

字段名 |类型 | 备注
:--- | :---| :---
id |bigint |
organization_id | bigint|
enable |tinyint| 是否开启
resource_id | varchar |
title |varchar|
order_no |int|
recommend |tinyint| 置顶
tag | varchar|
image_url |varchar|
brief |varchar|
url |varchar| 
url_type |bigint| URL类型：1=活动，2=拼课团，3=自定义
deleted |tinyint| 删除标记
created_time | datetime |创建时间
updated_time | datetime |更新时间

### category_resource 商品分类表

字段名 |类型 | 备注
:--- | :---| :---
id |bigint |
category_id | bigint|商品id
from_member_id |bigint| 上线成员id
updated_time | datetime |更新时间

### channel 渠道表

字段名 |类型 | 备注
:--- | :---| :---
id |bigint |
name | varchar|名称
organization_id | bigint|组织id
descr | varchar|描述
from_member_id |bigint| 上线成员id
created_time | datetime |创建时间
updated_time | datetime |更新时间
deleted |tinyint| 删除标记

### coupons_record 优惠券记录表

字段名 |类型 | 备注
:--- | :---| :---
id |int |
coupons_code|varchar|优惠券code
coupons_json | varchar|返回详细信息
created_time | datetime |创建时间
updated_time | datetime |更新时间

### dab_privilege 权限表

字段名 |类型 | 备注
:--- | :---| :---
id |bigint |
name | varchar|权限名称
level | varchar|权限等级
parent_id|bigint|父节点
code | varchar|权限编辑
deleted |tinyint| 删除标记
created_time | datetime |创建时间
updated_time | datetime |更新时间

### dab_privilege_role_map 权限规则表

字段名 |类型 | 备注
:--- | :---| :---
role_id |bigint |
privilege_int| bigint|


### dab_role 规则表
字段名 |类型 | 备注
:--- | :---| :---
id |bigint |
name | varchar|角色名称
organization_id | bigint|组织id
descr | varchar|描述
deleted |tinyint| 删除标记
created_time | datetime |创建时间
updated_time | datetime |更新时间

### dab_tenant_role_map 租户规则表
字段名 |类型 | 备注
:--- | :---| :---
tenant_id |bigint | 租户id
role_id |  bigint|角色id

### dab_tenant_upmember_record 更新成员记录表
字段名 |类型 | 备注
:--- | :---| :---
id |bigint |
tenant_id |bigint | 租户id
member_id |  bigint|成员id
from_point|int|
to_pint|int|
from_growth|int|
to_growth|int|
created_time|datetime|

### discount_coupon_code 优惠券码表
字段名 |类型 | 备注
:--- | :---| :---
id |bigint |
code | varchar|优惠券码
discount_coupon_id | bigint|优惠券id
discount_amount | bigint|优惠金额
discount_coupon_send_rule_id |bigint| 优惠券投放id
member_id|bigint|会员id
effect_end_time|datetime|有效期结束时间
give_member_time|datetime|发送到会员时间
effect_start_time|datetime|有效期开始时间
used_time|datetime|
order_id|bigint|订单id
dicount_coupon_name|varchar|优惠券名称
order_type|varchar|订单类型
status|varchar|状态 UNSEND UNOPEN UNUSED USED TIME_OUT
deleted |tinyint| 删除标记
created_time | datetime |创建时间
updated_time | datetime |更新时间

### discount_coupon_code 优惠券发送规则表
字段名 |类型 | 备注
:--- | :---| :---
id |bigint |
discount_coupon_id | bigint|优惠券id
resource_id | varchar|资源id
count | int|投放量
send_type|varchar|OPEN_GET 公开投放 CLOSE_GIVE 定向投放
get_type|varchar|NO_MAX_GET 不限量领取 MAX_GET 限量领取
give_count|int|每个用户发放张数
deleted |tinyint| 删除标记
created_time | datetime |创建时间
updated_time | datetime |更新时间

### event 活动表
字段名 |类型 | 备注
:--- | :---| :---
id |bigint |
guide_image | bigint|引导图片
event_category_second_id|bigint|
event_category_first_id|bigint|
organization_id|bigint|归属组织
resource_id|varchar|资源id
end_time|datetime|结束时间
begin_time|datetime|开始时间
order_no|int|
name|varchar|活动名称
brief|varchar|活动简介
recommend|tinyint|置顶
banner||varchar|头图
sms_template_id|varchar|模板消息id
coupon_batch|varchar|优惠券批次
cover_image|varchar|封面图
detail|mediumtext|活动详情
published|tinyint|是否发布
form_id|bigint|表单id
charged_amount|int|
reservation|review_toggle|tinyint|预约审核开关
cancel_review_toggle|tinyint|取消审核开关
charge_toggle|tinyint|收费开关
checkin_qrcode_toggle|tinyint|核销码开关
created_time | datetime |创建时间
updated_time | datetime |更新时间
deleted |tinyint| 删除标记

### event_category 活动描述表
字段名 |类型 | 备注
:--- | :---| :---
id |bigint |
descr | varchar|描述
parent_id | bigint|父类id
name|varchar|姓名
type | varchar|FIRST SECOND
created_time | datetime |创建时间
updated_time | datetime |更新时间
deleted |tinyint| 删除标记

### event_checkin_qrcode 
字段名 |类型 | 备注
:--- | :---| :---
id |bigint |
event_id | bigint|
store_org_id | bigint|
qrcode_url|varchar|
deleted |tinyint| 删除标记


### event_order 活动排名表
字段名 |类型 | 备注
:--- | :---| :---
id |bigint |
member_id |bigint |会员id
event_id | bigint|活动id
checkin_store_org_id|bigint|
event_tile|varchar|活动标题
name|varchar|活动名称
mobile|varchar|手机号码
form_data_ids|varchar|附加表单数据
channel|varchar|渠道
code|varchar|核销码
pament_status|varchar|
status|varchar|订单状态
payment_order_id|bigint |支付订单ID
session_id|bigint |
session_store_id|bigint |选择的店铺
refund_order_id|bigint |退款订单ID
session_start_time|datetime |场次开始时间
session_end_time|datetime |场次结束时间
session_address|varchar |场次场地
charged_mount|int|
time_expire|datetime |超时时间
created_time | datetime |创建时间
updated_time | datetime |更新时间
deleted |tinyint| 删除标记


### event_session 活动场次表
字段名 |类型 | 备注
:--- | :---| :---
id |bigint |
member_id |bigint |会员id
event_id | bigint|活动id
start_time|datetime |开始时间
end_time|datetime |结束时间
applicable_store_ids|varchar|
place_type|varchar|STORE 为酒店ID集合 其他为默认字符串
quota|int|限额
latitude|varchar|维度
longitude|varchar|精度
address|varchar|地址
created_time | datetime |创建时间
updated_time | datetime |更新时间
deleted |tinyint| 删除标记


### family_members 家庭成员表
字段名 |类型 | 备注
:--- | :---| :---
id |bigint |
member_id |bigint |会员id
third_code|varchar|第三方  PRI系统代码，卓越：ZYEDU_TMS
build_type|varchar|绑定类型 PARENTID MOBILE
third_member_id|varchar|第三方会员ID
relation|varchar|学生：CHILDREN , 枚举类：FamilyRelationEnum
name|varchar|姓名
sex|tinyint|性别 0:女 1:男
brithday|date|生日
mobile|varchar|手机
school_name|varchar|生源学校名
grade_name|varchar|年级名
created_time | datetime |创建时间
deleted |tinyint| 删除标记

### feeder_school 直属学校表
字段名 |类型 | 备注
:--- | :---| :---
id |bigint |
third_id |bigint |
name|varchar|学校名
province|varchar|省份
city|varchar|城市
address|varchar|地址
status|tinyint|
third_modify_id|bigint|
third_modify_name|varchar|
created_time | datetime |创建时间
updated_time | datetime |更新时间
deleted |tinyint| 删除标记

### fission_poster 裂变海报表
字段名 |类型 | 备注
:--- | :---| :---
id |bigint |
title |varchar|标题
type |varchar|类型
organization_id |bigint |组织id
resource_id |varchar |资源id
background_url|varchar|背景图片
enabled|tinyint|是否开启
created_time | datetime |创建时间
updated_time | datetime |更新时间
deleted |tinyint| 删除标记

### flyway_schema_history 表
字段名 |类型 | 备注
:--- | :---| :---
installed_rank |bigint |
version |varchar|
description|varchar|描述
type |varchar|类型
script|varchar|
checksum|int|
installed_by|varchar |
installed_on|timestamp|
execution_time|int|
success|tinyint|


### form 表
字段名 |类型 | 备注
:--- | :---| :---
id |bigint |主键
fields |varchar|字段
created_time | datetime |创建时间
updated_time | datetime |更新时间
deleted |tinyint| 删除标记

### form_data 表单数据
字段名 |类型 | 备注
:--- | :---| :---
id |bigint |主键
type|varchar|字段类型，文本：text、单选：radio、图片：image
event_order_id|bigint|
key|varchar|字段名称
value|varchar|字段内容
created_time | datetime |创建时间
updated_time | datetime |更新时间
deleted |tinyint| 删除标记

### form_data 表单数据
字段名 |类型 | 备注
:--- | :---| :---
id |bigint |主键
type|varchar|字段类型，文本：text、单选：radio、图片：image
event_order_id|bigint|
key|varchar|字段名称
value|varchar|字段内容
created_time | datetime |创建时间
updated_time | datetime |更新时间
deleted |tinyint| 删除标记

### goods 商品表
字段名 |类型 | 备注
:--- | :---| :---
id |bigint |主键
name|varchar|名称
price|int|价格
effective_type|varchar|有效期类型
type|varchar|字段类型，文本：text、单选：radio、图片：image
effective_day|int|有效天数
organization_id|bigint |
source_type|varchar|来源
use_type|varchar|核销状态
resource_id|varchar|资源id
enable|tinyint|是否开启
order_no|int|序列化
begin_time|datetime|开始时间
end_time|datetime|结束时间
banner||varchar|头图
cover_image|varchar|封面图
point|int|积分
descr|text|描述
organization_id|bigint|归属组织
created_time | datetime |创建时间
updated_time | datetime |更新时间
deleted |tinyint| 删除标记


### goods_code 商品状态码表
字段名 |类型 | 备注
:--- | :---| :---
id |bigint |主键
goods_ids|bigint|
selled|tinyint|是否已经被兑换
code|varchar|
created_time | datetime |创建时间
deleted |tinyint| 删除标记


### goods_order 商品序列表
字段名 |类型 | 备注
:--- | :---| :---
id |bigint |主键
member_name|varchar|成员名称
goods_name|varchar|商品名称
goods_ids|varchar|商品id
use_type|varchar|核销状态
price|int|价格
goods_type|varchar|
count|int|
last_time|datetime|
mobile|varchar|手机
goods_code|varchar|
point|int|积分
status|varchar|
organization_id|bigint |
member_id|bigint |成员id
created_time | datetime |创建时间
updated_time | datetime |更新时间
deleted |tinyint| 删除标记

### group_buy_event 拼课团表
字段名 |类型 | 备注
:--- | :---| :---
id |bigint |主键
event_category_second_id|varchar|名称
event_category_first_id|int|价格
resource_id|varchar|资源id
descr|varchar|简介
titile|varchar|
organization_id|bigint |
begin_time|datetime|开始时间
team_last_time_hours|int|拼团最长小时数 LIMITED 时有效
remind_hours|int|提醒的小时数 开始后多少小时 或者结束前多少小时
remind_time_type|varchar|提醒时间的类型 BEGIN 开始 END 结束
team_last_time_type|varchar|团队拼团时长 LIMITLESS 一直 LIMITED 有限的
form_id|bigint|表单模板id
end_time|datetime|结束时间
repeat_join|tinyint|
effective_type|varchar|优惠券有效期类型
effective_end_time|datetime|结束时间
status|varchar|
effective_begin_time|datetime|开始时间
student_can_join|tinyint|在读学生 是否可以参加
effective_hours|int|有效期天数
banner||varchar|头图
cover_image|varchar|封面图
cancel_review_toggle|tinyint|取消审核开关
detail|varchar|详情
enable|tinyint|是否开启
guide_image | bigint|引导图片
order_no|int|序列化
recommend |tinyint| 置顶
price|int|价格
checkin_qrcode_toggle|tinyint|核销码开关
created_time | datetime |创建时间
updated_time | datetime |更新时间
deleted |tinyint| 删除标记

### group_buy_event_order 拼课团订单表
字段名 |类型 | 备注
:--- | :---| :---
id |bigint |主键
group_buy_event_id|bigint|团购活动id
group_buy_event_name|varchar|拼客团名称
group_buy_event_team_id|bigint|团id
member_id|bigint|会员id
size|int|团队数量
member_head_url|varchar|会员头像地址
time_expire|datetime|过期时间
member_name|varchar|会员名称
channel|varchar|来源渠道
form_data_ids|varchar|表单数据id集合
checkin_store_org_id|bigint(20)|核销店铺id
status|varchar|状态
pament_status|varchar|支付状态
code|varchar|核销码
member_mobile|varchar|会员手机号
payment_order_id|bigint|支付订单id
refund_order_id|bigint|退款订单id
sku_values|varchar|规格值 简易
sku_values_detail|varchar|规格值详情
charged_amount|int|金额
robot|tinyint|是不是机器人订单
team_leader|tinyint|是不是团长订单
created_time|datetime|创建时间
updated_time|datetime|更新时间



### group_buy_event_robot 拼课团机器人表

### group_buy_event_robot_record 拼课团机器人记录表


### group_buy_event_rule 拼课团规则表


### group_buy_event_specification_conf 拼课团  表

### group_buy_event_specification_detail 拼课团  表

### group_buy_event_specification_detail_parent 拼课团  表


### group_buy_event_team 拼课团团队表

### level_descr 等级描述表

### level_privilege 等级  表


### mall_category  表

### mall_goods  表

### mall_goods_category  表

### mall_goods_category_level  表

### mall_goods_collection  表

### mall_goods_sku  表

### mall_goods_sku_relation  表

### mall_goods_ticket  表

### mall_group_buy_event  表

### mall_item_attr_key   表

### mall_item_attr_val   表

### mall_item_sku   表

### mall_order   表

### mall_order_goods   表

### mall_order_log   表

### mall_order_member_ticket   表

### mall_order_operation_record   表

### mall_template   表

### mall_template_attr   表

### mall_ticket_coupon   表

### mall_ticket_coupon_code   表

### mall_ticket_discount_coupon   表

### marketing_tool_third_order_map   表

### marketing_training_class_map   表

### member 会员信息表 
| 字段名                         | 类型             | 备注                  |
|-----------------------------|----------------|---------------------|
| id                          | bigint\(20\)   |                     |
| organization\_id            | bigint\(20\)   | 组织id                |
| name                        | varchar\(45\)  | 姓名                  |
| save\_info\_time            | datetime       | 流资时间                |
| last\_login\_time           | datetime       | 最后登录时间              |
| student                     | tinyint\(1\)   | 是否是学生               |
| channel                     | varchar\(255\) | 渠道                  |
| sex                         | varchar\(45\)  | 性别                  |
| birthday                    | varchar\(50\)  | 生日                  |
| mobile                      | varchar\(45\)  | 手机号                 |
| email                       | varchar\(45\)  | 邮箱                  |
| points                      | int\(11\)      | 积分                  |
| nick\_name                  | varchar\(255\) | 昵称                  |
| sign\_days                  | int\(11\)      | 当前签到天数              |
| sign\_total\_days           | int\(11\)      | 总共签到天数              |
| sign\_max\_days             | int\(11\)      | 最长签到天数              |
| share\_count                | int\(11\)      | 分享次数                |
| child\_member\_save\_count  | int\(11\)      | 带来用户留资数             |
| child\_member\_uv\_count    | int\(11\)      | 带来新用户数              |
| child\_member\_total\_count | int\(11\)      | 带来用户数               |
| open\_count                 | int\(11\)      | 打开次数                |
| growth                      | int\(11\)      | 增长率                 |
| zy\_member\_info            | varchar\(255\) | 卓越会员ID              |
| worker                      | tinyint\(1\)   | 员工标识0非员工 1员工        |
| source                      | varchar\(255\) | SELF 自身 THIRD 其他第三方 |
| level                       | int\(11\)      | 级别                  |
| deleted                     | tinyint\(1\)   | 删除标记                |
| created\_time               | datetime       | 创建时间                |
| updated\_time               | datetime       | 更新时间                |


### member_benefits 会员  表

### member_child_info 推荐人和下线的关系表
| 字段名                              | 类型              | 备注                          |
|----------------------------------|-----------------|-----------------------------|
| id                               | bigint\(20\)    |                             |
| child\_member\_id                | bigint\(20\)    | 下线ID                        |
| member\_id                       | bigint\(20\)    | 推荐人ID                       |
| resource\_id                     | varchar\(255\)  | 资源ID                        |
| root\_member\_id                 | bigint\(20\)    | 根推荐人ID                      |
| from\_member\_ids                | varchar\(1000\) | 推荐人链路 在前面添加 A\->B,A\->C,B,A |
| child\_member\_share\_count      | int\(11\)       | 下线分享次数                      |
| child\_member\_open\_count       | int\(11\)       | 下线打开次数                      |
| child\_member\_count             | int\(11\)       | 带来下线数                       |
| child\_member\_save\_info\_count | int\(11\)       | 留资人数                        |
| created\_time                    | datetime        | 创建时间                        |
| updated\_time                    | datetime        | 更新时间                        |


### member_class_buy_info 会员  表

### member_event_record 会员下线表

### member_growth_log 会员下线表

### member_level 会员下线表

### member_if_record    表

### member_log 会员  表

### member_organization 会员  表


### member_organization_map 会员  表

### member_point_record 会员  表

### member_resource_info

### member_static_tag_group_map 会员  表


### member_task 会员任务表


### member_third_info 会员  表

### notice 表

### organization 表

### organization_config 表

### organization_wx_app 表

### pay_notify_log 表

### payment_order 表

### poster 表

### promotion_info_report 表

### refund_order 表

### resource_channel 表

### resource_conf 表

### resource_member_order_info 表

### resource_organization_map 表

### resource_share_info 表

### resource_static_tag_group_map 表

### resource_share_info 表

### resource_static_tag_group_map 表

### resource_use_info 表

### share_tracking 表
| 字段名               | 类型              | 备注                   |
|-------------------|-----------------|----------------------|
| id                | bigint\(20\)    |                      |
| organization\_id  | bigint\(20\)    | 组织id                 |
| member\_id        | bigint\(20\)    | 会员ID                 |
| resource\_type    | varchar\(255\)  | 资源类型                 |
| resource\_id      | varchar\(255\)  | 资源id                 |
| type              | varchar\(255\)  | 传播类型：SHARE分享、触达REACH |
| store\_org\_id    | bigint\(20\)    | 门店组织ID               |
| channel           | varchar\(255\)  | 渠道                   |
| from\_member\_ids | varchar\(255\)  | 分享的会员ID集合            |
| depth             | int\(11\)       | 深度                   |
| browse\_time      | datetime        | 首次浏览时间               |
| from\_ids         | varchar\(5000\) | 父节点集合                |
| from\_id          | bigint\(20\)    | 上一个资源链接              |
| root\_id          | bigint\(20\)    | 这个链路开始id             |
| qrcode\_url       | varchar\(255\)  | 拼接的图片的url            |
| created\_time     | datetime        | 创建时间                 |
| updated\_time     | datetime        | 更新时间                 |


### static_tag_group 表

### store 表

### superuser_plan 表

### superuser_plan_stage 表

### superuser_plan_stage_ranking 表

### superuser_point_record 表


### task 表

### task_center 表

### taskcenter_in_event 表

### tenant 表

### tenant_organization_map 表

### timed_task_info 表

### training_class 表

### worker 表
| 字段名            | 类型             | 备注    |
|----------------|----------------|-------|
| id             | bigint\(20\)   |       |
| name           | varchar\(255\) | 姓名    |
| member\_id     | bigint\(20\)   | 会员id  |
| department     | varchar\(255\) | 部门    |
| position       | varchar\(255\) | 职位    |
| wechat\_qrcode | varchar\(255\) | 微信二维码 |
| head\_image    | varchar\(255\) | 头像    |
| wechat\_num    | varchar\(255\) | 微信号   |
| mobile         | varchar\(255\) | 手机号   |
| worker\_no     | varchar\(255\) | 工号    |
| on\_work       | tinyint\(1\)   | 是否在职  |
| created\_time  | datetime       | 创建时间  |
| deleted        | tinyint\(1\)   | 删除标记  |
| updated\_time  | datetime       | 更新时间  |



### wx_miniapp_account 表


### wx_miniapp_formid_record 表

### wx_mp_account 表

### wx_pay_config 表












### event_order 活动订单表
|                           字段名 | 类型              | 备注     |
|-------------------------------|-----------------|--------|
| id                            | bigint\(20\)    |        |
| guide\_image                  | varchar\(255\)  | 引导图片   |
| event\_category\_second\_id   | bigint\(20\)    | 活动二级分类 |
| event\_category\_first\_id    | bigint\(20\)    | 活动一级分类 |
| organization\_id              | bigint\(20\)    | 归属组织   |
| resource\_id                  | varchar\(30\)   | 资源ID   |
| end\_time                     | datetime        | 结束时间   |
| begin\_time                   | datetime        | 开始时间   |
| order\_no                     | int\(10\)       | 订单排序   |
| name                          | varchar\(100\)  | 活动名称   |
| brief                         | varchar\(100\)  | 活动简介   |
| recommend                     | tinyint\(1\)    | 置顶     |
| banner                        | varchar\(200\)  | 头图     |
| sms\_template\_id             | varchar\(200\)  | 模板消息id |
| coupon\_batch                 | varchar\(1000\) | 优惠券批次  |
| cover\_image                  | varchar\(200\)  | 封面图    |
| detail                        | mediumtext      | 活动详情   |
| published                     | tinyint\(1\)    | 是否发布   |
| form\_id                      | bigint\(20\)    | 表单iD   |
| charged\_amount               | int\(11\)       | 收费金额   |
| reservation\_review\_toggle   | tinyint\(1\)    | 预约审核开关 |
| cancel\_review\_toggle        | tinyint\(1\)    | 取消审核开关 |
| charge\_toggle                | tinyint\(1\)    | 收费开关   |
| checkin\_qrcode\_toggle       | tinyint\(1\)    | 核销码开关  |
| created\_time                 | datetime        | 创建时间   |
| updated\_time                 | datetime        | 更新时间   |
| deleted                       | tinyint\(1\)    | 是否删除   |





test_group_buy_event.py | 营销中台拼课团的增删改查代码|
wx_pay_config