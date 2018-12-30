from django.db import models

# Create your models here.

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



    
