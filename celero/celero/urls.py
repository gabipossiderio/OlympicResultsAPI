from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('csv-reader/', include(('core.urls', 'core'), namespace='csvs')),
    path('', include(router.urls)),
]
