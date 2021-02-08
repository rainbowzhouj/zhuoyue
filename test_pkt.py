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
import requests
#登录营销中台
url = "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/tenants/login"
payload="{\"username\":\"test\",\"password\":\"test\"}"
headers = {
  'Content-Type': 'application/json;charset=UTF-8'
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)

# 选择营销工坊->拼课团
url = "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event/list?page=1&limit=20&size=10&eventSearchVO=%7B%7D"

payload={}
headers = {
  'X-Token': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI3MDAwMzUwNTMyNTM1NTgyNzIifQ.RhXY4Sz6ayef5L-eKY9ja_gBfCnQu3D-2B9napSul2M'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

# 创建拼课团
import requests

url = "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/common/get_new_resource_id?type=pt"

payload={}
headers = {
  'X-Token': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI3MDAwMzUwNTMyNTM1NTgyNzIifQ.RhXY4Sz6ayef5L-eKY9ja_gBfCnQu3D-2B9napSul2M'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


"""

def test_login():
    # 登录
    url = "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/tenants/login"
    payload="{\"username\":\"test\",\"password\":\"test\"}"
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

    json = {
            "checkinQrcodeToggle": "false",
            "banner": "",
            "beginTime": 1612627200000,
            "endTime": 1615132800000,
            "cancelReviewToggle": "true",
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
            "customerServerGuideOpened": "false",
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
            "resourceId": "pt_807976863172452352",
            "robotRules": [],
            "storeOrgIds": [
                "768419758852390912"
            ],
            "tags": [],
            "repeatJoin": "false",
            "teamLastTimeType": "LIMITLESS",
            "teamLastTimeHours": 0,
            "titile": "1",
            "studentCanJoin": "true",
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

    r = requests.request("POST", url, headers=headers, data=json)

    print(r.text)
    print(json.dumps(r.json(), indent=2))
    print(r.json()['data'])
    event_id=r.json()['data']
    assert r.status_code == 200
    assert len(event_id) >0
    return event_id

def test_del_group_buy_event():

    url = "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event/808034405862137856"
    # event_id = 808034405862137856
    payload = {}
    headers = {
        'X-Token': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1ODczNjMwOTYwMDgzMjcyMjIifQ.GHCkx19Zhcz2BKZmNJskYCiI9bJ6SnBYZqlG2WhX4Cw'
    }

    r = requests.request("DELETE", url, headers=headers, data=payload)
    print(r.text)
    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200

# def teardown():
#    pass
