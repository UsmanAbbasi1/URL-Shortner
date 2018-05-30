# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from shortener.utils import create_shortcode


class KirrUrlManager(models.Manager):
    """We are using this for example purpose only"""

    def reset_codes(self):
        query_set = KirrURL.objects.all()

        for item in query_set:
            item.shortcode = create_shortcode(item)
            item.save()


# Create your models here.
class KirrURL(models.Model):
    url = models.CharField(max_length=220)
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)  # when model was last updated
    timestamp = models.DateTimeField(auto_now_add=True)  # when model was created

    # Overriding manager just for example purposes
    objects = KirrUrlManager()

    def save(self, *args, **kwargs):
        if not self.shortcode:
            self.shortcode = create_shortcode(self)

        super(KirrURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)