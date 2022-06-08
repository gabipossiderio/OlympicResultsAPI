from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(('api.urls', 'api'), namespace='api')),
    path('', include(router.urls)),
]
