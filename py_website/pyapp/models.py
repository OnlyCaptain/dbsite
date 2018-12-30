from django.db import models

# # Create your models here.
# class Topic(models.Model):
    
#     text = models.CharField(max_length=200)
#     date_added = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.text

# class Entry(models.Model):
#     """ 学到的有关某个主题的具体知识 """
#     topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
#     text = models.TextField() # 无长度限制
#     date_added = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         verbose_name_plural = 'entries'

#     def __str__(self):
#         return self.text[:50] + "..."

class Question(models.Model):
    """
    
    问题
    """
    Description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Description 


class User(models.Model):
    """

    用户
    """
    UserName = models.CharField(max_length=200)
    Password = models.CharField(max_length=20)

class Answer(models.Model):
    """

    答案
    """
    AnswerWords = models.TextField()
    AnswerOwner = models.ForeignKey(User, on_delete=models.CASCADE)
    AnswerToQuestion = models.ForeignKey(Question, on_delete=models.CASCADE)

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



    
