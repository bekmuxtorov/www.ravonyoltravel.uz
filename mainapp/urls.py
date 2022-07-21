from unicodedata import name
from .views import (
    BasePageView, 
    TravelPageView, 
    NewsPagesView, 
    HomePagesView, 
    ImagePagesView, 
    AboutPagesView, 
    TravelDetailView,
    NewsDetailView,
    ImageDetailView,
    )
from django.urls import path    


urlpatterns = [
    path('', HomePagesView.as_view(), name = 'home'),
    path('base/', BasePageView.as_view(), name = 'base'),
    path('travels/', TravelPageView.as_view(), name = 'travels' ),
    path('news/', NewsPagesView.as_view(), name='news'),
    path('images/', ImagePagesView.as_view(), name = "images"),
    path('images/<int:pk>/',ImageDetailView.as_view(), name = 'images_detail' ),
    path('about/', AboutPagesView.as_view(), name = 'about'),
    path('travels/<int:pk>/', TravelDetailView.as_view(), name = 'travel_detail'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name = 'news_detail'),
]
