from django.urls import path

from .views import *

urlpatterns = [
    path('', where_to_go, name='where_to_go'),
    path('where-to-eat/', where_to_eat, name='where_to_eat'),
    path('where-to-rest/', where_to_rest, name='where_to_rest'),
    path('where-to-do/', where_to_do, name='where_to_do'),
    path('load-more-cafe/', cafe_load, name='load_more_cafe'),
    path('load-more-hotel/', hotel_load, name='load_more_hotel'),
    path('load-more-entertainment/', ent_load, name='load_more_entertainment'),
    path('show-to-eat-<slug:slug>/', show_to_eat, name='show_to_eat'),
    path('show-to-rest-<slug:slug>/', show_to_rest, name='show_to_rest'),
    path('show-to-do-<slug:slug>/', show_to_do, name='show_to_do')
]
