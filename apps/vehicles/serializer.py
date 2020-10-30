from apps.vehicles import models
from rest_framework import serializers

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class TypeSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = models.Type
        fields =['id', 'name']

class BrandSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = models.Brand
        fields =['id', 'name']

class StatusSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = models.Status
        fields =['id', 'name']        
               
class VehiclesSerializer(DynamicFieldsModelSerializer):
    data = serializers.SerializerMethodField()
    class Meta:
        model = models.Vehicle
        fields ="__all__"  

    def get_data(self, obj):
        vehicle= models.Vehicle.objects.get(id=obj.id)
        photos=[]
        get_photos = models.Photos.objects.filter(vehicle= vehicle.id)

        for item in get_photos:
            photos.append({
                "img":item.image_url.url,
                "description":item.description
            })
      
        data={
            'status':vehicle.status.name,
            'provider':vehicle.provider.first_name +" " + vehicle.provider.last_name ,
            'brand':vehicle.brand.name,
            'type':vehicle.type.name,
            'photos':photos            
        }
        return data    

class PhotosSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = models.Photos
        fields ="__all__"           