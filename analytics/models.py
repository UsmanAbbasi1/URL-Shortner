from django.db import models

# Create your models here.
from shortener.models import KirrURL


class ClickEventManager(models.Manager):
    def create_event(self, kirrInstance):
        if isinstance(kirrInstance, KirrURL):
            obj, created = self.get_or_create(url=kirrInstance)
            obj.count += 1
            obj.save()
            return obj.count
        return None


class ClickEvent(models.Model):
    url = models.OneToOneField(KirrURL, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)

    objects = ClickEventManager()
