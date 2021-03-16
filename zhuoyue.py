import allure
import yaml

from base_api import BaseApi


class Zhuoyue(BaseApi):
    def __init__(self):
        super().__init__()

    def list_member(self):
        data = {
            "method": "get",
            "url": f"{self.Base_url}/members",
            "params": {},
            "headers": {'Content-Type': 'application/json;charset=UTF-8',
                        'X-Wx-Appid': 'wxa6c830ff8650cc37',
                        'accessToken': self.accesstoken,
                        }
        }
        return self.send(data)


    def list_group_buy_event(self, group_buy_event_id):
        data = {
            "method": "get",
            "url": f"{self.Base_url}/group_buy_event/" + group_buy_event_id,
            "params": {},
            "headers": {'Content-Type': 'application/json;charset=UTF-8',
                        'X-Wx-Appid': 'wxa6c830ff8650cc37',
                        'accessToken': self.accesstoken,
                        }
        }
        return self.send(data)

    @allure.feature('活动地址兑换信息')
    def list_groupBuyEventDetailSecond(self, group_buy_event_id):
        data = {
            "method": "get",
            "url": f"{self.Base_url}/group_buy_event/groupBuyEventDetailSecond/" + group_buy_event_id,
            "params": {},
            "headers": {'Content-Type': 'application/json;charset=UTF-8',
                        'X-Wx-Appid': 'wxa6c830ff8650cc37',
                        'accessToken': self.accesstoken,
                        }
        }
        return self.send(data)

    @allure.feature('活动规格信息')
    def list_groupBuyEventDetailThree(self, group_buy_event_id):
        data = {
            "method": "get",
            "url": f"{self.Base_url}/group_buy_event/groupBuyEventDetailThree/" + group_buy_event_id,
            "params": {},
            "headers": {'Content-Type': 'application/json;charset=UTF-8',
                        'X-Wx-Appid': 'wxa6c830ff8650cc37',
                        'accessToken': self.accesstoken,
                        }
        }
        return self.send(data)


    def get_resources(self, resourceId):
        data = {
            "method": "get",
            "url": f"{self.Base_url}/resources/" + resourceId,
            "params": {},
            "headers": {'Content-Type': 'application/json;charset=UTF-8',
                        'X-Wx-Appid': 'wxa6c830ff8650cc37',
                        'accessToken': self.accesstoken,
                        }
        }
        return self.send(data)

    def add_teams(self,group_buy_event_id):
        with open('./datas/team.yml',encoding='utf-8')as f:
            team=yaml.safe_load(f)
        data = {
            "method": "post",
            "url": f"{self.Base_url}/group_buy_event/teams",
            "json": team,
            "headers": {'Content-Type': 'application/json;charset=UTF-8',
                        'X-Wx-Appid': 'wxa6c830ff8650cc37',
                        'accessToken': self.accesstoken,
                        }
        }


        return self.send(data)


    def cancel_orders(self, orderId):
        data = {
            "method": "put",
            "url": f"{self.Base_url}/group_buy_event/orders/" + orderId,
            "params": {},
            "headers": {'Content-Type': 'application/json;charset=UTF-8',
                        'X-Wx-Appid': 'wxa6c830ff8650cc37',
                        'accessToken': self.accesstoken,
                        }
        }
        return self.send(data)

    def get_orders(self):
        data = {
            "method": "get",
            "url": f"{self.Base_url}/group_buy_event/orders",
            "params": {"page":1,
                       "size":10,
                       "type":"",
                       "beginTime":"",
                       "endTime": "",
                       "minAmount": "",
                       "maxAmount": "",
                       "keyWord": ""
                       },
            "headers": {'Content-Type': 'application/json;charset=UTF-8',
                        'X-Wx-Appid': 'wxa6c830ff8650cc37',
                        'accessToken': self.accesstoken,
                        }
        }
        return self.send(data)