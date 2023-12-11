from django.contrib import admin

# Register your models here.

# Configuración del ModelAdmin para Curso
class CourseAdmin(admin.ModelAdmin):
    list_display = ('idcourse', 'code', 'name', 'hour', 'credits', 'state')
    list_filter = ('state',)
    search_fields = ('code', 'name')

# Configuración del ModelAdmin para Carrera
class CareerAdmin(admin.ModelAdmin):
    list_display = ('idcareer', 'name', 'shortname', 'image', 'state')
    list_filter = ('state',)
    search_fields = ('name', 'shortname')