from django.urls import path
from rest_framework import routers

from api.v1.views import (
    AthleteViewSet,
    CityViewSet,
    EventViewSet,
    NOCViewSet,
    OlympicsViewSet,
    RegionViewSet,
    ResultViewSet,
    SportViewSet,
    UploadResultsCsvView,
    UploadRegionCsvView,
    TeamViewSet,
)

router = routers.SimpleRouter()
router.register(r'region', RegionViewSet, basename='region')
router.register(r'noc', NOCViewSet, basename='noc')
router.register(r'city', CityViewSet, basename='city')
router.register(r'sport', SportViewSet, basename='sport')
router.register(r'event', EventViewSet, basename='event')
router.register(r'team', TeamViewSet, basename='team')
router.register(r'athlete', AthleteViewSet, basename='athlete')
router.register(r'olympics', OlympicsViewSet, basename='olympics')
router.register(r'result', ResultViewSet, basename='result')

urlpatterns = [
    path('upload-results-csv/', UploadResultsCsvView.as_view(), name='upload-view'),
    path('upload-regions-csv/', UploadRegionCsvView.as_view(), name='upload-view'),
] + router.urls
