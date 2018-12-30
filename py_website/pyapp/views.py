from django.shortcuts import render
from .models import Question, Answer

# Create your views here.

def index(request):
    """

    app的主页
    """
    return render(request, 'index.html')

# def topics(request):
#     """

#     显示所有的主题
#     """
#     topics = Topic.objects.order_by('date_added')
#     context = {'topics': topics}
#     return render(request, 'topics.html',context)

# def topic(request, topic_id):
#     """

#     显示单个主题下的所有条目
#     """
#     topic = Topic.objects.get(id=topic_id)
#     entries = topic.entry_set.order_by('-date_added')
#     context = {'topic': topic, 'entries': entries}
#     return render(request, 'topic.html',context)


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
    context = {'question': question}
    return render(request, 'question.html', context)

