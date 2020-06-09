from django.urls import path
from . import views
urlpatterns = [
    path('', views.PersonCreateView.as_view(), name='person_add'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
    path('ajax/load_vehicle_types/', views.load_vehicle_type, name='ajax_load_vehicle_type'),
]
