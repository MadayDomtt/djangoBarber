from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class resourceBarberia (resources.ModelResource):
    class Meta:
        model = barberia

class adminBarberia(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['nombre', 'direccion', 'telefono']
    resource_class = resourceBarberia

admin.site.register(barberia, adminBarberia)

class resourceServicios(resources.ModelResource):
    class Meta:
        model = servicios

class adminServicios(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['pk_servicios']
    list_display = ['tipo','precio','descuento']
    resource_class = resourceServicios

admin.site.register(servicios, adminServicios)

class resourceEmpleados(resources.ModelResource):
    class Meta:
        model = empleados

class adminEmpleados(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['pk_empleados']
    list_display = ['nombre', 'apellidos', 'telefono','fk_barberia']
    resource_class = resourceEmpleados

admin.site.register(empleados, adminEmpleados)

class resourceCliente(resources.ModelResource):
    class Meta:
        model = cliente

class adminCliente(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['nombre', 'apellidos', 'c_cita','fk_barberia', 'fk_servicios']
    resource_class = resourceCliente

admin.site.register(cliente, adminCliente)

class resourceCita(resources.ModelResource):
    class Meta:
        model = cita

class adminCita(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['fecha']
    list_display = ['fecha','horario','fk_cliente']
    resource_class = resourceCita

admin.site.register(cita, adminCita)

