from django.contrib import admin
from .models import location, group, focus, statistics, location_statistics

# Register your models here.
admin.site.register(location)
admin.site.register(group)
admin.site.register(focus)
admin.site.register(statistics)
admin.site.register(location_statistics)