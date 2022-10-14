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
        Order(place_id=place_id, customer_full_name=name, customer_phone_number=phone_number).save()
        status = True

    object = Travel.objects.get(pk=pk)
    context = {'object':object,
                'status': status
                }

    return render(request, 'modal.html', context)


def TravelChoosePageView(request, pk):
    choose_travel = Travel.objects.get(pk=pk)
    context = {'choose_travel':choose_travel}
    return render(request, 'travel.html', context)

def setsessions(request, uid):
    request.session['travels'] = uid
    return HttpResponse("session is set") 

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
    return render(request, 'chosse_travel.html')

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
