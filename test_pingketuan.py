import datetime
import json
import pytest
from jsonpath import jsonpath

#from address_list.tongxun import Tongxun, PhoneNOGenerator

from pingketuan import Pingketuan


class TestPingketuan:
    def setup_class(self):
        self.pkt = Pingketuan()
    def test_add_pkt(self):
        pass
    @pytest.mark.parametrize("group_buy_event_id,resourceId,titile",[
        ['813830799369887744','pt_813830799357304832', 'zhouj1'],
        ['813830799369887744','pt_813830799357304832', 'zhouj2'],
    ])
    def test_list_pkt(self,group_buy_event_id,resourceId,titile):
        titile = titile+ str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
        r = self.pkt.list()
        r=self.pkt.update_group_buy_event(group_buy_event_id=group_buy_event_id,resourceId=resourceId, titile=titile)
        r=self.pkt.list()
        print(json.dumps(r.json(), indent=2).encode("utf-8").decode("unicode-escape"))
        assert r.json()['code'] == '0'
        assert r.status_code == 200
        assert r.json()['data'] != []
        assert jsonpath(r.json(), f"$.data[1].titile") == [titile]



    def test_update_pkt(self):
        pass

    #         ['813791300195639296','pt_813791300145307648', '取消订单测试3'],
    #['zhouj3——中文20210226-150607'] == ['zhouj120210226-152702']
    #['zhouj3——中文20210226-150607'] == ['zhouj220210226-152703']
    # def test_add_user(self):
    #     userid = "liumengqing"
    #     # 名字为中文时，存在转义问题
    #     name = "Zz"
    #     pg = PhoneNOGenerator()
    #     mobile = pg.phoneNORandomGenerator()
    #     department = "1"
    #     r = self.user.add(userid=userid, name=name, mobile=mobile, department=department)
    #     assert r.status_code == 200
    #     assert r.json()["errcode"] == 0
    #
    # def test_add_and_delete(self):
    #     name = "lN"
    #     userid = "liumengqing"
    #     pg = PhoneNOGenerator()
    #     mobile = pg.phoneNORandomGenerator()
    #     self.user.add_and_delete(name=name, userid=userid, mobile=mobile, department=[]
    #                              )
    #
    # @pytest.mark.parametrize("userid, user_name", [
    #     ['liumengqing', 'Zreturn_'],
    #     ['liumengqing', 'UIAutomartor'],
    #     ['liumengqing', 'mitmproxy[中文]'],
    # ])
    # def test_update_user(self, userid, user_name):
    #     user_name = user_name + str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
    #     r = self.user.update(userid=userid, user_name=user_name)
    #     r = self.user.list(userid=userid)
    #     assert r.status_code == 200
    #     assert r.json()["errcode"] == 0
    #     a = jsonpath(r.json(), f"$..name")
    #     print(a)
    #     assert "".join(a) == user_name
    #
    # def test_list_user(self):
    #     userid = "liumengqing"
    #     r = self.user.list(userid=userid)
    #     assert r.status_code == 200
    #     assert r.json()["userid"] == "liumengqing"
    #
    # # 如果 60111 ，invalid userid
    # # 0. 添加 user
    # # 1. 删除 userid 有问题
    # # 2. 再进行重试（重试次数： n）：手动实现
    # #   a. 添加一个接口
    # #   b. 对新添加的接口再删除
    # #   c. 查询删除是否成功
    # def test_delete_user(self):
    #     # userid="liumengqing"
    #     self.user.delete(["liumengqing"])
    #
    # def test_delete_and_detect_user(self):
    #     r = self.user.delete_and_detect_user(["liumengqing"])
    #     print(json.dumps(r.json(), indent=2))
    #
    # def test_department(self):
    #     self.user.get_partyid()