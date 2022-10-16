from itertools import product
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import Travel, Tassurotlar, Rasmlar, Fikrlar, Transport
from payment.models import Order
# Create your views here.

class BasePageView(TemplateView):
    template_name = 'base.html'

def TravelPageView(request):
    object_list = Travel.objects.all()
    context = {
        'object_list':object_list,
              }

    return render(request, 'travel.html', context)

def ModalPageView(request, pk):
    status = False
    if request.method == "POST":
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        place_id = request.POST.get('place_id')
        object = Order(place_id=place_id, customer_full_name=name, customer_phone_number=phone_number).save()
        status = True
        request.session['recently_viewed'] =  object.get_uid

    object = Travel.objects.get(pk=pk)
    context = {'object':object,
                'status': status
                }

    return render(request, 'modal.html', context)


def TravelChoosePageView(request, pk):
    choose_travel = Travel.objects.get(pk=pk)
    context = {'choose_travel':choose_travel}
    return render(request, 'travel.html', context)

def TravelDetailView(request, pk):
    object = Travel.objects.get(pk=pk)
    context = {"object":object}

    # Modelda kiritilgan qiymatlarni Order modeliga saqlash
    if request.method == "POST":
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        object = Order(place_id=pk, customer_full_name=name, customer_phone_number=phone_number).save()



    return render(request, 'travel_detail.html', context)
    

class NewsPagesView(ListView):
    model = Tassurotlar
    template_name = 'news.html'

def ChooseTravelView(request):
    recently_viewed_products = None

    if 'recently_viewed' in request.session:
        products = Travel.objects.filter(pk__in=request.session['recently_viewed'])
        recently_viewed_products = (products)        
        if len(request.session['recently_viewed']) > 5:
            request.session['recently_viewed'].pop()
        
    else:
        products = "Hozircha hech qanday buyurtma berilmagan!"

    request.session.modified = True

    context = {
        'recently_viewed_products': recently_viewed_products,


    }

        

    return render(request, 'chosse_travel.html', context)

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
