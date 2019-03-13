
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Person', views.PersonView)
router.register('Pet', views.PetView)
router.register('House', views.HouseView)

urlpatterns = [
    path('', include(router.urls))
]
