from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField('标题', max_length=100)
    description = models.TextField('描述')
    completed = models.BooleanField('是否完成', default=False)
    create_date = models.DateTimeField('创建时间', auto_now_add=True)

    def __unicode__(self):
        return self.title

class Question(models.Model):
    """
    
    问题
    """
    Description = models.TextField()   # 创建文本项，没有长度限制
    date_added = models.DateTimeField(auto_now_add=True)   # 使用系统自带的时间

    def __str__(self):
        return self.Description 


class User(models.Model):
    """

    用户
    """
    UserName = models.CharField(max_length=200)  # 长度限制为 200
    Password = models.CharField(max_length=200)  

class Answer(models.Model):
    """

    答案
    """
    AnswerWords = models.TextField()
    AnswerOwner = models.ForeignKey(User, on_delete=models.CASCADE)   # 外码约束
    AnswerToQuestion = models.ForeignKey(Question, on_delete=models.CASCADE)  
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.AnswerWords

class UserFocusQuestion(models.Model):
    """

    用户关注问题
    """
    QuestionID = models.ForeignKey(Question, on_delete=models.CASCADE)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)

class QuestionToUser(models.Model):
    """
    
    用户对应问题
    """
    QuestionID = models.ForeignKey(Question, on_delete=models.CASCADE)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
