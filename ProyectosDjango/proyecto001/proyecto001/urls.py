from django.contrib import admin
from django.urls import path, include
from miapp.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('miapp/', include('miapp.urls')),
    path('', include('miapp.urls')),  # Añade esta línea para manejar la URL raíz
]
