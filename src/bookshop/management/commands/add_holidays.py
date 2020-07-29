from bookshop.models import Holiday
from logging import getLogger
from ics import Calendar
from django.core.management.base import BaseCommand
from requests import get

logger = getLogger('django')

class Command(BaseCommand):
    def handle(self, *args, **options):
        url = "https://www.officeholidays.com/ics/ics_country.php?tbl_country=Belarus"
        calendar = Calendar(get(url).text)
        for h in calendar.events:
            h = Holiday(
            title=h.name,
            date_start=h.begin.date(),
            duration=h.duration,
            descriptions=h.description
            )
            try:
                h.save()
                logger.warning(h.title)
            except:
                pass
