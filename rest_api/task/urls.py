# -*- coding:utf-8 -*-
from django.conf.urls import  url
from . import views

urlpatterns = [
    url(r'^$', views.question_list, name='task_list'),
    # url(r'^tasks/$', views.task_list, name='task_list'),
    url(r'^questions/$', views.question_list, name='question_list'),
    url(r'^questions/(?P<question_id>[0-9]+)$', views.question_detail, name='question_detail'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),

    url(r'^answers/(?P<question_id>[0-9]+)$', views.answer_list, name='answer_list'),
    url(r'^answers/(?P<question_id>[0-9]+)/(?P<answer_id>[0-9]+)$', 
        views.answer_detail, name='answer_detail'),
]