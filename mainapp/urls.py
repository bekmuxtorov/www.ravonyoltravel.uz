from .views import (
    BasePageView,
    travels_list,
    HomePagesView,
    ImagePagesView,
    AboutPagesView,
    travel_detail_view,
    ImageDetailView,
    CommentPagesView,
    CommentNewView,
    CommentDetailView,
    TransportPagesView,
    my_orders,
    make_new_order,
)
from django.urls import path

urlpatterns = [
    path('', HomePagesView.as_view(), name='home'),
    path('base/', BasePageView.as_view(), name='base'),

    path('travels/', travels_list, name='travels'),
    path('travels/<int:pk>/', travel_detail_view, name='travel_detail'),

    path('product/', my_orders, name='product'),
    path('images/', ImagePagesView.as_view(), name="images"),
    path('images/<int:pk>/', ImageDetailView.as_view(), name='images_detail'),
    path('about/', AboutPagesView.as_view(), name='about'),
    path('my-orders/', my_orders, name='choose_travel'),
    path('new-order/<int:pk>', make_new_order, name='modal'),
    path('fikrlar/', CommentPagesView.as_view(), name='fikrlar'),
    path('fikrlar/add/', CommentNewView.as_view(), name='fikrlar_new'),
    path('fikrlar/<int:pk>', CommentDetailView.as_view(), name='fikrlar_detail'),
    path('transport/', TransportPagesView.as_view(), name="transport"),
]
