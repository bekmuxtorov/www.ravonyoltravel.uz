from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class BasePageView(TemplateView):
    template_name = 'base.html'

class TravelPageView(TemplateView):
    template_name = 'travel.html'

class NewsPagesView(TemplateView):
    template_name = 'news.html'

class HomePagesView(TemplateView):
    template_name = 'home.html'