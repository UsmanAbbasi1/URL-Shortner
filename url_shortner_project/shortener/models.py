# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from url_shortner_project.shortener.utils import create_shortcode


# Create your models here.
class KirrURL(models.Model):
    url = models.CharField(max_length=220)
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)  # when model was last updated
    timestamp = models.DateTimeField(auto_now_add=True)  # when model was created

    def save(self, *args, **kwargs):
        if not self.shortcode:
            self.shortcode = create_shortcode(self)

        super(KirrURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)
