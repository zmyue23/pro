from django.urls import path
from index import views

app_name='index'

urlpatterns = [
    path('index/',views.index,name='index'),
    path('photo/',views.photo,name='photo'),
    path('login/',views.login,name='login'),
    path('code/',views.code,name='code'),
    path('check/',views.check,name='check'),
]
