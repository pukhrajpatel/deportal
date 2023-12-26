from .serializers import VillageBoundaryModelSerializer,VillageMappingFileSerializer
from rest_framework import viewsets
from .models import *
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect


class VillageBoundaryViewsetFilter(filters.FilterSet):
    state_name = filters.CharFilter(lookup_expr="icontains",name="state_name")
    ac_no = filters.NumberFilter(lookup_expr='icontains',name="ac_no")
    class Meta:
        model = VillageBoundaryModel
        fields = ['state_name','ac_no']
        

class VillageBoundaryViewset(viewsets.ModelViewSet):
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes=[IsAuthenticated]
    queryset = VillageBoundaryModel.objects.all()
    serializer_class = VillageBoundaryModelSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['state_name','ac_no']
    

class VillageMappingFileViewsetFilter(filters.FilterSet):
    state_name = filters.CharFilter(lookup_expr="icontains",name="state_name")
    ac_no = filters.NumberFilter(lookup_expr='icontains',name="ac_no")
    class Meta:
        model = VillageMappingFile
        fields = ['state_name','ac_no',]

class VillageMappingFileViewset(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    queryset = VillageMappingFile.objects.all()
    serializer_class = VillageMappingFileSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['state_name','ac_no']
    
    # filter_backends = (filters.DjangoFilterBackend,)
    # filter_class = VillageMappingFileViewsetFilter
    # filterset_fields = ['state_name','ac_no']
    # filterset_class = VillageMappingFileViewsetFilter
    # filterset_fields = {'state_name':['exact','in'],'ac_no':['in','exact'],}
    