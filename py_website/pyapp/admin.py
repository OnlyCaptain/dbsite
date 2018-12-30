from django.contrib import admin
# from .models import Topic,Entry
from .models import Question, User, UserFocusQuestion, QuestionToUser, Answer
# Register your models here.

# class TopicAdmin(admin.ModelAdmin):
#     list_display = ('text', 'date_added')

# class EntryAdmin(admin.ModelAdmin):
#     list_display = ('topic', 'text', 'date_added')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('Description', 'date_added')

class UserAdmin(admin.ModelAdmin):
    list_display = ('UserName',)


class UserFocusQuestionAdmin(admin.ModelAdmin):
    list_display = ('QuestionID',)

class QuestionToUserAdmin(admin.ModelAdmin):
    list_display = ('UserID',)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('AnswerWords', 'AnswerOwner', 'AnswerToQuestion')


admin.site.register(Question, QuestionAdmin)
admin.site.register(User, UserAdmin)

admin.site.register(Answer, AnswerAdmin)

admin.site.register(UserFocusQuestion, UserFocusQuestionAdmin)

admin.site.register(QuestionToUser, QuestionToUserAdmin)


# admin.site.register(Entry, EntryAdmin)
