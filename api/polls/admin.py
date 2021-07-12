from django.contrib import admin
from polls.models import Poll, Question, Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):

    pass


class QuestionInline(admin.TabularInline):

    model = Question



@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):

    inlines = [QuestionInline]
    fields = ('name', 'start_date', 'finish_date', 'description',)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('start_date',)
        return self.readonly_fields
