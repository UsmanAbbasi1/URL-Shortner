# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
# Create your views here.
from django.shortcuts import get_object_or_404
from django.views.generic import View

from shortener.models import KirrURL


class KirrRedirectView(View):
    def get(self, request, shortcode, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)
