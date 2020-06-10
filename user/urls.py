from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('get_user/',views.get_user,name='get_user'),
    path('add_user/',views.add_user,name='add_user'),
    path('edit_user/',views.edit_user,name='edit_user'),
]
