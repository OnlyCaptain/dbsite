from django.shortcuts import render
from .models import Question, Answer, User
from django.shortcuts import redirect
# Create your views here.
from . import forms

import hashlib


def hash_code(s, salt='captainsite'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


def index(request):
    """

    app的主页  
    (啥都没有)
    """
    return render(request, 'index.html')

def questions(request):
    """

    显示所有问题的界面  
    使用接口： 
    Question.objects.order_by()  
    相当于 sql语句中的 order by
    """
    questions = Question.objects.order_by('date_added')
    context = {'questions': questions}
    return render(request, 'questions.html', context)

def question(request, question_id):
    """
    
    显示单个问题界面  
    使用接口：
    Question.objects.get()  
    Answer.objects.filter()  
    两个方法都是查询变量，不同的地方在get方法只能获取单条语句，
    获取两个或两个以上使用 filter（筛选）方法。 
    """
    question = Question.objects.get(id=question_id)
    # entries = topic.entry_set.order_by
    answers = Answer.objects.filter(AnswerToQuestion=question_id).order_by('date_added')
    context = {'question': question, 'answers': answers}
    return render(request, 'question.html', context)

def login(request):
    """
    
    登录界面，只需要填写用户和密码。  
    在数据库里面的内容是hash过的。  
    使用接口：
    User.objects.get()  
    查询了 User里面的东西，相当于 sql 语句中的 SELECT FROM
    """

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

            if user.Password == hash_code(password):
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

def logout(request):
    """
    
    登出界面  
    只是修改了会话层里面的 is_login 变量
    """
    if not request.session.get('is_login', None):
        return redirect('/index')
    request.session['is_login'] = False 
    request.session.flush()
    return redirect('/index')

def register(request):
    """
    
    注册界面, 需要填写用户名和两次密码（确认）  
    使用接口：
    User.objects.create(...) 
    无需自己另外调用 save(), 相当于 sql语句中的 INSERT INTO
    """
    if request.session.get('is_login', None):
        return redirect('/index')

    if request.method == "POST":
        register_form = forms.RegisterForm(request.POST)
        message = '请检查填写的内容!'
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            if password1 != password2:
                message = '两次输入的密码不相同！'
                return render(request, 'register.html', locals())
            else:
                same_name_user = User.objects.filter(UserName=username)
                if same_name_user:
                    message = '用户名已经存在，请重新选择！'
                    return render(request, 'register.html', locals())

            new_user = User.objects.create(UserName=username, Password=hash_code(password2))

            message = '注册成功！正在跳转...'

            return render(request, 'confirm.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'register.html', locals())

def confirm(request):
    """
    
    确认登录等待  
    在 confirm.html 里面等待了 2s
    """

    return render(request, 'confirm.html')
