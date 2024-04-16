from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PeopleViewSet, search, submit
router = DefaultRouter()
router.register('people', PeopleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('search/', search, name='search'),
    path('submit/', submit, name='submit'),
]
