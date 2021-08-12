import requests
import random
import json

first_name = ["王", "李", "张", "刘", "赵", "蒋", "孟", "陈", "徐", "杨", "沈", "马", "高", "殷", "上官", "钟", "常"]
second_name = ["伟", "华", "建国", "洋", "刚", "万里", "爱民", "牧", "陆", "路", "昕", "鑫", "兵", "硕", "志宏", "峰", "磊", "雷", "文", "明浩",
               "光", "超", "军", "达"]
for i in range(100):
    name = random.choice(first_name) + random.choice(second_name)
    num = str(random.randint(1111111, 2222222))
    data = {
        "username": num,
        "password": "zxczxc",
        "name": name,
        "gender": random.randint(0, 1),
        "institutionid": 1
    }
    respon = requests.post(url="http://127.0.0.1:8000/register", data=json.dumps(data))
    if respon:
        print(respon.json())
