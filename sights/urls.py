from django.urls import path

from . import views
from .views import DynamicPostLoad

urlpatterns = [
    path('', views.sights, name='sights'),
    path('show-sight-<slug:slug>/', views.show_sights, name='show_sights'),
    path('load-more-sights/', DynamicPostLoad.as_view(), name='load-more-sights'),
]
