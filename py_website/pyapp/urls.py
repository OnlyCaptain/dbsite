"""定义db_app的URL模式"""


from django.conf.urls import url
from . import views
from django.conf.urls import include


urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),

    url(r'^index/$', views.index, name='index'),

    url(r'^login/$', views.login, name='login'),

    url(r'^logout/$', views.logout, name='logout'),

    # 显示所有 questions
    url(r'^questions/$', views.questions, name='questions'),

    url(r'^register/$', views.register, name='register'),

    url(r'^confirm/$', views.confirm, name='confirm'),

    url(r'^questions/(?P<question_id>\d+)/$', views.question, name='question'),
]
