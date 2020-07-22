from datetime import timedelta
from django.db import models
from logging import getLogger


logger = getLogger('django')
CHOICE_DELTA = [
    (timedelta(hours=1), 'За час'),
    (timedelta(hours=2), 'За 2 часа'),
    (timedelta(hours=4), 'За 4 часа'),
    (timedelta(days=1), 'За день'),
    (timedelta(weeks=1), 'За неделю')
]
class Event(models.Model):
    class Meta:
        verbose_name_plural = 'события'
        verbose_name = 'событие'
        db_table = 'my_event'

    choice_delta = CHOICE_DELTA
    title = models.CharField(
        max_length=100,
        verbose_name='Название события')
    date_start = models.DateTimeField(
        verbose_name='Начало события'
    )
    date_stop = models.DateTimeField(
        verbose_name='Окончание события',
        blank=True,
        null=True
    )
    reminder = models.DurationField(
        verbose_name='напомнить за...',
        choices=choice_delta)


    @property
    def reminder4api(self):
        for i in self.choice_delta:
            if self.reminder == i[0]:
                return i[1]
        return 'not found'

    def __str__(self):
        return self.title
    
    def save(self, **kwargs):
        if self.date_stop is None:
            self.date_stop = self.date_start.replace(
                hour=23,
                minute=59,
                second=59
            )


