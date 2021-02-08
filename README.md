## 代码目录及介绍
文件 | 注释
---|---
test_group_buy_event.py | 营销中台拼课团的增删改查代码
test_event.py | 营销中台活动的增删改查代码
test_pkt.py | 初始拼课团代码


## 数据库表介绍
### article 物品，条款表

字段名 |类型 | 注释
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

字段名 |类型 | 注释
:--- | :---| :---
id |bigint |
category_id | bigint|商品id
from_member_id |bigint| 上线成员id
updated_time | datetime |更新时间

### channel 渠道表

字段名 |类型 | 注释
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

字段名 |类型 | 注释
:--- | :---| :---
id |int |
coupons_code|varchar|优惠券code
coupons_json | varchar|返回详细信息
created_time | datetime |创建时间
updated_time | datetime |更新时间

### dab_privilege 权限表

字段名 |类型 | 注释
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

字段名 |类型 | 注释
:--- | :---| :---
role_id |bigint |
privilege_int| bigint|


### dab_role 规则表
字段名 |类型 | 注释
:--- | :---| :---
id |bigint |
name | varchar|角色名称
organization_id | bigint|组织id
descr | varchar|描述
deleted |tinyint| 删除标记
created_time | datetime |创建时间
updated_time | datetime |更新时间

### dab_tenant_role_map 租户规则表
字段名 |类型 | 注释
:--- | :---| :---
tenant_id |bigint | 租户id
role_id |  bigint|角色id

### dab_tenant_upmember_record 更新成员记录表
字段名 |类型 | 注释
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
字段名 |类型 | 注释
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
字段名 |类型 | 注释
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
字段名 |类型 | 注释
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
字段名 |类型 | 注释
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
字段名 |类型 | 注释
:--- | :---| :---
id |bigint |
event_id | bigint|
store_org_id | bigint|
qrcode_url|varchar|
deleted |tinyint| 删除标记


### event_order 活动排名表
字段名 |类型 | 注释
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
字段名 |类型 | 注释
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
字段名 |类型 | 注释
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
字段名 |类型 | 注释
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
字段名 |类型 | 注释
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

### flyway_schema_history 裂变海报表
字段名 |类型 | 注释
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



test_group_buy_event.py | 营销中台拼课团的增删改查代码|
wx_pay_config