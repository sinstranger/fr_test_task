from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Answer(models.Model):

    ERROR_TEXT_IN_OPTIONS = (
        'В ответе к вопросу с вариантами ответов должны быть только цифры вариантов, разделенные пробелами')
    ERROR_TOO_MANY_OPTIONS = 'Количество вариантов больше, чем указано в вопросе'
    ERROR_UNACCEPTABLE_OPTION = 'Значения вариантов ответов больше, чем максимальное количество вариантов'

    question = models.ForeignKey('Question', verbose_name='вопрос', on_delete=models.CASCADE)
    user = models.IntegerField(verbose_name='ID пользователя')
    answer = models.TextField(
        verbose_name='ответ',
        help_text='Текст для текстовых ответов. Цифры, разделенные пробелами, для вопросов с вариантами')

    class Meta:
        verbose_name = 'ответ пользователя'
        verbose_name_plural = 'ответы пользователя'
        ordering = ('id', )

    def __str__(self):
        return f'Ответ {self.user} на {self.question}'
