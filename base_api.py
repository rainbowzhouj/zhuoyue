import json

import requests
import yaml



class BaseApi:
    params = {}
    def __init__(self):
        # todo ：此处环境可以用conftest 进行管理pytest fixtures(scope=session)，设置env  小程序端为：clt 营销中台端为：dab
        self.base_url="https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab"
        self.token = self.get_token()
        self.params["token"] = self.token
        self.params["base_url"] = self.base_url
        #self.Base_url = "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/clt"
        #self.accesstoken=self.get_accessToken()


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
    """
    小程序自动化
    todo：accessToken 参数化
    
    """

    # def get_accessToken(self):
    #     """
    #      文豪：
    #     # eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJvcmdhbml6YXRpb25JZCI6NTg3MzU3NTM5NzU5MjkyNDE2LCJzdWIiOiI3ODQzNTg1NTQ0NTg1MDUyMTYiLCJhcHBJZCI6Ind4YTZjODMwZmY4NjUwY2MzNyIsImlzcyI6Im1vY2hhIiwid29ya2VyIjp0cnVlLCJleHAiOjE2MTU0Njg1MzIsImlhdCI6MTYxNTQzMjUzMn0.ALqIvGPoPhebvHvLHW7i7NqhnzcFhQnkFQZNXEW_KGo
    #     # 周晶
    #     # eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJvcmdhbml6YXRpb25JZCI6NTg3MzU3NTM5NzU5MjkyNDE2LCJzdWIiOiI3OTg5OTE4MjExOTI0ODY5MTIiLCJhcHBJZCI6Ind4YTZjODMwZmY4NjUwY2MzNyIsImlzcyI6Im1vY2hhIiwid29ya2VyIjpmYWxzZSwiZXhwIjoxNjE1NDM2MTA5LCJpYXQiOjE2MTU0MzI1MDl9.b-PxpGBiO_GzCpsRKIcDCrzFSM2tNco6zRlp2I0Cxcc
    #     # 邓鑫：
    #     eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJvcmdhbml6YXRpb25JZCI6NTg3MzU3NTM5NzU5MjkyNDE2LCJzdWIiOiI3OTg5OTQyNTMxMDQ0NzIwNjQiLCJhcHBJZCI6Ind4YTZjODMwZmY4NjUwY2MzNyIsImlzcyI6Im1vY2hhIiwid29ya2VyIjpmYWxzZSwiZXhwIjoxNjE1NDY0MDI3LCJpYXQiOjE2MTU0MjgwMjd9.YMfXCIr5PaC46c0nOHLAMBQD9W4GEvDlviRO59Hxa1c
    #     # 于俊
    #     eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJvcmdhbml6YXRpb25JZCI6NTg3MzU3NTM5NzU5MjkyNDE2LCJzdWIiOiI4MTk2MzE1ODY0MjY2NzUyMDAiLCJhcHBJZCI6Ind4YTZjODMwZmY4NjUwY2MzNyIsImlzcyI6Im1vY2hhIiwiZXhwIjoxNjE1NDkyOTk4LCJpYXQiOjE2MTU0NTY5OTh9.N_1E4DAEhAJ_nSMICVajd5EugXra8i3C80gdvAFbYsk
    #     :return:
    #     """
    #     data = {
    #         "method": "get",
    #         "url":  f"{self.Base_url}/wechat/login",
    #         "headers": {'Content-Type': 'application/json;charset=UTF-8',
    #                     'X-Wx-Appid': 'wxa6c830ff8650cc37',
    #                     'accessToken': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJvcmdhbml6YXRpb25JZCI6NTg3MzU3NTM5NzU5MjkyNDE2LCJzdWIiOiI3OTg5OTE4MjExOTI0ODY5MTIiLCJhcHBJZCI6Ind4YTZjODMwZmY4NjUwY2MzNyIsImlzcyI6Im1vY2hhIiwid29ya2VyIjpmYWxzZSwiZXhwIjoxNjE1NDM2MTA5LCJpYXQiOjE2MTU0MzI1MDl9.b-PxpGBiO_GzCpsRKIcDCrzFSM2tNco6zRlp2I0Cxcc',
    #                     },
    #         "params": {"code": ""}
    #     }
    #     r = self.send(data)
    #     accesstoken = r.json()['data']['accessToken']
    #     return accesstoken

    def send(self, data):
        raw_data = json.dumps(data)
        for key, value in self.params.items():
            raw_data = raw_data.replace("${" + key + "}", value)
        data = json.loads(raw_data)
        #r = requests.request(**data).json()
        r = requests.request(**data)
        # print(json.dumps(r.json(), indent=2).encode("utf-8").decode("unicode-escape"))
        return r
