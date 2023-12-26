from django.contrib import admin
from .models import VillageMappingFile,VillageBoundaryModel
from import_export.admin import ImportExportActionModelAdmin,ImportMixin,ImportExportModelAdmin,ExportActionMixin
from .forms import *
from .resource import *


# Register your models here.
class VillageMappingFileAdmin(ImportExportModelAdmin,ExportActionMixin):
    import_form_class = CustomImportForm
    export_form_class = CustomExportForm
    confirm_form_class = CustomConfirmImportForm
    resource_classes = [VillageMappingFileResource]
    def get_confirm_form_initial(self,request,import_form):
        initial = super().get_confirm_form_initial(request,import_form)
        if import_form:
            initial['state_name'] = import_form.cleaned_data['state_name']
        return initial

    def get_import_data_kwargs(self,request,*args,**kwargs):
        form = kwargs.get('form')
        if form:
            return form.cleaned_data
        return {}
    
    def get_export_resource_kwargs(self,request,*args,**kwargs):
        export_form = kwargs.get('export_form')
        if export_form:
            print(export_form.cleaned_data['state_name'])
            return dict(state_name = export_form.cleaned_data['state_name'])
        return {}
    

    
admin.site.register(VillageMappingFile,VillageMappingFileAdmin)
# admin.site.register(State)
# admin.site.register(VillageLocalityModel)
admin.site.register(VillageBoundaryModel)