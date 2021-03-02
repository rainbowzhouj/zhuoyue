import json

import requests


class BaseApi:
    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        data = {
            "method": "post",
            "url": "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/tenants/login",
            "headers": {'Content-Type': 'application/json;charset=UTF-8'},
            "json": {"username": "zhuoyue",
                     "password": "123456"}
        }
        r = self.send(data)
        token = r.json()['data']['token']
        return token

    def send(self, kwargs):
        r = requests.request(**kwargs)
        print(json.dumps(r.json(), indent=2).encode("utf-8").decode("unicode-escape"))
        return r
