from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    # Add other URL patterns as needed
]
