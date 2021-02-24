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
# 更新拼课团
import requests

url = "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event"

payload="{\r\n    \"checkinQrcodeToggle\": false,\r\n    \"banner\": \"\",\r\n    \"beginTime\": 1613923200000,\r\n    \"endTime\": 1643644800000,\r\n    \"cancelReviewToggle\": true,\r\n    \"coverImage\": \"\",\r\n    \"guideImage\": \"\",\r\n    \"remindHours\": 1,\r\n    \"descr\": \"\",\r\n    \"detail\": \"\",\r\n    \"effectiveHours\": 2,\r\n    \"effectiveType\": \"RELATIVE_DATE\",\r\n    \"customerServerShowVO\": {\r\n        \"iconName\": \"\",\r\n        \"image\": \"\",\r\n        \"title\": \"\"\r\n    },\r\n    \"customerServerGuideOpened\": false,\r\n    \"form\": \"[]\",\r\n    \"groupBuyEventTeamRules\": [\r\n        {\r\n            \"leaderPrice\": 0,\r\n            \"maxNumber\": 33,\r\n            \"memberPrice\": 0,\r\n            \"size\": 33,\r\n            \"begintNumber\": 0\r\n        }\r\n    ],\r\n    \"resourceId\": \"pt_813361571650920448\",\r\n    \"robotRules\": [],\r\n    \"storeOrgIds\": [\r\n        \"768419663792685056\"\r\n    ],\r\n    \"tags\": [],\r\n    \"repeatJoin\": false,\r\n    \"teamLastTimeType\": \"LIMITLESS\",\r\n    \"teamLastTimeHours\": 0,\r\n    \"titile\": \"test\",\r\n    \"studentCanJoin\": false,\r\n    \"remindTimeType\": \"BEGIN\",\r\n    \"eventCategorySecondId\": \"799246111471493120\",\r\n    \"eventCategorySecondIdName\": \"员工mock\",\r\n    \"eventCategoryFirstId\": \"754008091141341184\",\r\n    \"eventCategoryFirstIdName\": \"测试\",\r\n    \"price\": null,\r\n    \"effectiveBeginTime\": 1613962236000,\r\n    \"effectiveEndTime\": 1613962236000\r\n}"
headers = {
  'Connection': 'keep-alive',
  'Accept': 'application/json, text/plain, */*',
  'X-Token': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1ODczNjMwOTYwMDgzMjcyMjIifQ.GHCkx19Zhcz2BKZmNJskYCiI9bJ6SnBYZqlG2WhX4Cw',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.74',
  'Content-Type': 'application/json;charset=UTF-8',
  'Origin': 'https://apex-test-zhuoyue-mini-admin.chinapex.com.cn',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Dest': 'empty',
  'Referer': 'https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/',
  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
  'Cookie': 'sidebarStatus=0; vue_admin_template_token=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1ODczNjMwOTYwMDgzMjcyMjIifQ.GHCkx19Zhcz2BKZmNJskYCiI9bJ6SnBYZqlG2WhX4Cw; vue_admin_template_privilege=WORKER_DELETE%2CFISSIONPOSTER_VIEW%2CFISSIONPOSTER_EDIT%2CFISSIONPOSTER_CREATE%2CFISSIONPOSTER_DELETE%2CMEMBER_VIEW%2CMEMBER_EDIT%2CMEMBER_CREATE%2CMEMBER_DELETE%2CSTATIC_TAG_GRPUP_VIEW%2CSTATIC_TAG_GRPUP_EDIT%2CSTATIC_TAG_GRPUP_CREATE%2CSTATIC_TAG_GRPUP_DELETE%2CMEMBER_CONFIG_VIEW%2CMEMBER_CONFIG_EDIT%2CMEMBER_CONFIG_CREATE%2CMEMBER_CONFIG_DELETE%2CMALL_VIEW%2CMALL_EDIT%2CMALL_CREATE%2CMALL_DELETE%2CMALL_CHECKIN%2CMALL_ORDER%2CMALL_STOCK%2CTASK_VIEW%2CTASK_EDIT%2CTASK_CREATE%2CTASK_DELETE%2CPOSTER_VIEW%2CPOSTER_TASK_EDIT%2CPOSTER_TASK_CREATE%2CPOSTER_TASK_DELETE%2CARTICLE_VIEW%2CARTICLE_TASK_EDIT%2CARTICLE_TASK_CREATE%2CARTICLE_TASK_DELETE%2CEVENT_VIEW%2CEVENT_EDIT%2CEVENT_CREATE%2CEVENT_DELETE%2CEVENT_LAUNCH%2CEVENT_CHECKIN%2CEVENT_ORDER%2CSUPER_USER_VIEW%2CSUPER_USER_EDIT%2CSUPER_USER_CREATE%2CSUPER_USER_DELETE%2CORGANIZATION_VIEW%2CORGANIZATION_EDIT%2CORGANIZATION_CREATE%2CORGANIZATION_DELETE%2CROLE_VIEW%2CROLE_EDIT%2CROLE_CREATE%2CROLE_DELETE%2CACCOUNT_VIEW%2CACCOUNT_EDIT%2CACCOUNT_CREATE%2CACCOUNT_DELETE%2CCHANNEL_VIEW%2CCHANNEL_EDIT%2CCHANNEL_CREATE%2CCHANNEL_DELETE%2CEVENT_CATEGORY_VIEW%2CEVENT_CATEGORY_EDIT%2CEVENT_CATEGORY_CREATE%2CEVENT_CATEGORY_DELETE%2CWORKER_VIEW%2CWORKER_CREATE%2CWORKER_EDIT%2CGROUP_BUY_EVENT_VIEW%2CGROUP_BUY_EVENT_EDIT%2CGROUP_BUY_EVENT_CREATE%2CGROUP_BUY_EVENT_TEAM%2CGROUP_BUY_EVENT_DELETE%2CGROUP_BUY_EVENT_LAUNCH%2CGROUP_BUY_EVENT_CHECKIN%2CGROUP_BUY_EVENT_ORDER%2CTASK_CENTER_VIEW%2CTASK_CENTER_ADD%2CTASK_CENTER_EDIT%2CTASK_CENTER_RELEASE%2CTASK_CENTER_DELETE%2CTASK_CENTER_BACK%2CEVENT_REPORT_VIEW%2CEVENT_REPORT_EXPORT%2CGROUP_EVENT_REPORT_VIEW%2CGROUP_EVENT_REPORT_EXPORT%2CMEMBER_GROWTH_REPORT_VIEW%2CMEMBER_GROWTH_REPORT_EXPORT%2CMEMBER_POINTS_REPORT_VIEW%2CMEMBER_POINTS_REPORT_EXPORT%2CATTEND_CLASS_AMOUNT_REPORT_VIEW%2CATTEND_CLASS_AMOUNT_REPORT_EXPORT%2CALL_MARKET_REPORT_VIEW%2CALL_MARKET_REPORT_EXPORT'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


"""
global new_id
def test_login():
    # 登录
    url = "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/tenants/login"
    payload="{\"username\":\"zhuoyue\",\"password\":\"123456\"}"
    headers = {
        'Content-Type': 'application/json;charset=UTF-8'
    }

    r = requests.post(url, headers=headers, data=payload,verify=False)
    print(r.text)
    print(json.dumps(r.json(), indent=2))
    print(r.json()['data']['token'])
    assert r.status_code == 200
    assert r.json()['code'] == '0'
    token = r.json()['data']['token']
    return token

def test_find_group_buy_event():
    #显示拼课团列表
    url = "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event/list?page=1&limit=20&size=10&eventSearchVO={}"
    payload = {}
    r = requests.get(url,
                      headers={
                                'Content-Type': 'application/json;charset=UTF-8',
                                'X-Token': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI3MDAwMzUwNTMyNTM1NTgyNzIifQ.RhXY4Sz6ayef5L-eKY9ja_gBfCnQu3D-2B9napSul2M'
                                },
                      data=payload,
                      verify=False)
    print(r.text)
    print(json.dumps(r.json(), indent=2))
    assert r.json()['code'] == '0'
    assert r.status_code == 200


def test_searchWord_find_group_buy_event():
    # 通过搜索关键词查找拼课团，模糊搜索
    url = "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event/list?page=1&limit=20&size=10&searchWord=%E5%8F%96%E6%B6%88%E8%AE%A2%E5%8D%95&eventSearchVO=%7B%7D"
    payload = {}
    # payload = {
    #     "page": 1,
    #     "limit": 20,
    #     "size": 10,
    #     "searchWord": "取消订单测试",
    #     "eventSearchVO": "%7B%7D"
    #
    # }
    headers = {
        'X-Token': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1ODczNjMwOTYwMDgzMjcyMjIifQ.GHCkx19Zhcz2BKZmNJskYCiI9bJ6SnBYZqlG2WhX4Cw'
    }
    r = requests.request("GET", url, headers=headers, data=payload,verify=False)
    print(r.text)
    print(json.dumps(r.json(), indent=2).encode("utf-8").decode("unicode-escape"))
    assert r.json()['code'] == '0'
    assert r.status_code == 200

def test_add_group_buy_event():
    url = "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/common/get_new_resource_id?type=pt"
    payload = {}
    headers = {
        'X-Token': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI3MDAwMzUwNTMyNTM1NTgyNzIifQ.RhXY4Sz6ayef5L-eKY9ja_gBfCnQu3D-2B9napSul2M'
    }

    r = requests.get(url, headers=headers, data=payload)

    print(r.text)
    print(json.dumps(r.json(), indent=2))
    print(r.json()['data'])
    assert r.status_code == 200
    resource_id=r.json()['data']
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
            "resourceId": "pt_813346305852366848",
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
    event_id=r.json()['data']
    assert r.status_code == 200
    assert len(event_id) >0
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
    #为某一个拼课团关联课程班级 拼课团名称：取消订单测试
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
    #复制后的拼课团id值，可在group_buy_event表中查询得出
    new_id=r.json()['data']
    print(new_id)
    return new_id

@pytest.mark.parametrize("enable",[['false'],['true']])
def test_enable_group_buy_event(enable):
    # 撤销和发布一个拼课团
    url = "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event/813830799369887744/enable"
    payload = {"enable":enable}
    headers = {
        'X-Token': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1ODczNjMwOTYwMDgzMjcyMjIifQ.GHCkx19Zhcz2BKZmNJskYCiI9bJ6SnBYZqlG2WhX4Cw'
    }

    r = requests.request("PUT", url, headers=headers, data=payload)
    print(r.text)
    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200

@pytest.mark.parametrize("recommend", [        ['false'],        ['true'],    ])
def test_recommend_group_buy_event(recommend):
    # 移除和置顶一个拼课团，recommend字段控制
    url = "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event/813830799369887744/recommend"
    payload = {"recommend":recommend}
    headers = {
        'X-Token': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1ODczNjMwOTYwMDgzMjcyMjIifQ.GHCkx19Zhcz2BKZmNJskYCiI9bJ6SnBYZqlG2WhX4Cw'
    }

    r = requests.request("PUT", url, headers=headers, data=payload)
    print(r.text)
    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200

def test_find_team_group_buy_event():
    # 查看拼课团的参团列表
    url = "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event_order/teams?page=1&limit=20&size=10&groupBuyEventId=813791300195639296"
    payload = {}
    # payload = {
    #     "page": 1,
    #     "limit": 20,
    #     "size": 10,
    #     "groupBuyEventId": 813791300195639296
    #     }
    headers = {
        'X-Token': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1ODczNjMwOTYwMDgzMjcyMjIifQ.GHCkx19Zhcz2BKZmNJskYCiI9bJ6SnBYZqlG2WhX4Cw'
    }
    r = requests.request("GET", url, headers=headers, data=payload)
    print(r.text)
    print(json.dumps(r.json(), indent=2).encode("utf-8").decode("unicode-escape"))
    assert r.status_code == 200


def test_find_team_group_buy_event():
    # 查看拼课团的参团成员
    url = "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event_order/teams"
    payload = {
        "page": 1,
        "limit": 20,
        "size": 10,
        "groupBuyEventId": 813791300195639296
    }
    headers = {
        'X-Token': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1ODczNjMwOTYwMDgzMjcyMjIifQ.GHCkx19Zhcz2BKZmNJskYCiI9bJ6SnBYZqlG2WhX4Cw'
    }
    r = requests.request("GET", url, headers=headers, data=payload)
    print(r.text)
    print(json.dumps(r.json(), indent=2).encode("utf-8").decode("unicode-escape"))
    assert r.status_code == 200

# def teardown():
#    pass
