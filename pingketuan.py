import random
import re

from address_list.base_api import BaseApi


class PhoneNOGenerator():
    # 随机生成手机号码
    def phoneNORandomGenerator(self):
        prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
                   "153", "155", "156", "157", "158", "159", "186", "187", "188"]
        return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))


class Pingketuan(BaseApi):
    def __init__(self):
        super().__init__()

    def add(self, userid, name, mobile, department, **kwargs):
        data = {
            "method": "post",
            "url": "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/common/get_new_resource_id?type=pt",
            "params": {"access_token": self.token},
            "json": {"userid": userid,
                     "name": name,
                     "mobile": mobile,
                     "department": department,
                     **kwargs
                     }}
        return self.send(data)

    def test_add_group_buy_event():
        url = "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/common/get_new_resource_id?type=pt"
        payload = {}
        headers = {
            'X-Token': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI3MDAwMzUwNTMyNTM1NTgyNzIifQ.RhXY4Sz6ayef5L-eKY9ja_gBfCnQu3D-2B9napSul2M'
        }

        r = requests.get(url, headers=headers, data=payload)

        print(r.text)
        print(json.dumps(r.json(), indent=2))
        print(r.json()['data'])
        assert r.status_code == 200
        resource_id = r.json()['data']
        return resource_id

    def add_and_delete(self, userid, name, mobile, department, **kwargs):
        r = self.add(userid, name, mobile, department, **kwargs)
        errcode = r.json()['errcode']
        # userid出现相同的时候
        if errcode == 60102:
            user_id = self.list(userid).json()['userid']
            if not user_id:
                return ""
            self.delete(userid)
            self.add(userid, name, mobile, department, **kwargs)
            result = self.list(userid).json()['userid']
            if not result:
                print("add not success")
            return result
        # 当出现手机号相同情况
        elif errcode == 60104:
            # 根据错误信息返回拿到user_id
            msg = r.json()['errmsg']
            user = re.findall("([^:]+)$", msg)[0]
            # 判断是否存在手机号
            mobile = self.list(user).json()['mobile']
            if not mobile:
                return ""
            self.delete(user)
            self.add(userid, name, mobile, department, **kwargs)
            result = self.list(userid).json()['userid']
            if not result:
                print("add not success")
            return result
        # 手机号和邮箱为空的情况
        elif errcode == 60129:
            pg = PhoneNOGenerator()
            mobile = pg.phoneNORandomGenerator()
            email = mobile + "@139.com"
            self.add(userid, name, email=email, **kwargs)
        # 当部门为空或者不存在时候
        elif errcode == 40066:
            print("不合法的部门列表")

    def list(self, userid):
        data = {
            "method": "get",
            "url": 'https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event/list?page=1&limit=20&size=10&eventSearchVO={}',
            "params": {"X-Token": self.token, 'userid': userid},
            "json": {
            }
        }
        return self.send(data)

    def test_find_group_buy_event():
        url = "https://apex-test-zhuoyue-mini-admin.chinapex.com.cn/dab/group_buy_event/list?page=1&limit=20&size=10&eventSearchVO={}"
        payload = {}
        r = requests.get(url,
                         headers={
                             'Content-Type': 'application/json;charset=UTF-8',
                             'X-Token': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI3MDAwMzUwNTMyNTM1NTgyNzIifQ.RhXY4Sz6ayef5L-eKY9ja_gBfCnQu3D-2B9napSul2M'
                         },
                         data=payload,
                         verify=False)

    def update(self, userid, user_name):
        data = {
            "method": "post",
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/user/update',
            "params": {"access_token": self.token},
            "json": {"userid": userid,
                     "name": user_name
                     }}
        return self.send(data)

    def delete(self, userid):
        data = {
            "method": "get",
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/user/delete',
            "params": {"access_token": self.token, 'userid': userid},
            "json": {}
        }
        return self.send(data)

    def delete_and_detect_user(self, user_ids):
        deleted_user_ids = []
        r = self.delete(user_ids)
        if r.json()["errcode"] == 60111:
            # 如果用户不存在，就添加一个用户，将它的 userid存储进来
            for userid in user_ids:
                if not self.find_userid_exist(userid):
                    user_id_tmp = self.add(userid="hechenxin", name="zy", mobile="13452808772", department=[1])
                    deleted_user_ids.append(user_id_tmp)
                    # 如果标签存在，就将它存入标签组
                else:
                    deleted_user_ids.append(userid)

        elif r.json()["errcode"] == 301005:
            # 当用户id为本人时，不允许删除
            print("不允许删除创建者")
        r = self.delete(deleted_user_ids)
        return r

    def find_userid_exist(self, user_id):
        # 查询用户id是否存在，如果不存在，报错
        user = self.list(user_id).json()["errmsg"]
        if 'userid not found' == user:
            return ""

    def get_partyid(self, par_id=None):
        # par_id 为空时，获取所有部门信息
        data = {"method": "post",
                "url": "https://qyapi.weixin.qq.com/cgi-bin/department/list",
                "params": {"access_token": self.token, "id": par_id}}
        return self.send(data)