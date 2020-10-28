from django.urls import path
from rest_framework import routers

from apps.vehicles import views as vehicles_v

vehicles = routers.DefaultRouter()
vehicles.register('type',  vehicles_v.TypeView),
vehicles.register('brand',  vehicles_v.BrandView),
vehicles.register('status',  vehicles_v.StatusView),
vehicles.register('vehicles',  vehicles_v.VehicleView),
vehicles.register('photos',  vehicles_v.PhotosView),