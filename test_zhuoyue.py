import json

import allure
import pytest

from zhuoyue import Zhuoyue


class TestZhuoyue:
    def setup_class(self):
        self.zy = Zhuoyue()

    def test_list_members(self):
        r = self.zy.list_member()
        assert r.json()['code'] == '0'
        assert r.status_code == 200
        assert r.json()['data'] != []
        # assert r.json()['data']['name']== "zj"

    @allure.feature('活动简介')
    @pytest.mark.parametrize('group_buy_event_id', ['818541842147893248'])
    def test_list_group_buy_event(self, group_buy_event_id):
        r = self.zy.list_group_buy_event(group_buy_event_id=group_buy_event_id)
        r = self.zy.list_groupBuyEventDetailSecond(group_buy_event_id=group_buy_event_id)
        r = self.zy.list_groupBuyEventDetailThree(group_buy_event_id=group_buy_event_id)
        assert r.json()['code'] == '0'
        assert r.status_code == 200
        assert r.json()['data'] != []

    @allure.feature('获取活动资源id')
    @pytest.mark.parametrize('resourceId', ['pt_818541842097561600'])
    def test_resources(self,resourceId):
        r=self.zy.get_resources(resourceId=resourceId)
        assert r.json()['code'] == '0'
        assert r.status_code == 200

    @allure.feature('对pkt进行下单')
    @pytest.mark.parametrize('group_buy_event_id', ['818795609996976128'])
    def test_add_teams(self,group_buy_event_id):
        r=self.zy.add_teams(group_buy_event_id=group_buy_event_id)
        assert r.json()['code'] == '0'
        assert r.status_code == 200
        assert r.json()["data"]["groupBuyEventId"]==group_buy_event_id

    @allure.feature('查看我的订单')
    def test_get_orders(self):
        r=self.zy.get_orders()
        assert r.json()['code'] == '0'
        assert r.json()["data"][0]["status"]=="UNUSED"


    """
    
    done：先下单，再取消订单
    todo： 
    若订单，不存在，则添加异常捕获
        code返回100022
        msg为订单不可取消
    若订单，orderId存在，且订单状态正常，则取消订单    
    """
    @allure.feature('取消订单')
    def test_cancel_order(self):
        r = self.zy.add_teams('818795609996976128')
        orderId=r.json()["data"]["orderId"]
        r=self.zy.cancel_orders(orderId=orderId)
        assert r.json()['code'] == '0'
