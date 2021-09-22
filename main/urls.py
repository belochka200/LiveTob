from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('history/', views.history, name='history'),
    path('dev/', views.developers, name='developers'),
    path('brand/', views.brand, name='brand'),
]
