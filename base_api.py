import json

import requests


class BaseApi:
    def __init__(self):
        # 此处环境可以用conftest 进行管理pytest fixtures(scope=session)，设置env  小程序端为：clt 营销中台端为：dab
        self.base_url="https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab"
        self.token = self.get_token()
        # self.params["token"]=self.token

    # "url": "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/tenants/login",
    def get_token(self):
        data = {
            "method": "post",
            "url":  f"{self.base_url}/tenants/login",
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
