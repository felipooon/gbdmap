from django.urls import path
from . import views

urlpatterns = [
    # Ruta pública para acceder al radar
    path('api/ebird/<path:ebird_path>', views.ebird_proxy, name='ebird_proxy'),
    path('api/diccionario-especies/', views.get_species_dict, name='species_dict'),
]