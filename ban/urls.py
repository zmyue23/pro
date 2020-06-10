from django.urls import path
from ban import views

app_name='ban'

urlpatterns = [
    path('get_banner/',views.get_banner,name='get_banner'),
    path('add_banner/',views.add_banner,name='add_banner'),
    path('edit_banner/',views.edit_banner,name='edit_banner'),

]
