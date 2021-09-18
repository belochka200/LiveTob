from django.urls import path

from .views import *

urlpatterns = [
    path('', sights, name='sights'),
    path('show-sight-<slug:slug>/', show_sights, name='show_sights'),
    path('load-more-sights/', load_sights, name='load-more-sights'),
]
