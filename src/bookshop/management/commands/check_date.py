from django.core.management.base import BaseCommand, CommandError
from bookshop.models import Event
from logging import getLogger
from datetime import datetime
from django.core.mail import send_mail
import pytz

utc = pytz.UTC

logger = getLogger('django')


class Command (BaseCommand):
    def handle(self, *args, **options):
        now = utc.localize(datetime.now())
        all_events = Event.objects.all()
        for event in all_events:
                if event.need_remind and event.date_start - event.reminder <= now:
                    email = event.User_event.email
                    send_mail(
                        'Пора',
                        f"{event.title}-{event.date_start}",
                        'kirill.bar.kazak@gmail.com',
                        [email],
                        fail_silently=False,
                )
                event.need_remind = False
                event.save()
                logger.warning('sent')



