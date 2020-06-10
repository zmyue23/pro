from django.urls import path
from picture import views

app_name='picture'

urlpatterns = [
    path('get_map/',views.get_map,name='get_map'),
    path('get_data/',views.get_data,name='get_data'),
]
