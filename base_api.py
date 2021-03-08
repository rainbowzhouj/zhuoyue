import json

import requests


class BaseApi:
    def __init__(self):
        self.token = self.get_token()
        self.base_url="https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab"
        # self.params["token"]=self.token

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

    def send(self,data):
        # raw_data = json.dumps(data)
        # for key,value in self.params.items():
        #     raw_data= raw_data.replace("${"+key+"}",value)

        # r = requests.request(**data).json()
        r = requests.request(**data)
        print(json.dumps(r.json(), indent=2).encode("utf-8").decode("unicode-escape"))
        return r
