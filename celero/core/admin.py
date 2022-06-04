from django.contrib import admin

from core.models import (
    Athlete,
    City,
    Event,
    NOC,
    Olympics,
    Region,
    Result,
    Sport,
)

admin.site.register(Athlete)
admin.site.register(City)
admin.site.register(Event)
admin.site.register(NOC)
admin.site.register(Olympics)
admin.site.register(Region)
admin.site.register(Result)
admin.site.register(Sport)
