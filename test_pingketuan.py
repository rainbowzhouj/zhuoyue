import datetime
import json
import pytest
from jsonpath import jsonpath

from pingketuan import Pingketuan


class TestPingketuan:
    def setup_class(self):
        self.pkt = Pingketuan()

    @pytest.mark.parametrize("type", [['pt'], ['test']])
    def test_add_pkt(self, type):
        r = self.pkt.add(type=type)
        print(json.dumps(r.json(), indent=2).encode("utf-8").decode("unicode-escape"))
        assert r.status_code == 200
        assert r.json()["code"] == "0"

    @pytest.mark.parametrize("group_buy_event_id,resourceId,titile", [
        ['813830799369887744', 'pt_813830799357304832', 'zhouj1'],
        ['813830799369887744', 'pt_813830799357304832', 'zhouj2'],
    ])
    def test_update_pkt(self, group_buy_event_id, resourceId, titile):
        titile = titile + str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
        r = self.pkt.update_group_buy_event(group_buy_event_id=group_buy_event_id, resourceId=resourceId, titile=titile)
        r = self.pkt.list_group_buy_event(titile)
        print(json.dumps(r.json(), indent=2).encode("utf-8").decode("unicode-escape"))
        assert r.json()['code'] == '0'
        assert r.status_code == 200
        assert r.json()['data'] != []
        """
        此处因断言类型不一致，会导致报错，解决方式有两种:
        1.将左右两边的类型都改为dict，[]
        2.将左右两边的类型都改为string
        """
        # 方式1
        assert jsonpath(r.json(), f"$.data[1].titile") == [titile]
        # 方式2 assert jsonpath(r,"$..topics[?(@.user.login=='VipMagic')].node_name")[0]=='性能常识'
        # a = jsonpath(r.json(), f"$.data[0].titile")
        # print(a)
        # assert "".join(a) == titile

    def test_list_pkt(self):
        titile = "取消订单测试_副本"
        r = self.pkt.list_group_buy_event(titile)
        print(json.dumps(r.json(), indent=2).encode("utf-8").decode("unicode-escape"))
        assert r.json()['code'] == '0'
        assert r.status_code == 200
        assert r.json()['data'] != []

    def test_delete_pkt(self):
        # group_buy_event_id="813837484247408640" 删除不存在的情况无报错
        self.pkt.delete_update_group_buy_event("813837484247408640")

    def test_add_group_buy_event_specification_detail(self):
        # 为某一个拼课团关联课程班级 拼课团名称：取消订单测试,未进行参数化，需进一步封装
        self.pkt.add_group_buy_event_specification_detail()

    def test_copy_group_buy_event(self):
        # 复制一个拼课团
        r=self.pkt.copy_group_buy_event("813791300195639296")
        assert r.json()['code'] == '0'
        assert r.status_code == 200
        new_id = r.json()['data']
        print(new_id)
        return new_id

    @pytest.mark.parametrize("group_buy_event_id,enable", [["815170951962877952",False], ["815170951962877952",True]])
    def test_enable_group_buy_event(self,group_buy_event_id,enable):
        # 撤销和发布一个拼课团
        r = self.pkt.enable_group_buy_event(group_buy_event_id=group_buy_event_id,enable=enable)
        r= self.pkt.list_group_buy_event("取消订单测试")
        assert r.json()['code'] == '0'
        assert r.status_code == 200
        assert jsonpath(r.json(), f"$.data[2].enable") == [enable]

    @pytest.mark.parametrize("group_buy_event_id,recommend", [["815170951962877952",False], ["815170951962877952",True]])
    def test_recommend_group_buy_event(self,group_buy_event_id,recommend):
        # 移除和置顶一个拼课团，recommend字段控制
        r=self.pkt.recommend_group_buy_event(group_buy_event_id=group_buy_event_id,recommend=recommend)
        r = self.pkt.list_group_buy_event("取消订单测试")
        assert r.json()['code'] == '0'
        assert r.status_code == 200
        assert jsonpath(r.json(), f"$.data[1].recommend") == [recommend]

    @pytest.mark.parametrize("group_buy_event_id",
                             [["815170951962877952"], ["813791300195639296"], ["813791300195639297"]])
    def test_find_team_group_buy_event(self, group_buy_event_id):
        # 测试查看单个拼课团的参团列表,前两个为存在，后一个不存在
        r = self.pkt.find_team_group_buy_event(group_buy_event_id=group_buy_event_id)
        print(json.dumps(r.json(), indent=2).encode("utf-8").decode("unicode-escape"))
        assert r.json()['code'] == '0'
        """
        参团列表为空,分为两种情况：
        1.拼课团活动存在，但无人参加该拼课团；
        2.拼课团活动不存在.
        """
        assert r.json()['data'] != []

    @pytest.mark.parametrize("group_buy_event_id",
                             [["815170951962877952"], ["813791300195639296"], ["813791300195639297"]])
    def test_find_teamnumber_group_buy_event(self, group_buy_event_id):
        # 测试查看单个拼课团的查看拼课团的参团成员,前两个为存在，后一个不存在
        r = self.pkt.find_teamnumber_group_buy_event(group_buy_event_id=group_buy_event_id)

        assert r.json()['code'] == '0'
        """
        参团成员为空,分为两种情况：
        1.拼课团活动存在，但无人参加该拼课团；
        2.拼课团活动不存在.
        """
        assert r.json()['data'] != []

    @pytest.mark.parametrize("group_buy_event_id,status", [
        ["813791300195639296","PENDING"],
        ["813791300195639296","SUCCESS"],
        ["813791300195639296","FAILED"],
        ["813791300195639296","UNPAID"]])
    def test_excel_teamnumber_group_buy_event(self, group_buy_event_id,status):
        """
        # 导出不同拼课团状态或不同团队成员人数的某一拼课团的参团成员,
        团队大小，teamSize，拼课团团队状态，status：
        - PENDING 拼团中
        - SUCCESS 拼团成功
        - FAILED  拼团失败
        - UNPAID  未支付
        :return:
        """
        r = self.pkt.excel_teamnumber_group_buy_event(group_buy_event_id=group_buy_event_id,status=status)
        assert r.status_code == 200

    def test_channel_list_group_buy_event(self):
        # 查看所有渠道
        r = self.pkt.channel_list_group_buy_event()
        assert r.json()['code'] == '0'
        a = jsonpath(r.json(), f"$..name")[0]
        #print(a)
        assert "".join(a) == "线上-微信"

    def test_store_list_group_buy_event(self):
        # 查看所有校区
        r=self.pkt.store_list_group_buy_event()
        assert r.json()['code'] == '0'
        a = jsonpath(r.json(), f"$..data[0].name")
        # print(a)
        assert "".join(a) == "虹口校区"

    def test_url_list_excel_group_buy_event(self):
        group_buy_event_id1="813830799369887744"
        # 下载全部二维码，渠道二维码
        r = self.pkt.url_list_excel_group_buy_event(group_buy_event_id1)
        assert r.status_code == 200

    @pytest.mark.parametrize("group_buy_event_id,organizationId,channelIds",[["813830799369887744","768419663792685056","593114936268292096"]])
    def test_add_launch_group_buy_event(self,group_buy_event_id,organizationId,channelIds):
        # 为单个拼课团添加门店及渠道，生成渠道二维码
        # channelIds ="593114936268292096"
        # organizationId = "768419663792685056"
        # group_buy_event_id = "813830799369887744"
        r= self.pkt.add_launch_group_buy_event(channelIds,group_buy_event_id,organizationId)
        print(r.text)

        assert r.status_code == 200
        a = jsonpath(r.json(), f"$..data[0].storeName")
        # print(a)
        assert "".join(a) == "虹口校区"

    def test_upload_qrcode_group_buy_event(self):
        # 下载单个二维码
        r=self.pkt.upload_qrcode_group_buy_event()
        assert r.status_code == 200
        #print(r)

    def test_upload_qrcode_group_buy_event():
        # 订单号详情

        print(r.text)
        print(json.dumps(r.json(), indent=2).encode("utf-8").decode("unicode-escape"))
        assert r.status_code == 200

# 为某一个拼课团关联课程班级 拼课团名称：取消订单测试

    # ['813791300195639296','pt_813791300145307648', '取消订单测试3'],
    # ['zhouj3——中文20210226-150607'] == ['zhouj120210226-152702']
    # ['zhouj3——中文20210226-150607'] == ['zhouj220210226-152703']
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
