from django.db import models
from django.core.exceptions import ValidationError


class Question(models.Model):

    ERROR_NO_NUMBER_OF_ANSWERS = 'Для вопросов с вариантами ответов нужно указать количество правильных ответов'
    ERROR_NUMBER_OF_ANSWER_FOR_TEXT_QUESTION = (
       'Для вопросов с текстовым ответом не нужно указывать количество правильных ответов')

    KIND_TEXT, KIND_OPTIONS = 'text', 'choices'
    KIND_CHOICES = (
        (KIND_TEXT, 'Вопрос с текстовым ответом'),
        (KIND_OPTIONS, 'Вопрос с выбором одного или нескольких вариантов')
    )

    poll = models.ForeignKey('Poll', on_delete=models.CASCADE, related_name='questions')
    text = models.TextField(verbose_name='текст вопроса')
    kind = models.CharField(
        verbose_name='тип вопроса', max_length=16, choices=KIND_CHOICES, default=KIND_TEXT)
    number_of_answers = models.IntegerField(
        verbose_name='количество правильных ответов, для вопросов с вариантами', blank=True, null=True)

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'
        ordering = ('id', )

    def __str__(self):
        return f'Вопрос {self.pk} к {self.poll}'

    def clean(self):
        if self.kind == Question.KIND_OPTIONS and not self.number_of_answers:
            raise ValidationError(Question.ERROR_NO_NUMBER_OF_ANSWERS)
        elif self.kind == Question.KIND_TEXT and self.number_of_answers:
            raise ValidationError(Question.ERROR_NUMBER_OF_ANSWER_FOR_TEXT_QUESTION)
