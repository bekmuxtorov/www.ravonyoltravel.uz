from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import Travel, Tassurotlar, Rasmlar, Fikrlar, Transport
from payment.models import Order

from uuid import uuid4
from django.contrib.auth.models import User


def get_or_create_user(request):
    user = request.session.get('user')
    if not user:
        print('3333')
        user = str(uuid4())
        request.session['user'] = user
    user, _ = User.objects.get_or_create(username=user)
    return user


class BasePageView(TemplateView):
    template_name = 'base.html'


def travels_list(request):
    object_list = Travel.objects.all()
    context_data = {
        'object_list': object_list,
    }
    return render(request, 'travel.html', context_data)


def make_new_order(request, pk):
    status = -1
    place = Travel.objects.get(pk=pk)
    user = get_or_create_user(request)
    order = Order.objects.filter(user=user).filter(place=place).first()
    if order is not None:
        status = 0
    if status == -1 and request.method == "POST":
        full_name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        Order.objects.create(
            user=user,
            place=place,
            customer_full_name=full_name,
            customer_phone_number=phone_number
        )
        status = 1
    context = {
        'object': place,
        'status': status
    }
    return render(request, 'modal.html', context)


def travel_detail_view(request, pk):
    order = Travel.objects.get(pk=pk)
    context = {"object": order}

    if request.method == "POST":
        # Creating new order
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        order = Order(place_id=pk, customer_full_name=name, customer_phone_number=phone_number).save()

    return render(request, 'travel_detail.html', context)


class NewsPagesView(ListView):
    model = Tassurotlar
    template_name = 'news.html'


def my_orders(request):
    orders = Order.objects.filter(user=get_or_create_user(request))
    context = {
        'orders': orders,
    }
    return render(request, 'chosse_travel.html', context)


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


class TransportPagesView(ListView):
    model = Transport
    template_name = 'transport.html'
