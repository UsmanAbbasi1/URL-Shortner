# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.views.generic import View

from analytics.models import ClickEvent
from shortener.forms import SubmitUrlForm
from shortener.models import KirrURL


class HomeView(View):
    def get(self, request):
        url_form = SubmitUrlForm()
        context = {
            'title': 'Url Shortener',
            'form': url_form
        }
        return render(request, 'shortener/home.html', context)

    def post(self, request):
        url_form = SubmitUrlForm(request.POST)
        template = 'shortener/home.html'
        context = {
            'title': 'Url Shortener',
            'form': url_form
        }

        if url_form.is_valid():
            url = url_form.cleaned_data.get('url')
            object, created = KirrURL.objects.get_or_create(url=url)
            context = {
                'object': object,
                'created': created
            }

            if created:
                template = 'shortener/success.html'
            else:
                template = 'shortener/already-exists.html'

        return render(request, template, context)


class URLRedirectView(View):
    def get(self, request, shortcode, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        print(ClickEvent.objects.create_event(obj))
        return HttpResponseRedirect(obj.url)
