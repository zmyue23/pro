import requests
from fofa import settings

class Message(object):
    """封装单条短信发送的接口"""

    def __init__(self, api_key):
        self.api_key = api_key  # 账户的唯一标识
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_message(self, mobile, code):
        """实现短信发送的逻辑"""
        param = {
            "apikey": self.api_key,
            "mobile": mobile,
            # code短信验证码需要随机生成
            # text必须与已审核通过的模板保持一致
            "text": "【张名悦】正在进行登录操作，您的验证码是{code}".format(code=code)
        }

        req = requests.post(self.single_send_url, data=param)
        print(req)


# if __name__ == '__main__':
    # msg = Message(settings.API_KEY)
    # msg.send_message("18475638396", "888888")
