from django.urls import path
from . import views 

urlpatterns = [
    path('', views.cock, name='cock'),
]