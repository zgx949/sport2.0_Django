from django.contrib import admin
from .models import *

# Register your models here.

admin.site.site_header = 'BOOM赛事管理管理后台'  # 设置header
admin.site.site_title = 'BOOM赛事管理管理后台'  # 设置title
admin.site.index_title = 'BOOM赛事管理管理后台'


class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'data')


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'gender', 'institution')
    search_fields = ('username', 'name')
    list_filter = ('gender', 'institution')


class GameAdmin(admin.ModelAdmin):
    list_display = ('type', 'gender', 'name', 'game_type', 'status', 'start_time', 'end_time')
    list_filter = ('game_type', 'gender', 'status', 'start_time', 'end_time', 'type')
    search_fields = ['name']
    list_editable = ['status', 'end_time']


class enrollAdmin(admin.ModelAdmin):
    # list_display = ('gametype', 'username', 'player', 'institution', 'gender', 'game', 'create_time')
    list_display = (
        'gametype', 'username',
        'player', 'institution',
        'gender', 'game', 'unit',
        'score', 'finall_game',
        'finall_score', 'create_time'
    )
    list_filter = ['game__type', 'player__gender', 'game', 'finall_game', 'player__institution', 'create_time']
    search_fields = ['player__name', 'player__username']
    list_editable = ('finall_game', 'score', 'finall_score')

    # actions = ['custom_button']
    #
    # def custom_button(self, request, queryset):
    #     queryset.update(game_type=2)

    # custom_button.short_description = '修改为决赛'
    # custom_button.type = 'primary'

    def gametype(self, obj):
        """
        写方法查询比赛类型
        :param obj:
        :return game_type:
        """
        return obj.game.type

    gametype.short_description = "赛事类型"

    def username(self, obj):
        """
        写方法查询运动员学号
        :param obj:
        :return game_type:
        """
        return obj.player.username

    username.short_description = "学号"

    def institution(self, obj):
        """
        写方法查询学院名称
        :param obj:
        :return instution_name:
        """
        return obj.player.institution.name

    institution.short_description = "学院"

    def gender(self, obj):
        """
        写方法查询运动员性别
        :param obj:
        :return player_gender:
        """
        return obj.player.get_gender_display()

    gender.short_description = "性别"

    def unit(self, obj):
        return obj.game.unit

    unit.short_description = "单位"


# class ScoreAdmin(admin.ModelAdmin):
#     # list_display = ('username', 'player', 'game', 'score', 'unit', 'create_time')
#     list_display = ('username',)
#
#     def username(self, obj):
#         """
#         写方法查询运动员学号
#         :param obj:
#         :return game_type:
#         """
#         return obj.enroll_set.all()
#
#     username.short_description = "学号"

# def unit(self, obj):
#     return obj.game.unit
#
# unit.short_description = "成绩单位"
#
# def institution(self, obj):
#     """
#     写方法查询学院名称
#     :param obj:
#     :return instution_name:
#     """
#     return obj.player.institution.name
#
# institution.short_description = "学院"
#
# def gametype(self, obj):
#     """
#     写方法查询比赛类型
#     :param obj:
#     :return game_type:
#     """
#     return obj.game.type
#
# gametype.short_description = "赛事类型"


# class ScoreAdmin(admin.ModelAdmin):
#     list_display = ('gametype', 'username', 'player', 'institution', 'game', 'score', 'unit', 'create_time')
#     search_fields = ['player__name', 'player__username']
#     list_filter = ['game__type', 'player__gender', 'game', 'player__institution', 'create_time']
#     actions = ['make_published']
#
#     def make_published(self, request, queryset):
#         print(request, queryset)
#         return "那么"
#
#     make_published.short_description = "进入决赛"
#
#     def username(self, obj):
#         """
#         写方法查询运动员学号
#         :param obj:
#         :return game_type:
#         """
#         return obj.player.username
#
#     username.short_description = "学号"
#
#     def unit(self, obj):
#         return obj.game.unit
#
#     unit.short_description = "成绩单位"
#
#     def institution(self, obj):
#         """
#         写方法查询学院名称
#         :param obj:
#         :return instution_name:
#         """
#         return obj.player.institution.name
#
#     institution.short_description = "学院"
#
#     def gametype(self, obj):
#         """
#         写方法查询比赛类型
#         :param obj:
#         :return game_type:
#         """
#         return obj.game.type
#
#     gametype.short_description = "赛事类型"


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_time')
    search_fields = ('title', 'content')
    list_filter = ('create_time',)
    # list_editable = ('content',)


class ComplaintAdmin(admin.ModelAdmin):
    search_fields = ('contact', 'content')
    list_display = ('contact', 'content', 'create_time')


admin.site.register(Institution, InstitutionAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(enroll, enrollAdmin)
# admin.site.register(Score, ScoreAdmin)

admin.site.register(News, NewsAdmin)
admin.site.register(Complaint, ComplaintAdmin)
