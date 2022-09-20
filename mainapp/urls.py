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
    CommentPagesView,
    CommentNewView,
    CommentDetailView,
    TransportPagesView,
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
    
    path('fikrlar/', CommentPagesView.as_view(), name = 'fikrlar'),
    path('fikrlar/add/', CommentNewView.as_view(), name = 'fikrlar_new'),
    path('fikrlar/<int:pk>', CommentDetailView.as_view(), name = 'fikrlar_detail'),

    path('transport/', TransportPagesView.as_view(), name = "transport" ),

]


