# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from url_shortner_project.shortener.models import KirrURL

admin.site.register(KirrURL)
