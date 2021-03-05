from base_api import BaseApi


class Huodongyuyue(BaseApi):
    def __init__(self):
        super().__init__()

    def add(self, type):
        data = {
            "method": "get",
            "url": "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/common/get_new_resource_id",
            "params": {"type": type},
            "headers": {'X-Token': self.token}
        }
        return self.send(data)

    def update_event(self, event_id, resourceId, name):
        # 更新活动
        data = {
            "method": "put",
            "url": "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/event/" + event_id,
            "headers": {
                'X-Token': self.token,
                'Content-Type': 'application/json;charset=UTF-8'
            },
            "json": {
                "shareImageUrl": "null",
                "customerServerShowVO": {
                    "title": "",
                    "image": "",
                    "iconName": "",
                    "status": False
                },
                "customerServerGuideOpened": False,
                "fissionPosterUrl": "null",
                "hasFissionPoster": "null",
                "shareId": "null",
                "organizationId": "587357539759292416",
                "resourceId": resourceId,
                "brief": "null",
                "name": name,
                "banner": "null",
                "published": False,
                "chargedAmount": 0,
                "reservationReviewToggle": False,
                "cancelReviewToggle": False,
                "chargeToggle": True,
                "createdTime": 1614925860000,
                "coverImage": "null",
                "detail": "",
                "form": "[]",
                "id": "817403833122086912",
                "eventSessionList": [
                    {
                        "id": "817403833151447040",
                        "startTime": 1603696130000,
                        "endTime": 1604073600000,
                        "quota": "null",
                        "createdTime": 0,
                        "address": "",
                        "placeType": "STORE",
                        "applicableStoreIds": "768419663792685056,768419724291325952,768419758852390912,768419795774849024,768419885767835648,768419937961754624,768419964918546432,768419983163768832,768420112813899776,768420240182329344,768420307354107904,768573611400871936,768574015970852864",
                        "seatsLeft": 100,
                        "latitude": "null",
                        "longitude": "null",
                        "applicableStoreCount": 0
                    }
                ],
                "beginTime": 1603641600000,
                "lastTime": 1604073600000,
                "tags": [

                ],
                "hasOrder": "null",
                "orderId": "null",
                "smsTemplateId": "",
                "couponBatch": "",
                "status": "CLOSED",
                "endTime": 1604073600000,
                "eventCategorySecondId": "",
                "eventCategoryFirstId": "767799481818927104",
                "eventCategorySecondIdName": "",
                "eventCategoryFirstIdName": "活动类目-lu",
                "applicableStoreIds": "768420307354107904,768419758852390912,768420240182329344,768573611400871936,768419795774849024,768419937961754624,768419724291325952,768574015970852864,768419885767835648,768419983163768832,768420112813899776,768419663792685056,768419964918546432",
                "applicableStoreCount": 13,
                "storeVo": {
                    "name": " ",
                    "organizationId": "768420307354107904",
                    "longitude": "",
                    "latitude": "",
                    "address": "啊范德萨",
                    "tel": "",
                    "length": 0
                },
                "guideImage": "",
                "checkinQrcodeToggle": False
            },
        }
        return self.send(data)

    def list_event(self, name):
        # 查询活动列表
        data = {
            "method": "get",
            "url": "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/event/list",
            "headers": {'X-Token': self.token},
            "params": {
                "page": 1,
                "limit": 20,
                "size": 10,
                "searchWord": name,
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

    def copy_event(self, event_id):
        data = {
            "method": "PUT",
            "url": "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/event/" + event_id + "/copy",
            "headers": {'X-Token': self.token},
            "data": {}
        }
        return self.send(data)

    def publish_event(self, event_id, publish):
        # 撤销和发布一个活动
        data = {
            "method": "PUT",
            "url": "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/event/" + event_id + "/publish",
            "headers": {'X-Token': self.token},
            "data": {"publish": publish}
        }
        return self.send(data)

    def recommend_event(self, event_id, recommend):
        # 移除和置顶一个活动，recommend字段控制
        data = {
            "method": "PUT",
            "url": "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/event/" + event_id + "/recommend",
            "headers": {'X-Token': self.token},
            "data": {"recommend": recommend}
        }
        return self.send(data)

    def find_get_order_list_event(self, event_id):
        # 查看单个活动的参团列表
        """
        "json": {
                "channel": "微信",
                "orderStatus": "UNPAID",
                "pamentStatus": "UNPAID",
                "storeOrgIds": ["768419663792685056"],
                "keyWord":"150"
            }
        :param event_id:
        :return:
        """
        # https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/event_orders/get_order_list
        data = {
            "method": "post",
            "url": "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/event_orders/get_order_list",
            "headers": {'X-Token': self.token},
            "params": {
                "page": 1,
                "size": 10,
                "eventId": event_id
            },
            "json": {

                "storeOrgIds": []

            }

        }
        return self.send(data)

    def find_teamnumber_event(self, event_id, status):
        data = {
            "method": "get",
            "url": "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/event_orders/search",
            "headers": {'X-Token': self.token},
            "params": {
                "page": 1,
                "size": 20,
                "limit": 20,
                "event_id": event_id,
                "keyWord": "",
                "status": status

            }
        }
        return self.send(data)

    def find_event_checkin_qrcode(self, event_id):
        # https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/event_checkin_qrcode/list?page=1&size=20
        data = {
            "method": "post",
            "url": "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/event_checkin_qrcode/list",
            "headers": {'X-Token': self.token, 'Content-Type': 'application/json;charset=UTF-8'},
            "params": {
                "page": 1,
                "size": 20
            },
            "json": {
                "page": 1,
                "limit": 20,
                "size": 20,
                "eventId": event_id,
                "storeOrgIds": []
            }
        }
        return self.send(data)

    def canceled_event(self, event_id):
        data = {
            "method": "PUT",
            "url": "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/event_orders/" + event_id + "/canceled",
            "headers": {'X-Token': self.token},
            "data": {}
        }
        return self.send(data)
