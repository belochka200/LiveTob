from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import SimpleRouter
from sights.views import SightsViewAPI

router = SimpleRouter()

router.register('api/sights', SightsViewAPI)

urlpatterns = [
    path('', include('main.urls')),
    path('where-to-go/', include('events.urls')),
    path('sights/', include('sights.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)