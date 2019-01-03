# -*- coding:utf-8 -*-
from django.conf.urls import  url
from . import views

urlpatterns = [
    url(r'^$', views.task_list, name='task_list'),
    url(r'^tasks/$', views.task_list, name='task_list'),
    url(r'^questions/$', views.question_list, name='question_list'),
    url(r'^questions/(?P<question_id>[0-9]+)$', views.question_detail, name='question_detail'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    # url(r'^tasks/$', views.TaskList.as_view(), name='task_list'),
    # url(r'^tasks/$', views.TaskListCreate.as_view(), name='task_list'),
    url(r'^tasks/(?P<pk>[0-9]+)$', views.task_detail, name='task_detail'),
]