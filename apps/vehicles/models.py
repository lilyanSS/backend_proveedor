from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=50, verbose_name='Username', unique=True)
    email = models.EmailField(('email address'), unique=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    EXTRA_USER_FIELD = 'username'

    def __str__(self):
        return f'{self.email}'

class Type(models.Model):
    name =  models.CharField(max_length=200)

    def __str__(self):
        return self.name
       
class Brand(models.Model):
    name =  models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Status(models.Model):
    name =  models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    model = models.CharField(max_length=200)
    line = models.CharField(max_length=100)
    cubic_centimeters  = models.CharField(max_length=150)
    image = models.ImageField(upload_to = "imagenes/", blank=True)
    price= models.DecimalField(max_digits=9, decimal_places=2)
    type = models.ForeignKey(Type, on_delete=models.PROTECT, null=True, blank=True, related_name='tipo_vehiculo')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, null=True, blank=True, related_name='marca')
    provider = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, related_name='proveedor')
    status = models.ForeignKey(Status, on_delete=models.PROTECT, null=True, blank=True, related_name='estado_vehiculo')

    def __str__(self):
        return self.model

class Photos(models.Model):
    image_url= models.ImageField(upload_to='images/Photos', blank=True)
    description = models.TextField(verbose_name="Descriptiom", null=True, blank=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.PROTECT, verbose_name="Vehicle", related_name='pictures')
    
    def __str__(self):
        return f'{self.vehicle}'



