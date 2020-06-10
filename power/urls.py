from django.urls import path
from power import views
app_name = 'power'

urlpatterns = [
    path('r_login/', views.r_login, name='r_login'),
    path('check_user/', views.check_user, name='check_user'),
]