from django.contrib import admin

# Register your models here.
from analytics.models import ClickEvent

admin.site.register(ClickEvent)