from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import Travel, Tassurotlar, Rasmlar, Fikrlar, Transport

# Create your views here.

class BasePageView(TemplateView):
    template_name = 'base.html'

class TravelPageView(ListView):
    model = Travel
    template_name = 'travel.html'

class TravelDetailView(DetailView):
    model = Travel
    template_name = 'travel_detail.html'

class NewsPagesView(ListView):
    model = Tassurotlar
    template_name = 'news.html'


# Commentariya 
# ===================================

class CommentPagesView(ListView):
    model = Fikrlar
    template_name = 'fikrlar.html'

class CommentDetailView(DetailView):
    model = Fikrlar
    template_name = 'fikrlar_detail.html'

class CommentNewView(CreateView):
    model = Fikrlar
    template_name = 'fikrlar_new.html'
    fields = ['name', 'text']

# ===================================

class NewsDetailView(DetailView):
    model = Tassurotlar
    template_name = 'news_detail.html'

class HomePagesView(TemplateView):
    template_name = 'home.html'

class ImagePagesView(ListView):
    model = Rasmlar
    template_name = 'images.html'

class ImageDetailView(DetailView):
    model = Rasmlar
    template_name = 'images_detail.html'

class AboutPagesView(TemplateView):
    template_name = 'about.html'

# Transport xizmati
# ===================================
class TransportPagesView(ListView):
    model = Transport
    template_name = 'transport.html'



# ===================================








