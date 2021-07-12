from django.db import models
from django.utils import timezone


class PollQueryset(models.QuerySet):

    def active_polls(self):
        now_date = timezone.now().date()
        return self.filter(start_date__lte=now_date).filter(finish_date__gte=now_date)


class Poll(models.Model):

    name = models.CharField(verbose_name='название опроса', max_length=50)
    start_date = models.DateField(verbose_name='дата старта опроса')
    finish_date = models.DateField(verbose_name='дата окончания опроса')
    description = models.TextField(verbose_name='описание')

    objects = PollQueryset.as_manager()

    class Meta:
        verbose_name = 'опрос'
        verbose_name_plural = 'опросы'
        ordering = ('id', )

    def __str__(self):
        return f'Опрос {self.pk}-{self.name[:15]}'
