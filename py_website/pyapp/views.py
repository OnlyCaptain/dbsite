from django.shortcuts import render
from .models import Question, Answer, User
from django.shortcuts import redirect
# Create your views here.
from . import forms

import hashlib


def index(request):
    """

    app的主页
    """
    return render(request, 'index.html')

def questions(request):
    """

    显示所有问题
    """
    questions = Question.objects.order_by('date_added')
    context = {'questions': questions}
    return render(request, 'questions.html', context)

def question(request, question_id):
    """
    
    显示详细问题
    """
    question = Question.objects.get(id=question_id)
    # entries = topic.entry_set.order_by
    answers = Answer.objects.filter(AnswerToQuestion=question_id).order_by('date_added')
    context = {'question': question, 'answers': answers}
    return render(request, 'question.html', context)

def login(request):
    if request.session.get('is_login', None):
        return redirect('/index')
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = '所有的字段都必须填写！'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            # ....
            try:
                user = User.objects.get(UserName=username)
            except:
                message = '用户不存在'
                return render(request, 'login.html', locals())

            if user.Password == (password):
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.UserName
                return redirect('/index')
            else:
                message = '密码错误'
                return render(request, 'login.html', locals())
        else:
            return render(request, 'login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'login.html', locals())


# def answers(request， question_id):
#     """
    
#     显示所有答案
#     """
#     # Answer = Answer.object.get(id=)

#     return render(request, 'ques')

