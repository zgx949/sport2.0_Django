from django.shortcuts import render
from django.http import HttpResponse
import datetime
import json

from sportmeeting.models import *


class api:
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
        return HttpResponse(json.dumps(
            {
                'msg': '操作成功',
                'code': 1,
                'data': self.data
            }
        ),
            content_type="application/json"
        )

    def error(self):
        """
        错误返回的json
        :return:
        """
        return HttpResponse(json.dumps(
            {
                'msg': '非法操作',
                'code': 0,
                'data': self.data
            }
        ),
            content_type="application/json"
        )


def current_datetime():
    return str(datetime.datetime.now())[:-7]


# Create your views here.

def login(request):
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            username = json_data['username']
            password = json_data['password']
        except:
            return api({'msg': 'json格式不正确'}).error()

        try:
            user = Player.objects.get(username=username)
            if user.password == password:
                return api({'uname': user.username, 'pwd': user.password, 'uid': user.id, "name": user.name, "gender": user.gender}).success()
            else:
                return api('密码错误').error()


        except Exception as e:
            return api('账号未注册').error()

    return api('must be post').error()


def register(request):
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            username = json_data['username']
            password = json_data['password']
            name = json_data['name']
            gender = json_data['gender']
            institutionid = json_data['institutionid']
        except:
            return api({'msg': 'json格式不正确'}).error()

        if Player.objects.filter(username=username).exists():
            return api('账号已存在').error()
        else:
            try:
                Player.objects.create(
                    username=username,
                    password=password,
                    name=name,
                    gender=gender,
                    institution_id=institutionid
                )
                return api('注册成功').success()
            except Exception as e:
                return api(e).error()
    else:
        return api([]).error()


def institutions(request):
    if request.method == 'GET':
        ins_id = request.GET.get('id', '')
        if ins_id == '':
            ins = Institution.objects.all()
            datalist = []
            for item in ins:
                datalist.append({'id': item.id, 'name': item.name})
            return api(datalist).success()
        else:
            ins = Institution.objects.filter(id=ins_id)
            datalist = []
            for item in ins:
                datalist.append({'id': item.id, 'name': item.name})
            return api(datalist).success()


def games(request):
    if request.method == 'GET':
        game_id = request.GET.get('id', '')
        if game_id == '':
            ins = Game.objects.all()
            datalist = []
            for item in ins:
                datalist.append(
                    {'id': item.id,
                     'name': item.name,
                     'game_type': item.game_type,
                     'type': item.type,
                     'gender': item.gender,
                     'unit': item.unit,
                     'data': item.data,
                     'status': item.status,
                     'start_time': str(item.start_time)[:-6],
                     'end_time': str(item.end_time)[:-6]
                     }
                )
            return api(datalist).success()
        else:
            ins = Game.objects.filter(id=game_id)
            datalist = []
            for item in ins:
                datalist.append(
                    {'id': item.id,
                     'name': item.name,
                     'type': item.type,
                     'gender': item.gender,
                     'unit': item.unit,
                     'data': item.data,
                     'status': item.status,
                     'start_time': str(item.start_time)[:-6],
                     'end_time': str(item.end_time)[:-6]
                     }
                )
            return api(datalist).success()


def enroll_model(request):
    if request.method == 'GET':
        enroll_id = request.GET.get('id', '')
        if enroll_id == '':
            items = enroll.objects.all()
            datalist = []
            for item in items:
                datalist.append(
                    {'id': item.id,
                     'name': item.player.name,
                     'institution': item.player.institution.name,
                     'gameid': item.game.id,
                     'game_name': item.game.name,
                     # 'finall_gameid': item.finall_game.id,
                     # 'finall_game': item.finall_game.name,
                     'gender': item.game.gender,

                     }
                )
            return api(datalist).success()
        else:
            ins = enroll.objects.filter(id=enroll_id)
            datalist = []
            for item in ins:
                datalist.append(
                    {'id': item.id,
                     'name': item.player.name,
                     'institution': item.player.institution.name,
                     'game_name': item.game.name,
                     'gender': item.game.gender,
                     'gameid': item.game.id,
                     }
                )
            return api(datalist).success()
    else:
        try:
            json_data = json.loads(request.body)
            username = json_data['username']
            password = json_data['password']
            gameId = json_data['gameId']
            enroll.objects.create(
                player=Player.objects.get(username=username, password=password),
                game=Game.objects.get(id=gameId),
                finall_game=Game.objects.get(id=3),
            )
            return api({'msg': '报名成功'}).success()
        except:
            return api({'msg': 'json格式不正确'}).error()


def complain(request):
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            contact = json_data['contact']
            content = json_data['content']
        except:
            return api({'msg': 'json格式不正确'}).error()
        try:
            Complaint.objects.create(
                contact=contact,
                content=content
            )
            return api({'msg': '投诉提交成功'}).success()
        except:
            return api({'msg': '投诉提交错误'}).error()
    else:
        return api({'msg': '投诉提交错误'}).error()


def news(request):
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            title = json_data['title']
            content = json_data['content']
        except:
            return api({'msg': 'json格式不正确'}).error()
        try:
            News.objects.create(
                title=title,
                content=content,
            )
            return api({'msg': '提交成功'}).success()
        except:
            return api({'msg': '投诉错误'}).error()
    else:
        news_id = request.GET.get('id', '')
        if news_id == '':
            items = News.objects.all()
            datalist = []
            for item in items:
                datalist.append(
                    {'id': item.id,
                     'title': item.title,
                     'content': item.content,
                     'create_time': str(item.create_time)[:10]
                     }
                )
            return api(datalist).success()
        else:
            items = News.objects.filter(id=news_id)
            datalist = []
            for item in items:
                datalist.append(
                    {'id': item.id,
                     'title': item.title,
                     'content': item.content,
                     'create_time': str(item.create_time)[:10]
                     }
                )
            return api(datalist).success()


def player(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        try:
            playerobj = Player.objects.get(username=username)
        except:
            return api("查无此用户").error()
        items = playerobj.enroll_set.all()
        data = []
        for item in items:
            data.append(
                {
                    "gameid": item.id,
                    "game": str(item.game),
                    "finall_gameid": str(item.finall_game.id),
                    "finall_game": str(item.finall_game),
                    "uid": item.player.id,
                    "name": item.player.name,
                    "institution": item.player.institution.name


                }
            )
        return api(data).success()
