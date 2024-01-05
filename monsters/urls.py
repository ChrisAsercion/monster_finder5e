from django.urls import path
from . import views
from .views import select_cr, index

app_name = 'monsters'

urlpatterns = [
    path('select_cr/', select_cr, name='select_cr'),
    path('index/', index, name='index'),
    # Add other URL patterns as needed
]
