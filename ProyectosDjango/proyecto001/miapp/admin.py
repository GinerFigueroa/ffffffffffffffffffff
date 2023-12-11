from django.contrib import admin
from .models import Course

# Register your models here.

# Configuración del ModelAdmin para Curso
class CourseAdmin(admin.ModelAdmin):
    list_display = ('idcourse', 'code', 'name', 'hour', 'credits', 'state')
    list_filter = ('state',)
    search_fields = ('code', 'name')
