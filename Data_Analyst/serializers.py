from rest_framework import serializers
from .models import VillageMappingFile,VillageBoundaryModel
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from django_filters import rest_framework as filters


# class StateSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField()
#     class Meta:
#         model=State
#         fields =('id','state_name',)
    
class VillageMappingFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = VillageMappingFile
        fields = '__all__'
        # datatables_always_serialize = ('id',)


class VillageBoundaryModelSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = VillageBoundaryModel
        geo_field="geometry"
        fields = '__all__'

