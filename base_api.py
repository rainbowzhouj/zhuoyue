import json

import requests


class BaseApi:
    def __init__(self):
        self.token = self.get_token()

    # def test_login():
    #     # 登录
    #     url = "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/tenants/login"
    #     payload = "{\"username\":\"test\",\"password\":\"test\"}"
    #     headers = {
    #         'Content-Type': 'application/json;charset=UTF-8'
    #     }
    #
    #     r = requests.post(url, headers=headers, data=payload, verify=False)
    #     print(r.text)
    #     print(json.dumps(r.json(), indent=2))
    #     print(r.json()['data']['token'])
    #     assert r.status_code == 200
    #     assert r.json()['code'] == '0'
    #     token = r.json()['data']['token']
    #     return token

    def get_token(self):
        username = 'zhuoyue'
        password = '123456'
        data = {
            "method": "post",
            "url": 'https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/tenants/login',
            "params": {'username': username, 'password': password}
        }
        r = self.send(data)
        token = r.json()['data']['token']
        return token

    def send(self, kwargs):
        r = requests.request(**kwargs)
        print(json.dumps(r.json(), indent=2))
        return r