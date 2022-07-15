from unicodedata import name
from .views import BasePageView, TravelPageView, NewsPagesView,HomePagesView
from django.urls import path    


urlpatterns = [
    path('base/', BasePageView.as_view(), name = 'base'),
    path('travel/', TravelPageView.as_view(), name = 'travel' ),
    path('news/', NewsPagesView.as_view(), name='news'),
    path('', HomePagesView.as_view(), name = 'home')
]
