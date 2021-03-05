from base_api import BaseApi


# done 封装代码，去除冗余代码
class Huodongyuyue(BaseApi):
    # 方式一放到类里：token= None
    # 先获取token
    def __init__(self):
        super().__init__()

    def update_event(self, event_id, resourceId, titile):
        # 更新活动
        data = {
            "method": "put",
            "url": "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/event/" + event_id,
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

    def list_event(self, titile):
        # 查询活动列表
        data = {
            "method": "get",
            "url": "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/event/list",
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

    def delete_update_event(self, event_id):
        # 删除一个活动
        data = {
            "method": "DELETE",
            "url": "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/event/" + event_id,
            "headers": {'X-Token': self.token},
            "data": {}
        }
        return self.send(data)