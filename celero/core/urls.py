from django.urls import path, include

urlpatterns = [
    path('', include(('core.api.v1.urls', 'core'), namespace='csvs')),
]
