from django.contrib import admin
from bookshop.models import Event


class EventAdmin(admin.ModelAdmin):
    fields = ('title', 'date_start', 'date_stop', 'reminder')


admin.site.register(Event, EventAdmin)




