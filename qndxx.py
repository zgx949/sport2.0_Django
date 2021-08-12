import time
import pymysql
import re
from multiprocessing import Pool
import requests
from urllib import parse
from json import dumps


def do_work(url):

    respon = requests.get(url)
    openid = parse.unquote(re.findall("userId=(.*?)&", url)[0])
    if respon:
        cookies = respon.cookies
        html = respon.text
        name = re.findall("name:\"(.*?)\"", html)[0]
        sign = re.findall("sign:\"(.*?)\"", html)[0]
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Content-Type': 'application/json;charset=utf-8',
            'Origin': 'http://onestop.jxufe.edu.cn',
            'Connection': 'keep-alive',
            'Referer': url,
        }
        data = {
            "orgid": "50",
            "urlStr": "http://def.yigao0792.com/1/jxufe/save.php",
            "openid": openid,
            "name": name,
            "nickname": "",
            "sex": "",
            "province": "江西省",
            "city": "南昌市",
            "headimgurl": "",
            "sign": sign,
            "timestamp": str(int(time.time())),
            "rectime": str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        }

        result = requests.post(url='http://onestop.jxufe.edu.cn/eos/wx/youthStudy/eos/com.lantuo.bps.youthStudy.stwhttp.biz.ext',
                               data=dumps(data),
                               cookies=cookies,
                               headers=headers)
        if result:
            print(result.json()['result'])


db = pymysql.connect(
    host='zswk.xyz',
    user='qndxx',
    password='qndxx',
    database='qndxx'
)

cursor = db.cursor()
cursor.execute("select * from user")
data = cursor.fetchall()

if __name__ == '__main__':
    url_list = []
    s = time.time()
    for cardnum, name, institution, url in data:
        # do_work(url)
        url_list.append(url)

    pool = Pool(30)
    pool.map_async(do_work, url_list)
    pool.close()
    pool.join()

    db.close()
    print("任务完成！总耗时：", time.time() - s, "秒")
