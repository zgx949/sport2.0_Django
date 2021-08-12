import json


class Common_result:
    def __init__(self, data):
        """
        初始化data
        :param data: List或Dict 数据库数据
        """
        self.data = data

    def success(self):
        """
        成功返回的json
        :return: String 编码后的json字符串
        """
        return json.dumps(
            {
                'msg': '操作成功',
                'code': 1,
                'data': self.data
            }
        )

    def error(self):
        """
        错误返回的json
        :return:
        """
        self.data = []
        return json.dumps(
            {
                'msg': '非法操作',
                'code': 0,
                'data': self.data
            }
        )
