from django.contrib import admin
from bookshop.models import Event, Holiday


class EventAdmin(admin.ModelAdmin):
    fields = ('title', 'date_start', 'date_stop', 'reminder', 'need_remind', 'User_event')



admin.site.register(Event, EventAdmin)
admin.site.register(Holiday)





