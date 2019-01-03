# -*- coding:utf-8 -*-
from rest_framework import serializers
from .models import User, Answer, Question, QuestionToUser, UserFocusQuestion


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'UserName', 'Password')

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'AnswerWords', 'AnswerOwner', 'AnswerToQuestion', 'date_added')

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'Description', 'date_added')

class UserFocusQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFocusQuestion
        fields = ('id', 'QuestionID', 'UserID')
