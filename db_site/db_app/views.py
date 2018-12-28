from django.shortcuts import render
from .models import Topic

# Create your views here.

def index(request):
    """app的主页"""
    return render(request, 'db_app/index.html')

def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'db_app/topics.html',context)

def topic(request, topic_id):
    """显示单个主题下的所有条目"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'db_app/topic.html',context)