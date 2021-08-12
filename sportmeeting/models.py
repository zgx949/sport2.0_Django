from django.db import models
from mdeditor.fields import MDTextField


# Create your models here.
class Institution(models.Model):
    # id = models.IntegerField(verbose_name='学院id', primary_key=True, auto_created=True)
    name = models.CharField(verbose_name='学院名称', max_length=255, null=False)
    data = models.CharField(verbose_name='学院信息', max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = '学院表'

    def __str__(self):
        return self.name


class Player(models.Model):
    gender_chices = ((0, '女'), (1, '男'), (2, '未知'))

    # id = models.IntegerField(verbose_name='运动员id', primary_key=True)
    username = models.CharField(verbose_name='学号', max_length=7, null=False)
    password = models.CharField(verbose_name='密码', max_length=255, null=False)
    name = models.CharField(verbose_name='姓名', max_length=255, null=False)
    gender = models.IntegerField(verbose_name='性别', choices=gender_chices, null=False)
    institution = models.ForeignKey(Institution, null=True, on_delete=models.SET_NULL, verbose_name='学院名')
    data = models.CharField(verbose_name='数据 ', max_length=255, null=True, blank=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        verbose_name_plural = '运动员表'

    def __str__(self):
        return self.name


class Game(models.Model):
    gender_chices = ((0, '女'), (1, '男'), (2, '未知'))
    status_chices = ((0, '未开始'), (1, '检录'), (2, '结束'))
    gametype_chices = ((1, '初赛'), (2, '决赛'))

    # id = models.IntegerField(verbose_name='赛事id', primary_key=True)
    name = models.CharField(verbose_name='赛事名称', max_length=255, null=False)
    game_type = models.IntegerField(verbose_name='初预赛', choices=gametype_chices, null=False, default=1)
    type = models.CharField(verbose_name='赛事类型', max_length=255, null=False)
    gender = models.IntegerField(verbose_name='性别', choices=gender_chices, null=False)
    unit = models.CharField(verbose_name='成绩单位', max_length=255, null=False)
    status = models.IntegerField(verbose_name='状态', choices=status_chices, null=False)
    start_time = models.DateTimeField(verbose_name='开始时间')
    end_time = models.DateTimeField(verbose_name='结束时间', null=True, blank=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    data = models.CharField(verbose_name='信息', max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = '赛事表'

    def __str__(self):
        return "【" + self.get_gender_display() + "子】" + self.name + "(" + self.get_game_type_display() + ")"


# class Score(models.Model):
#     # id = models.IntegerField(verbose_name='成绩表id', primary_key=True)
#     score = models.FloatField(verbose_name='成绩', null=True)
#     create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
#
#     class Meta:
#         verbose_name_plural = '成绩表'
#
#     def __str__(self):
#         return str(self.score)


class enroll(models.Model):
    # id = models.IntegerField(verbose_name='报名表id', primary_key=True)
    player = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL, verbose_name='运动员')
    game = models.ForeignKey(Game, null=True, on_delete=models.SET_NULL, verbose_name='初赛', related_name='初赛')
    score = models.FloatField(verbose_name='初赛成绩', null=True, blank=True)

    finall_game = models.ForeignKey(Game, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='决赛',
                                    related_name='决赛')
    # finall_score = models.ForeignKey(Score, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='决赛成绩',
    #                                  related_name='决赛成绩')
    finall_score = models.FloatField(verbose_name='决赛成绩', null=True, blank=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        verbose_name_plural = '报名表'

    def __str__(self):
        return self.player.name + " 报名了: " + "【" + self.game.get_gender_display() + "子】" + self.game.name


# class Score(models.Model):
#     enroll = models.ForeignKey(enroll, verbose_name='报名表', on_delete=models.SET_NULL, null=False)
#     score = models.FloatField(verbose_name='成绩', null=True)
#     create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
#
#     class Meta:
#         verbose_name_plural = '成绩表'
#
#     def __str__(self):
#         return self.player.name + " 在" + \
#                "【" + self.game.get_gender_display() + \
#                "子】" + self.game.name + " 比赛中取得:" + str(self.score) + self.game.unit + "的成绩"


class News(models.Model):
    title = models.CharField(verbose_name='标题', max_length=255)
    content = MDTextField()
    # content = models.CharField(verbose_name='内容(Markdown)', max_length=255)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        verbose_name_plural = '新闻表'

    def __str__(self):
        return self.title


class Complaint(models.Model):
    contact = models.CharField(verbose_name='联系方式', max_length=255)
    content = models.CharField(verbose_name='投诉内容', max_length=255)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        verbose_name_plural = '投诉表'

    def __str__(self):
        return self.content
