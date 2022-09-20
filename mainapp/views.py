from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import Travel, Tassurotlar, Rasmlar, Fikrlar, Transport

from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from .serializers import OrderSerializer


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


# Payment
# ===================================
class OrderCreateAPIView(CreateAPIView):
    queryset = Travel.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        order_id = response.data.get('id')
        order = Travel.objects.get(pk=order_id)
        return_url = request.data.get('return_url')
        return Response({
            'request': 'success',
            'click': order.get_payment_url(return_url)
        }, status=HTTP_201_CREATED)










