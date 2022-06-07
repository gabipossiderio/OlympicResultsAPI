from django.urls import path

from core.api.v1.views import UploadResultsCsvView, UploadRegionCsvView

urlpatterns = [
    path('results', UploadResultsCsvView.as_view(), name='upload-view'),
    path('regions', UploadRegionCsvView.as_view(), name='upload-view'),
]
