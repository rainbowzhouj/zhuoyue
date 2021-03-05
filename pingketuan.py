import json
import random
import re
import requests

from base_api import BaseApi


# done 封装代码，去除冗余代码
class Pingketuan(BaseApi):
    # 方式一放到类里：token= None
    # 先获取token
    def __init__(self):
        super().__init__()

    def add(self, type):
        # 创建活动，类型可为拼课团、优惠活动
        data = {
            "method": "get",
            "url": "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/common/get_new_resource_id",
            "params": {"type": type},
            "headers": {'X-Token': self.token}
        }
        return self.send(data)
        # resource_id = r.json()['data']
        # return resource_id

    def update_group_buy_event(self, group_buy_event_id, resourceId, titile):
        # 更新拼课团
        data = {
            "method": "put",
            "url": "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event/" + group_buy_event_id,
            "headers": {
                'X-Token': self.token,
                'Content-Type': 'application/json;charset=UTF-8'
            },
            "json": {
                "shareImageUrl": "https://apex-mini-dev.oss-cn-shanghai.aliyuncs.com/null/7f900cf29daa4b2caf991d9ba8da5788.jpg",
                "customerServerShowVO": {
                    "title": "",
                    "image": "",
                    "iconName": "",
                    "status": False
                },
                "customerServerGuideOpened": False,
                "id": "813830799369887744",
                "resourceId": resourceId,
                "descr": "",
                "titile": titile,
                "beginTime": 1611590400000,
                "form": "[]",
                "endTime": 1643040000000,
                "effectiveType": "RELATIVE_DATE",
                "effectiveHours": 3,
                "banner": "https://apex-mini-dev.oss-cn-shanghai.aliyuncs.com/null/0f554cf567564d6ba5f1f797409004f0.jpg",
                "coverImage": "https://apex-mini-dev.oss-cn-shanghai.aliyuncs.com/null/78db0280fc0a4f4fbc7fe2c49c58fa5d.jpg",
                "cancelReviewToggle": False,
                "detail": "",
                "price": 0,
                "storeOrgIds": [
                    "800758418357149696"
                ],
                "tags": [],
                "robotRules": [
                    {
                        "type": "END",
                        "offsetTime": 600000,
                        "probability": 30,
                        "id": "813830799525076992",
                        "begintNumber": "null"
                    }
                ],
                "groupBuyEventTeamRules": [
                    {
                        "size": 3,
                        "leaderPrice": 0,
                        "memberPrice": 0,
                        "maxNumber": 22,
                        "canJoin": True,
                        "begintNumber": 0
                    }
                ],
                "stores": [

                    {
                        "name": "西城区",
                        "organizationId": "800758418357149696",
                        "longitude": "",
                        "latitude": "",
                        "address": "西城区",
                        "tel": "",
                        "length": "null"
                    }
                ],
                "createdTime": 1614073982000,
                "updatedTime": 1614079695000,
                "enable": True,
                "teamLastTimeHours": 0,
                "teamLastTimeType": "LIMITLESS",
                "repeatJoin": False,
                "effectiveEndTime": 1611590400000,
                "effectiveBeginTime": 1611072000000,
                "teamStatus": "null",
                "teamLeader": "null",
                "payCountdown": 0,
                "studentCanJoin": True,
                "trainingClassId": "null",
                "eventCategorySecondId": "",
                "eventCategoryFirstId": "754008091141341184",
                "eventCategorySecondIdName": "",
                "eventCategoryFirstIdName": "测试",
                "guideImage": "https://apex-mini-dev.oss-cn-shanghai.aliyuncs.com/null/d53890f3a2d74e38ae521dcac2d13de4.jpg",
                "remindHours": 1,
                "remindTimeType": "BEGIN",
                "checkinQrcodeToggle": False
            },
        }
        return self.send(data)

    def list_group_buy_event(self, titile):
        # 查询拼课团列表
        data = {
            "method": "get",
            "url": "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event/list",
            "headers": {'X-Token': self.token},
            "params": {
                "page": 1,
                "limit": 20,
                "size": 10,
                "searchWord": titile,
                "eventSearchVO": "%7B%7D"
            }

        }
        return self.send(data)

    def delete_update_group_buy_event(self, group_buy_event_id):
        # 删除一个拼课团
        data = {
            "method": "DELETE",
            "url": "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event/" + group_buy_event_id,
            "headers": {'X-Token': self.token},
            "data": {}
        }
        return self.send(data)

    def add_group_buy_event_specification_detail(self):
        # 为某一个拼课团关联课程班级 拼课团名称：取消订单测试
        data = {
            "method": "PUT",
            "url": "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event/813791300195639296/specification",
            "headers": {
                'X-Token': self.token,
                'Content-Type': 'application/json;charset=UTF-8'
            },
            "json": {
                "groupBuyEventSpecificationDetails": [
                    {
                        "values": "语文,数学",
                        "enabled": True,
                        "orderNo": 0,
                        "trainingClassId": "699287789878902784",
                        "trainingClassName": "励暑语2"
                    },
                    {
                        "values": "语文,英语",
                        "enabled": False,
                        "orderNo": 1,
                        "trainingClassId": "",
                        "trainingClassName": ""
                    },
                    {
                        "values": "数学,数学",
                        "enabled": True,
                        "orderNo": 2,
                        "trainingClassId": "",
                        "trainingClassName": ""
                    },
                    {
                        "values": "数学,英语",
                        "enabled": True,
                        "orderNo": 3,
                        "trainingClassId": "",
                        "trainingClassName": ""
                    }
                ],
                "specificationConfs": [
                    {
                        "level": 1,
                        "name": "一年级",
                        "values": "语文,数学"
                    },
                    {
                        "level": 2,
                        "name": "二年级",
                        "values": "数学,英语"
                    }
                ]
            }
        }
        return self.send(data)

    def copy_group_buy_event(self, group_buy_event_id):
        data = {
            "method": "PUT",
            "url": "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event/" + group_buy_event_id + "/copy",
            "headers": {'X-Token': self.token},
            "data": {}
        }
        return self.send(data)

    def enable_group_buy_event(self, group_buy_event_id, enable):
        # 撤销和发布一个拼课团
        data = {
            "method": "PUT",
            "url": "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event/" + group_buy_event_id + "/enable",
            "headers": {'X-Token': self.token},
            "data": {"enable": enable}
        }
        return self.send(data)

    def recommend_group_buy_event(self, group_buy_event_id, recommend):
        # 移除和置顶一个拼课团，recommend字段控制
        data = {
            "method": "PUT",
            "url": "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event/" + group_buy_event_id + "/recommend",
            "headers": {'X-Token': self.token},
            "data": {"recommend": recommend}
        }
        return self.send(data)

    def find_team_group_buy_event(self, group_buy_event_id):
        # 查看单个拼课团的参团列表
        data = {
            "method": "get",
            "url": "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event_order/teams",
            "headers": {'X-Token': self.token},
            "params": {
                "page": 1,
                "limit": 20,
                "size": 10,
                "groupBuyEventId": group_buy_event_id
            }
        }
        return self.send(data)

    def find_teamnumber_group_buy_event(self, group_buy_event_id):
        # 查看拼课团的参团成员
        data = {
            "method": "get",
            "url": "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event_order/event_rule/numbers",
            "headers": {'X-Token': self.token},
            "params": {
                "groupBuyEventId": group_buy_event_id
            }
        }
        return self.send(data)

    def excel_teamnumber_group_buy_event(self, group_buy_event_id, status):
        data = {
            "method": "get",
            "url": "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event_order/excel_teams",
            "headers": {'X-Token': self.token, 'Content-Type': 'text/plain;charset=UTF-8'},
            "params": {
                "status": status,
                "groupBuyEventId": group_buy_event_id
            }
        }
        return self.send(data)

    def channel_list_group_buy_event(self):
        data = {
            "method": "get",
            "url": "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/channel/list",
            "headers": {'X-Token': self.token, 'Content-Type': 'application/json;charset=UTF-8'},
            "params": {
                "page": 1,
                "size": 100, }
        }
        return self.send(data)

    def store_list_group_buy_event(self):
        data = {
            "method": "get",
            "url": "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/organizations/store_list",
            "headers": {'X-Token': self.token, 'Content-Type': 'application/json;charset=UTF-8'},
            "params": {
                "page": 1,
                "size": 100, }
        }
        return self.send(data)

    def url_list_excel_group_buy_event(self, group_buy_event_id):
        data = {
            "method": "post",
            "url": "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event/url_list_excel",
            "headers": {'X-Token': self.token, 'Content-Type': 'application/json;charset=UTF-8'},
            "json": {
                "page": 1,
                "size": 10,
                "channelIds": [],
                "groupBuyEventId": group_buy_event_id,
                "orgIds": []
            }
        }
        return self.send(data)

    def add_launch_group_buy_event(self, channelIds, group_buy_event_id, organizationId):
        data = {
            "method": "post",
            "url": "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event/launch",
            "headers": {'X-Token': self.token, 'Content-Type': 'application/json;charset=UTF-8'},
            "json": {
                "page": 1,
                "size": 10,
                "channelIds": [
                    channelIds
                ],
                "groupBuyEventId": group_buy_event_id,
                "orgIds": [
                    organizationId
                ]
            }
        }
        return self.send(data)

    def upload_qrcode_group_buy_event(self):
        data = {
            "method": "GET",
            "url": "https://apex-mini-dev.oss-cn-shanghai.aliyuncs.com/null/mocha_qrcode_4389708749976803471.png",
            "headers": {'X-Token': self.token},
            "params": {}
        }
        return self.send(data)

    def orders_group_buy_event(self, group_buy_event_id):
        data = {
            "method": "GET",
            "url": "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event_order/orders",
            "headers": {'X-Token': self.token},
            "params": {
                "page": 1,
                "limit": 20,
                "size": 10,
                "groupBuyEventId": group_buy_event_id,
                "keyWord": "",
                "status": "",
                "orderStatus": "",
                "pamentStatus": ""
            }
        }
        return self.send(data)

    def status_group_buy_event(self, group_buy_event_id, status):
        data = {
            "method": "GET",
            "url": "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event_order/search",
            "headers": {'X-Token': self.token},
            "params": {
                "page": 1,
                "size": 100,
                "limit": 20,
                "groupBuyEventId": group_buy_event_id,
                "keyWord": "",
                "status": status
            }
        }

        return self.send(data)

    # def __init__(self):
    #     super().__init__()
    """
    登录获取token思路，定义一个类，添加方法
    返回方法的值，定义一个类的局部变量
    局部变量的值，先为空，然后通过返回赋值取到
    token =None
    
    def __init__(self):
        token=get.token()
        
    新增拼课团之后，通过拼课团的resource_id进行编辑更新拼课团
    更新后，查询拼课团，通过断言判断更新是否成功
    断言方式：
    - for in 判断
    - jsonpath 判断 jmepath
    - assert 判断
    def add(self):
        pass
    def update(self):
        pass
    def list(self):
        tags=
        [tag for group in r.json()['tag_group']
            if group['groupname']=='python15'
            for tag in group['tag']
            if tag['name']==tag_name  ]
        assert tags!=[]    
    
    def del(self):
        pass 
    """

#     def add(self, userid, name, mobile, department, **kwargs):
#         data = {
#             "method": "post",
#             "url": "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/common/get_new_resource_id?type=pt",
#             "params": {"access_token": self.token},
#             "json": {"userid": userid,
#                      "name": name,
#                      "mobile": mobile,
#                      "department": department,
#                      **kwargs
#                      }}
#         return self.send(data)
#
#
#     def add_and_delete(self, userid, name, mobile, department, **kwargs):
#         r = self.add(userid, name, mobile, department, **kwargs)
#         errcode = r.json()['errcode']
#         # userid出现相同的时候
#         if errcode == 60102:
#             user_id = self.list(userid).json()['userid']
#             if not user_id:
#                 return ""
#             self.delete(userid)
#             self.add(userid, name, mobile, department, **kwargs)
#             result = self.list(userid).json()['userid']
#             if not result:
#                 print("add not success")
#             return result
#         # 当出现手机号相同情况
#         elif errcode == 60104:
#             # 根据错误信息返回拿到user_id
#             msg = r.json()['errmsg']
#             user = re.findall("([^:]+)$", msg)[0]
#             # 判断是否存在手机号
#             mobile = self.list(user).json()['mobile']
#             if not mobile:
#                 return ""
#             self.delete(user)
#             self.add(userid, name, mobile, department, **kwargs)
#             result = self.list(userid).json()['userid']
#             if not result:
#                 print("add not success")
#             return result
#         # 手机号和邮箱为空的情况
#         elif errcode == 60129:
#             pg = PhoneNOGenerator()
#             mobile = pg.phoneNORandomGenerator()
#             email = mobile + "@139.com"
#             self.add(userid, name, email=email, **kwargs)
#         # 当部门为空或者不存在时候
#         elif errcode == 40066:
#             print("不合法的部门列表")
#
#     def list(self, userid):
#         data = {
#             "method": "get",
#             "url": 'https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event/list?page=1&limit=20&size=10&eventSearchVO={}',
#             "params": {"X-Token": self.token, 'userid': userid},
#             "json": {
#             }
#         }
#         return self.send(data)
#
#     def update(self, userid, user_name):
#         data = {
#             "method": "post",
#             "url": 'https://qyapi.weixin.qq.com/cgi-bin/user/update',
#             "params": {"access_token": self.token},
#             "json": {"userid": userid,
#                      "name": user_name
#                      }}
#         return self.send(data)
#
#     def delete(self, userid):
#         data = {
#             "method": "get",
#             "url": 'https://qyapi.weixin.qq.com/cgi-bin/user/delete',
#             "params": {"access_token": self.token, 'userid': userid},
#             "json": {}
#         }
#         return self.send(data)
#
#     def delete_and_detect_user(self, user_ids):
#         deleted_user_ids = []
#         r = self.delete(user_ids)
#         if r.json()["errcode"] == 60111:
#             # 如果用户不存在，就添加一个用户，将它的 userid存储进来
#             for userid in user_ids:
#                 if not self.find_userid_exist(userid):
#                     user_id_tmp = self.add(userid="hechenxin", name="zy", mobile="13452808772", department=[1])
#                     deleted_user_ids.append(user_id_tmp)
#                     # 如果标签存在，就将它存入标签组
#                 else:
#                     deleted_user_ids.append(userid)
#
#         elif r.json()["errcode"] == 301005:
#             # 当用户id为本人时，不允许删除
#             print("不允许删除创建者")
#         r = self.delete(deleted_user_ids)
#         return r
#
#     def find_userid_exist(self, user_id):
#         # 查询用户id是否存在，如果不存在，报错
#         user = self.list(user_id).json()["errmsg"]
#         if 'userid not found' == user:
#             return ""
#
#     def get_partyid(self, par_id=None):
#         # par_id 为空时，获取所有部门信息
#         data = {"method": "post",
#                 "url": "https://qyapi.weixin.qq.com/cgi-bin/department/list",
#                 "params": {"access_token": self.token, "id": par_id}}
#         return self.send(data)
#
#
# class PhoneNOGenerator():
#     # 随机生成手机号码
#     def phoneNORandomGenerator(self):
#         prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
#                    "153", "155", "156", "157", "158", "159", "186", "187", "188"]
#         return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))
