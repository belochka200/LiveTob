from django.urls import path

from . import views
from .views import DynamicCafeLoad
from .views import DynamicHotelLoad
from .views import DynamicEntertainmentLoad

urlpatterns = [
    path('', views.where_to_go, name='where_to_go'),
    path('where-to-eat/', views.where_to_eat, name='where_to_eat'),
    path('where-to-rest/', views.where_to_rest, name='where_to_rest'),
    path('where-to-do/', views.where_to_do, name='where_to_do'),
    path('load-more-cafe/', DynamicCafeLoad.as_view(), name='load_more_cafe'),
    path('load-more-hotel/', DynamicHotelLoad.as_view(), name='load_more_hotel'),
    path('load-more-entertainment/', DynamicEntertainmentLoad.as_view(), name='load_more_entertainment'),
    path('show-to-eat-<slug:slug>/', views.show_to_eat, name='show_to_eat'),
    path('show-to-rest-<slug:slug>/', views.show_to_rest, name='show_to_rest'),
    path('show-to-do-<slug:slug>/', views.show_to_do, name='show_to_do')
]
