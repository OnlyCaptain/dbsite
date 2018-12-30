"""定义db_app的URL模式"""


from django.conf.urls import url
from . import views


urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),

    # 显示所有topic
    # url(r'^topics/$', views.topics, name='topics'),

    # 显示所有 questions
    url(r'^questions/$', views.questions, name='questions'),

    # 显示特定topic的详细页面
    # url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    url(r'^questions/(?P<question_id>\d+)/$', views.question, name='question'),
]
