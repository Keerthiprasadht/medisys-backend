from django.urls import path
from .views import create_hospital, get_hospitals

urlpatterns = [
    path('api/hospitals/', create_hospital, name='create-hospital'),
    path('api/hospitals/all/', get_hospitals, name='get-hospitals'),
]
