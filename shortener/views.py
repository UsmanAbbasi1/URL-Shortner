# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
# Create your views here.
from django.views.generic import View


class KirrRedirectView(View):
    def get(self, request, shortcode, *args, **kwargs):
        return HttpResponse(f'Hello:{shortcode}')
