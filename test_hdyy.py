import datetime

import pytest
from jsonpath import jsonpath

from huodongyuyue import Huodongyuyue


class TestHuoDongYuYue:
    def setup_class(self):
        self.hdyy = Huodongyuyue()

    @pytest.mark.parametrize("type", [['hd'], ['11']])
    def test_add_hdyy(self, type):
        r = self.hdyy.add(type=type)
        assert r.status_code == 200
        assert r.json()["code"] == "0"

    # todo：测试数据放到数据文件中
    @pytest.mark.parametrize("event_id,resourceId,name", [
        ['817429315200802816', 'hd_817403833071755264', 'test_1'],
        ['817429315200802816', 'hd_817403833071755264', 'test_hd'],
    ])
    def test_update_hdyy(self,event_id, resourceId, name):
        name = name + str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
        r = self.hdyy.update_event(event_id=event_id, resourceId=resourceId,name=name)
        r = self.hdyy.list_event(name)
        assert r.json()['code'] == '0'
        a = jsonpath(r.json(), f"$.data[0].name")
        print(a)
        assert "".join(a) == name

    def test_list_hdyy(self):
        name = "专项测试"
        r = self.hdyy.list_event(name=name)
        assert r.json()['code'] == '0'
        assert r.status_code == 200
        assert r.json()['data'] != []


    def test_delete_hdyy(self):
        # event_id="813837484247408640" 删除不存在的情况无报错
        self.hdyy.delete_update_event("817401071256788992")


    def test_copy_event(self):
        # 复制一个活动,返回响应无新id
        r = self.hdyy.copy_event("817403833122086912")
        assert r.json()['code'] == '0'
        assert r.status_code == 200


    @pytest.mark.parametrize("event_id,publish", [["817428189374111744", True], ["817428189374111744", False]])
    def test_publish_event(self, event_id, publish):
        # 撤销和发布一个活动
        r = self.hdyy.publish_event(event_id=event_id, publish=publish)
        r = self.hdyy.list_event("test_自动化")
        assert r.json()['code'] == '0'
        assert r.status_code == 200
        assert jsonpath(r.json(), f"$.data[0].published") == [publish]
    @pytest.mark.parametrize("event_id,recommend",
                             [["817428189374111744", False], ["817428189374111744", True]])
    def test_recommend_event(self, event_id, recommend):
        # 移除和置顶一个活动，recommend字段控制
        r = self.hdyy.recommend_event(event_id=event_id, recommend=recommend)
        r = self.hdyy.list_event("test_自动化")
        assert r.json()['code'] == '0'
        assert r.status_code == 200
        assert jsonpath(r.json(), f"$.data[0].recommend") == [recommend]

    @pytest.mark.parametrize("event_id", ["799311504953237504"])
    def test_find_get_order_list_event(self, event_id):
        # 测试查看单个活动的参团列表
        # ["817403833122086912"], ["813791300195639296"], ["813791300195639297"]前两个为存在，后一个不存在
        r = self.hdyy.find_get_order_list_event(event_id=event_id)
        assert r.json()['code'] == '0'
        """
        参团列表为空,分为两种情况：
        1.活动活动存在，但无人参加该活动；
        2.活动活动不存在.
        """
        # assert r.json()['data'] != []

    @pytest.mark.parametrize("event_id,status", [["816723048673107968", "UNUSED"], ["816723048673107968", "USED"]])
    def test_find_teamnumber_event(self, event_id, status):
        # 测试搜索单个活动的不同状态成员,已核销与核销记录
        """
        ### 拼课团订单状态说明
        - 待支付 UNPAID
        - 支付处理中 PAY_PROCESSING
        - 已取消 CANCELED
        - 待核销 UNUSED
        - 已核销 USED
        - 取消待审核 CANCEL_REVIEW_PENDING
        - 已超时 TIME_OUT
        - 已失败 TEAM_FAIL
        :param event_id:
        :return:
        """
        r = self.hdyy.find_teamnumber_event(event_id=event_id, status=status)
        assert r.json()['code'] == '0'
        """
        参团成员为空,分为两种情况：
        1.活动活动存在，但无人参加该活动；
        2.活动活动不存在.
        """
        # assert r.json()['data'] != []


    @pytest.mark.parametrize("event_id", ["817429315200802816"])
    def test_find_event_checkin_qrcode(self,event_id):
        # 活动的反向核销？？"817429315200802816"
        r = self.hdyy.find_event_checkin_qrcode(event_id=event_id)
        assert r.json()['code'] == '0'

    def test_canceled_event(self):
        # 取消或退款一个订单，canceled字段控制
        event_id="799311504953237504"
        r = self.hdyy.canceled_event(event_id=event_id)
        r = self.hdyy.find_get_order_list_event(event_id=event_id)
        assert r.json()['code'] == '0'
        assert r.status_code == 200
        assert jsonpath(r.json(), f"$.data[0].status") == ["CANCELED"]