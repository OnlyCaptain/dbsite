#-*- coding=utf-8 -*-
# from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .models import User, Question, Answer
from .serializers import UserSerializer, QuestionSerializer, AnswerSerializer

import hashlib
from django.db import transaction

def hash_code(s, salt='captainsite'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()

@api_view(['POST'])
@transaction.atomic
def login(request):
    '''
    Login logic
    '''
    # print(request.data)
    # print("hello world")
    if request.method == 'POST':
        '''设置保存点用于事务管理'''
        sid1 = transaction.savepoint()
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data['UserName']
            password = serializer.data['Password']
            try:
                user = User.objects.get(UserName=name)
            except:
                message = 'No this user'
                print(message)
                transaction.savepoint_rollback(sid1) # 回滚
                return Response(status=status.HTTP_404_NOT_FOUND)
            if user.Password == hash_code(password):
                transaction.savepoint_commit(sid1) # 正常提交
                return Response(data=user.id, status=status.HTTP_200_OK)
            else:
                transaction.savepoint_rollback(sid1) # 回滚
                return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            transaction.savepoint_rollback(sid1) # 回滚
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@transaction.atomic
def register(request):
    '''
    Register logic
    '''
    if request.method == 'POST':
        '''设置保存点用于事务管理'''
        sid1 = transaction.savepoint()
        serializer = UserSerializer(data=request.data) 
        if serializer.is_valid():
            name = serializer.data['UserName']
            password = serializer.data['Password']
            same_user = User.objects.filter(UserName=name)
            print(same_user)
            if same_user:
                message = 'User already exists.'
                print(message)
                transaction.savepoint_rollback(sid1) # 回滚
                return Response(status=status.HTTP_403_FORBIDDEN)
            new_user = User.objects.create(UserName=name, Password=hash_code(password))
            message = 'Create user successfully.'
            print(message)
            transaction.savepoint_commit(sid1) # 正常提交
            return Response(status=status.HTTP_200_OK)
        else:
            transaction.savepoint_rollback(sid1) # 回滚
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@transaction.atomic
def question_list(request):
    '''
    return question list.  
    or create a new question. 
    GET方法： 获得问题列表  
    POST方法： 提出新问题 
    '''
    if request.method == 'GET':
        '''设置保存点用于事务管理'''
        sid1 = transaction.savepoint()
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        transaction.savepoint_commit(sid1) # 正常提交
        return Response(serializer.data)
    elif request.method == 'POST':
        '''设置保存点用于事务管理'''
        sid2 = transaction.savepoint()
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            transaction.savepoint_commit(sid2) # 正常提交
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            transaction.savepoint_rollback(sid2) # 回滚
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


@api_view(['GET', 'PUT', 'DELETE'])
@transaction.atomic
def question_detail(request, question_id):
    '''
    GET方法： 获得某个具体问题   
    PUT方法： 修改某个具体问题  
    '''
    '''设置保存点用于事务管理'''
    sid0 = transaction.savepoint()
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        transaction.savepoint_rollback(sid0) # 回滚
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        '''设置保存点用于事务管理'''
        sid1 = transaction.savepoint()
        serializer = QuestionSerializer(question)
        transaction.savepoint_commit(sid1) # 正常提交
        return Response(serializer.data)
    elif request.method == 'PUT':
        '''设置保存点用于事务管理'''
        sid2 = transaction.savepoint()
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            transaction.savepoint_commit(sid2) # 正常提交
            return Response(serializer.data)
        else:
            transaction.savepoint_rollback(sid2) # 回滚
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        '''设置保存点用于事务管理'''
        sid3 = transaction.savepoint()
        question.delete()
        transaction.savepoint_commit(sid3) # 正常提交
        return Response(status=status.HTTP_204_NO_CONTENT)
    # pass 

@api_view(['GET', 'POST', 'DELETE'])
@transaction.atomic
def answer_list(request, question_id):
    '''
    answer a question  
    '''
    '''设置保存点用于事务管理'''
    sid0 = transaction.savepoint()
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        transaction.savepoint_rollback(sid0) # 回滚
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        '''设置保存点用于事务管理'''
        sid1 = transaction.savepoint()
        answers = Answer.objects.filter(AnswerToQuestion=question_id)
        serializer = AnswerSerializer(answers, many=True)
        transaction.savepoint_commit(sid1) # 正常提交
        return Response(serializer.data)
    elif request.method == 'POST':
        '''设置保存点用于事务管理'''
        sid2 = transaction.savepoint()
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            answerOwn = int(serializer.data['AnswerOwner'])
            answerWord = serializer.data['AnswerWords']
            answerQue = question_id
            own = User.objects.get(id=answerOwn) 
            if own:
                pass 
            else:
                message = 'No this owner'
                print(message)
                transaction.savepoint_rollback(sid2) # 回滚
                return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

            same_ans = Answer.objects.filter(AnswerOwner=answerOwn, AnswerToQuestion=answerQue)
            if same_ans:
                message = 'Already exists a answer, one person has two question is not allowed'
                print(message)
                transaction.savepoint_rollback(sid2) # 回滚
                return Response(serializer.errors,status=status.HTTP_403_FORBIDDEN)

            newAns = Answer.objects.create(AnswerWords=answerWord, 
                        AnswerOwner=own, AnswerToQuestion=question)
            transaction.savepoint_commit(sid2) # 正常提交
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        else:
            transaction.savepoint_rollback(sid2) # 回滚
            return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
@transaction.atomic
def answer_detail(request, question_id, answer_id):
    '''
    查看答案  
    修改答案  
    '''
    '''设置保存点用于事务管理'''
    sid0 = transaction.savepoint()
    try:
        answer = Answer.objects.get(id=answer_id)
    except Answer.DoesNotExist:
        transaction.savepoint_rollback(sid0) # 回滚
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        '''设置保存点用于事务管理'''
        sid1 = transaction.savepoint()
        serializer = AnswerSerializer(answer)
        transaction.savepoint_commit(sid1) # 正常提交
        return Response(serializer.data)
    elif request.method == 'PUT':
        '''设置保存点用于事务管理'''
        sid2 = transaction.savepoint()
        serializer = AnswerSerializer(answer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            transaction.savepoint_commit(sid2) # 正常提交
            return Response(serializer.data)
        else:
            transaction.savepoint_rollback(sid2) # 回滚
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        '''设置保存点用于事务管理'''
        sid3 = transaction.savepoint()
        answer.delete()
        transaction.savepoint_commit(sid3) # 正常提交
        return Response(status=status.HTTP_204_NO_CONTENT)
