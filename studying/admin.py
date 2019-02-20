from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Testing, MultiChoiceQuestion, Choice, MatchTask, MatchQuestion, TFStatement, TFTask, WordBoxTask, Sentence

# Register your models here.


class SentenceInline(admin.TabularInline):
    model = Sentence
    extra = 1


class WordBoxAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['task_name', 'test', 'without_wordbox']})
    ]
    inlines = [SentenceInline]


class TFstatInline(admin.TabularInline):
    model = TFStatement
    extra = 1


class TFTaskAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['test', 'task_name']})
    ]
    inlines = [TFstatInline]


class TestAdmin(admin.ModelAdmin):
    fieldsets = [
         ('Testing', {'fields': ['test_name', 'description', 'test_date', 'students']})
     ]


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


# class MatchChoiceInline(admin.TabularInline):
#     model = MatchingChoice
#     extra = 1


class QuestionInline(admin.TabularInline):
    model = MatchQuestion
    extra = 1


class MultiChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question', {'fields': ['question_name', 'test', 'task', 'question']})
    ]
    inlines = [ChoiceInline]


class MatchAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Task', {'fields': ['match_task_name', 'test', 'task']})
    ]
    inlines = [QuestionInline]


admin.site.register(Testing, TestAdmin)
admin.site.register(MultiChoiceQuestion, MultiChoiceAdmin)
admin.site.register(MatchTask, MatchAdmin)
admin.site.register(TFTask, TFTaskAdmin)
admin.site.register(WordBoxTask, WordBoxAdmin)