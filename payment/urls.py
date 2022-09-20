from django.urls import path
from . import views
urlpatterns = [
    path('click/', views.TestView.as_view()),
]
