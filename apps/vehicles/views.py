from django.shortcuts import render
from apps.vehicles import models
from apps.vehicles import serializer 
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
# Create your views here.

class TypeView(viewsets.ModelViewSet):
    queryset = models.Type.objects.all()
    serializer_class = serializer.TypeSerializer
    
    def get_permissions(self):
        permission_classes_by_action = {
        'list': [AllowAny],
        'create': [IsAuthenticated],
        'books': [IsAuthenticated],
        'destroy': [IsAuthenticated],
        'update': [IsAuthenticated],
        'retrieve': [IsAuthenticated],
        }
        try:
            return [permission() for permission in permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

class BrandView(viewsets.ModelViewSet):
    queryset = models.Brand.objects.all()
    serializer_class = serializer.BrandSerializer
    
    def get_permissions(self):
        permission_classes_by_action = {
            'list': [AllowAny],
            'create': [IsAuthenticated],
            'books': [IsAuthenticated],
            'destroy': [IsAuthenticated],
            'update': [IsAuthenticated],
            'retrieve': [IsAuthenticated],
        }
        try:
            return [permission() for permission in permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

class StatusView(viewsets.ModelViewSet):
    queryset = models.Status.objects.all()
    serializer_class = serializer.StatusSerializer
    
    
    def get_permissions(self):
        permission_classes_by_action = {
            'list': [AllowAny],
            'create': [IsAuthenticated],
            'books': [IsAuthenticated],
            'destroy': [IsAuthenticated],
            'update': [IsAuthenticated],
            'retrieve': [IsAuthenticated],
        }
        try:
            return [permission() for permission in permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]    

class VehicleView(viewsets.ModelViewSet):
    queryset = models.Vehicle.objects.all()
    serializer_class = serializer.VehiclesSerializer

    def get_permissions(self):
        permission_classes_by_action = {
            'list': [AllowAny],
            'create': [IsAuthenticated],
            'books': [IsAuthenticated],
            'destroy': [IsAuthenticated],
            'update': [IsAuthenticated],
            'retrieve': [IsAuthenticated],
        }
        try:
            return [permission() for permission in permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

    def get_queryset(self):
        queryset = models.Vehicle.objects.filter(sold=False)
        return queryset

class PhotosView(viewsets.ModelViewSet):
    queryset = models.Photos.objects.all()
    serializer_class = serializer.PhotosSerializer
    
    def get_permissions(self):
        permission_classes_by_action = {
            'list': [AllowAny],
            'create': [IsAuthenticated],
            'books': [IsAuthenticated],
            'destroy': [IsAuthenticated],
            'update': [IsAuthenticated],
            'retrieve': [IsAuthenticated],
        }
        try:
            return [permission() for permission in permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]  
  


