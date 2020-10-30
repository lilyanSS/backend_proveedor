from django.contrib import admin
from apps.vehicles import models
# Register your models here.

admin.site.register(models.Type)
admin.site.register(models.User)
admin.site.register(models.Brand)
admin.site.register(models.Status)
admin.site.register(models.Vehicle)
admin.site.register(models.Photos)
