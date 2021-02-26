import pytest
import json
import requests

"""
1、登录营销中台
2、选择营销工坊->拼课团
3、创建拼课团
4、更新拼课团
5、查找拼课团
6、断言验证 hamcrest/assert
"""

# def setup():
#     pass

"""

"""

def test_login():
    # 登录
    url = "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/tenants/login"
    payload = "{\"username\":\"zhuoyue\",\"password\":\"123456\"}"
    headers = {
        'Content-Type': 'application/json;charset=UTF-8'
    }
    r = requests.post(url, headers=headers, data=payload, verify=False)
    print(r.text)
    print(json.dumps(r.json(), indent=2))

    assert r.status_code == 200
    assert r.json()['code'] == '0'
    token = r.json()['data']['token']
    return token


def test_find_group_buy_event():
    # 搜索框按钮，搜索显示拼课团列表
    url = "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event/list"
    payload = {
        "page": 1,
        "limit": 10,
        "size": 10,
        "eventSearchVO": {}
    }
    headers = {
        'X-Token': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI3MDAwMzUwNTMyNTM1NTgyNzIifQ.RhXY4Sz6ayef5L-eKY9ja_gBfCnQu3D-2B9napSul2M'
    }
    r = requests.get(url,
                     headers=headers, params=payload, verify=False)
    print(r.text)
    print(json.dumps(r.json(), indent=2).encode("utf-8").decode("unicode-escape"))
    assert r.json()['code'] == '0'
    assert r.status_code == 200


def test_searchWord_find_group_buy_event():
    # 通过搜索关键词查找拼课团，模糊搜索
    url = "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event/list"
    payload = {
        "page": 1,
        "limit": 20,
        "size": 10,
        "searchWord": "取消订单测试",
        "eventSearchVO": "%7B%7D"

    }
    headers = {
        'X-Token': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1ODczNjMwOTYwMDgzMjcyMjIifQ.GHCkx19Zhcz2BKZmNJskYCiI9bJ6SnBYZqlG2WhX4Cw'
    }
    r = requests.request("GET", url, headers=headers, params=payload, verify=False)
    print(r.text)
    print(json.dumps(r.json(), indent=2).encode("utf-8").decode("unicode-escape"))
    assert r.json()['code'] == '0'
    assert r.status_code == 200


@pytest.mark.parametrize("type", [['pt'], ['test']])
def test_add_group_buy_event(type):
    url = "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/common/get_new_resource_id"
    payload = {"type": type}
    headers = {
        'X-Token': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI3MDAwMzUwNTMyNTM1NTgyNzIifQ.RhXY4Sz6ayef5L-eKY9ja_gBfCnQu3D-2B9napSul2M'

    }
    r = requests.get(url, headers=headers, params=payload)
    print(r.text)
    print(json.dumps(r.json(), indent=2))
    print(r.json()['data'])
    assert r.status_code == 200
    resource_id = r.json()['data']
    return resource_id


def test_update_group_buy_event():
    url = "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event"

    payload = {
        "checkinQrcodeToggle": False,
        "banner": "",
        "beginTime": 1612627200000,
        "endTime": 1615132800000,
        "cancelReviewToggle": True,
        "coverImage": "",
        "guideImage": "",
        "remindHours": 1,
        "descr": "",
        "detail": "",
        "effectiveHours": 1,
        "effectiveType": "RELATIVE_DATE",
        "customerServerShowVO": {
            "iconName": "",
            "image": "",
            "title": ""
        },
        "customerServerGuideOpened": False,
        "form": "[]",
        "groupBuyEventTeamRules": [
            {
                "leaderPrice": 0,
                "maxNumber": 6,
                "memberPrice": 0,
                "size": 1,
                "begintNumber": 0
            }
        ],
        "resourceId": "pt_813830799357304832",
        "robotRules": [],
        "storeOrgIds": [
            "768419663792685056"
        ],
        "tags": [],
        "repeatJoin": False,
        "teamLastTimeType": "LIMITLESS",
        "teamLastTimeHours": 0,
        "titile": "接口自动化",
        "studentCanJoin": True,
        "remindTimeType": "BEGIN",
        "eventCategorySecondId": "",
        "eventCategorySecondIdName": "",
        "eventCategoryFirstId": "777280773328846848",
        "eventCategoryFirstIdName": "舆情部",
        "price": "null",
        "effectiveBeginTime": 1612678342000,
        "effectiveEndTime": 1612678342000
    }
    headers = {
        'X-Token': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1ODczNjMwOTYwMDgzMjcyMjIifQ.GHCkx19Zhcz2BKZmNJskYCiI9bJ6SnBYZqlG2WhX4Cw',
        'Content-Type': 'application/json;charset=UTF-8'
    }

    r = requests.request("POST", url, headers=headers, data=payload)
    print(r.text)
    print(json.dumps(r.json(), indent=2))
    print(r.json()['data'])
    event_id = r.json()['data']
    assert r.status_code == 200
    assert len(event_id) > 0
    return event_id


def test_del_group_buy_event():
    url = "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event/813452753813299200"
    # event_id = 808034405862137856
    payload = {}
    headers = {
        'X-Token': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1ODczNjMwOTYwMDgzMjcyMjIifQ.GHCkx19Zhcz2BKZmNJskYCiI9bJ6SnBYZqlG2WhX4Cw'
    }

    r = requests.request("DELETE", url, headers=headers, data=payload)
    print(r.text)
    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200


def test_add_group_buy_event_specification_detail():
    # 为某一个拼课团关联课程班级 拼课团名称：取消订单测试
    url = "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event/813791300195639296/specification"
    # event_id = 813791300195639296
    payload = {
        "groupBuyEventSpecificationDetails": [
            {
                "values": "语文,数学",
                "enabled": True,
                "orderNo": 0,
                "trainingClassId": "699287789878902784",
                "trainingClassName": "励暑语2"
            },
            {
                "values": "语文,英语",
                "enabled": False,
                "orderNo": 1,
                "trainingClassId": "",
                "trainingClassName": ""
            },
            {
                "values": "数学,数学",
                "enabled": True,
                "orderNo": 2,
                "trainingClassId": "",
                "trainingClassName": ""
            },
            {
                "values": "数学,英语",
                "enabled": True,
                "orderNo": 3,
                "trainingClassId": "",
                "trainingClassName": ""
            }
        ],
        "specificationConfs": [
            {
                "level": 1,
                "name": "一年级",
                "values": "语文,数学"
            },
            {
                "level": 2,
                "name": "二年级",
                "values": "数学,英语"
            }
        ]
    }
    headers = {
        'X-Token': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1ODczNjMwOTYwMDgzMjcyMjIifQ.GHCkx19Zhcz2BKZmNJskYCiI9bJ6SnBYZqlG2WhX4Cw',
        'Content-Type': 'application/json;charset=UTF-8'
    }

    r = requests.request("PUT", url, headers=headers, json=payload)
    print(r.text)
    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200


def test_copy_group_buy_event():
    # 复制一个拼课团
    url = "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event/813791300195639296/copy"
    # 拼课团原id = 813791300195639296，返回复制后的拼课团id值，取出data字段
    payload = {}
    headers = {
        'X-Token': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1ODczNjMwOTYwMDgzMjcyMjIifQ.GHCkx19Zhcz2BKZmNJskYCiI9bJ6SnBYZqlG2WhX4Cw'
    }

    r = requests.request("PUT", url, headers=headers, data=payload)
    print(r.text)
    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    # 复制后的拼课团id值，可在group_buy_event表中查询得出
    new_id = r.json()['data']
    print(new_id)
    return new_id


@pytest.mark.parametrize("enable", [['false'], ['true']])
def test_enable_group_buy_event(enable):
    # 撤销和发布一个拼课团
    url = "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event/813830799369887744/enable"
    payload = {"enable": enable}
    headers = {
        'X-Token': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1ODczNjMwOTYwMDgzMjcyMjIifQ.GHCkx19Zhcz2BKZmNJskYCiI9bJ6SnBYZqlG2WhX4Cw'
    }

    r = requests.request("PUT", url, headers=headers, data=payload)
    print(r.text)
    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200


@pytest.mark.parametrize("recommend", [['false'], ['true'], ])
def test_recommend_group_buy_event(recommend):
    # 移除和置顶一个拼课团，recommend字段控制
    url = "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event/813830799369887744/recommend"
    payload = {"recommend": recommend}
    headers = {
        'X-Token': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1ODczNjMwOTYwMDgzMjcyMjIifQ.GHCkx19Zhcz2BKZmNJskYCiI9bJ6SnBYZqlG2WhX4Cw'
    }

    r = requests.request("PUT", url, headers=headers, data=payload)
    print(r.text)
    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200


def test_find_team_group_buy_event():
    # 查看单个拼课团的参团列表
    url = "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event_order/teams"
    # payload = {}
    payload = {
        "page": 1,
        "limit": 20,
        "size": 10,
        "groupBuyEventId": 813791300195639296
    }
    headers = {
        'X-Token': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1ODczNjMwOTYwMDgzMjcyMjIifQ.GHCkx19Zhcz2BKZmNJskYCiI9bJ6SnBYZqlG2WhX4Cw'
    }
    r = requests.request("GET", url, headers=headers, params=payload)
    print(r.text)
    print(json.dumps(r.json(), indent=2).encode("utf-8").decode("unicode-escape"))
    assert r.status_code == 200


def test_find_teamnumber_group_buy_event():
    # 查看拼课团的参团成员
    url = "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event_order/event_rule/numbers"
    # payload={}
    payload = {
        "groupBuyEventId": 813791300195639296
    }
    headers = {
        'X-Token': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1ODczNjMwOTYwMDgzMjcyMjIifQ.GHCkx19Zhcz2BKZmNJskYCiI9bJ6SnBYZqlG2WhX4Cw'
    }
    r = requests.request("GET", url, headers=headers, params=payload)
    print(r.text)
    print(json.dumps(r.json(), indent=2).encode("utf-8").decode("unicode-escape"))
    assert r.status_code == 200


@pytest.mark.parametrize("status", [
    ["PENDING"],
    ["SUCCESS"],
    ["FAILED"],
    ["UNPAID"]])
def test_excel_teamnumber_group_buy_event(status):
    """
    # 导出不同拼课团状态或不同团队成员人数的某一拼课团的参团成员,
    团队大小，teamSize，拼课团团队状态，status：
    - PENDING 拼团中
    - SUCCESS 拼团成功
    - FAILED  拼团失败
    - UNPAID  未支付
    :return:
    """
    url = "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event_order/excel_teams"
    payload = {
        "status": status,
        "groupBuyEventId": 813791300195639296
    }
    headers = {
        'Content-Type': 'text/plain;charset=UTF-8',
        'X-Token': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1ODczNjMwOTYwMDgzMjcyMjIifQ.GHCkx19Zhcz2BKZmNJskYCiI9bJ6SnBYZqlG2WhX4Cw'
    }
    r = requests.request("GET", url, headers=headers, params=payload)
    print(r.text)
    assert r.status_code == 200

def test_launch_list_group_buy_event():
    # 查看单个拼课团的分发管理渠道
    url = "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event/launch_list?page=1&size=10"

    payload = {

        "channelIds": [],
        "groupBuyEventId": "813830799369887744",
        "orgIds": []
    }
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'X-Token': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1ODczNjMwOTYwMDgzMjcyMjIifQ.GHCkx19Zhcz2BKZmNJskYCiI9bJ6SnBYZqlG2WhX4Cw'
    }
    r = requests.request("POST", url, headers=headers, data=json.dumps(payload))
    print(r.text)
    print(json.dumps(r.json(), indent=2).encode("utf-8").decode("unicode-escape"))
    assert r.status_code == 200

def test_channel_list_group_buy_event():
    # 查看所有渠道
    #      https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/channel/list?page=1&limit=20&size=10
    url = "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/channel/list"
    payload = {
        "page": 1,
        "size": 100,

    }
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'X-Token': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1ODczNjMwOTYwMDgzMjcyMjIifQ.GHCkx19Zhcz2BKZmNJskYCiI9bJ6SnBYZqlG2WhX4Cw'
    }
    r = requests.request("GET", url, headers=headers, params=payload)
    print(r.text)
    print(json.dumps(r.json(), indent=2).encode("utf-8").decode("unicode-escape"))
    assert r.status_code == 200


def test_store_list_group_buy_event():
    # 查看所有校区
    url = "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/organizations/store_list"
    payload = {
        "page": 1,
        "size": 100,

    }
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'X-Token': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1ODczNjMwOTYwMDgzMjcyMjIifQ.GHCkx19Zhcz2BKZmNJskYCiI9bJ6SnBYZqlG2WhX4Cw'
    }
    r = requests.request("GET", url, headers=headers, params=payload)
    print(r.text)
    print(json.dumps(r.json(), indent=2).encode("utf-8").decode("unicode-escape"))
    assert r.status_code == 200

def test_url_list_excel_group_buy_event():
    # 下载全部二维码，渠道二维码
    url = "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event/url_list_excel"
    payload = {
        "page": 1,
        "size": 10,
        "channelIds": [],
        "groupBuyEventId": "813830799369887744",
        "orgIds": []
    }
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'X-Token': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1ODczNjMwOTYwMDgzMjcyMjIifQ.GHCkx19Zhcz2BKZmNJskYCiI9bJ6SnBYZqlG2WhX4Cw'
    }
    r = requests.request("POST", url, headers=headers, data=json.dumps(payload))
    #print(r.text)
    #print(json.dumps(r.json(), indent=2).encode("utf-8").decode("unicode-escape"))
    assert r.status_code == 200

def test_add_launch_group_buy_event():
    # 为单个拼课团添加门店及渠道，生成渠道二维码 下载单个二维码不会触发
    url = "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event/launch"

    payload = {
        "page": 1,
        "size": 10,
        "channelIds": [
            "593114936268292096"
        ],
        "groupBuyEventId": "813830799369887744",
        "orgIds": [
            "768419663792685056"
        ]
    }
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'X-Token': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1ODczNjMwOTYwMDgzMjcyMjIifQ.GHCkx19Zhcz2BKZmNJskYCiI9bJ6SnBYZqlG2WhX4Cw'
    }
    r = requests.request("POST", url, headers=headers, data=json.dumps(payload))
    print(r.text)
    print(json.dumps(r.json(), indent=2).encode("utf-8").decode("unicode-escape"))
    assert r.status_code == 200

def test_upload_qrcode_group_buy_event():
    # 下载单个二维码
    url = "https://apex-mini-dev.oss-cn-shanghai.aliyuncs.com/null/mocha_qrcode_4389708749976803471.png"

    payload = {}
    headers = {
        'X-Token': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1ODczNjMwOTYwMDgzMjcyMjIifQ.GHCkx19Zhcz2BKZmNJskYCiI9bJ6SnBYZqlG2WhX4Cw'
    }
    r = requests.request("GET", url, headers=headers, params=payload)
    assert r.status_code == 200

def test_upload_qrcode_group_buy_event():
    #订单号详情
    url = "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event_order/orders"

    payload = {
        "page": 1,
        "limit": 20,
        "size": 10,
        "groupBuyEventId": "813791300195639296",
        "keyWord":"",
        "status":"",
        "orderStatus":"",
        "pamentStatus":""
    }
    headers = {
        'X-Token': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1ODczNjMwOTYwMDgzMjcyMjIifQ.GHCkx19Zhcz2BKZmNJskYCiI9bJ6SnBYZqlG2WhX4Cw'
    }
    r = requests.request("GET", url, headers=headers, params=payload)
    print(r.text)
    print(json.dumps(r.json(), indent=2).encode("utf-8").decode("unicode-escape"))
    assert r.status_code == 200


@pytest.mark.parametrize("status", [
    ["USED"],
    ["UNUSED"]])
def test_search_group_buy_event(status):
    # 后台核销 ,status:USED 已核销 UNUSED 未核销，keyWord:兑换码，订单号，会员手机号
    "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event_order/search?page=1&limit=20&size=20&groupBuyEventId=800759900083118080&keyWord=&status=UNUSED"
    url = "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event_order/search"

    payload = {
        "page": 1,
        "size": 100,
        "limit": 20,
        "groupBuyEventId": "813791300195639296",
        "keyWord": "",
        "status": status
    }
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'X-Token': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1ODczNjMwOTYwMDgzMjcyMjIifQ.GHCkx19Zhcz2BKZmNJskYCiI9bJ6SnBYZqlG2WhX4Cw'
    }
    r = requests.request("GET", url, headers=headers, params=payload)
    print(r.text)
    print(json.dumps(r.json(), indent=2).encode("utf-8").decode("unicode-escape"))
    assert r.status_code == 200



# def teardown():
#    pass

