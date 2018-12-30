"""定义db_app的URL模式"""


from django.conf.urls import url
from . import views
from django.conf.urls import include


urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),

    # 主页
    url(r'^index/$', views.index, name='index'),

    # 登录界面
    url(r'^login/$', views.login, name='login'),

    # 登出操作
    url(r'^logout/$', views.logout, name='logout'),

    # 显示所有 questions
    url(r'^questions/$', views.questions, name='questions'),

    # 查看某个具体的问题以及对问题的回答
    url(r'^questions/(?P<question_id>\d+)/$', views.question, name='question'),

    # 注册界面
    url(r'^register/$', views.register, name='register'),

    # 注册界面成功后的页面跳转，延迟等待
    url(r'^confirm/$', views.confirm, name='confirm'),
]
