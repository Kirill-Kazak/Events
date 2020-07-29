
from requests import get
from ics import Calendar, Event

url = "https://www.officeholidays.com/ics/ics_country.php?tbl_country=Belarus"
c = Calendar(get(url).text)
all_events = list(c.events)