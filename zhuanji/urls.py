from django.urls import path

from zhuanji import views

app_name = 'album'

urlpatterns = [
    path('get_list/', views.get_list),
    path('add/', views.add),
    path('edit/', views.edit),
    path('chapters_ofalbum/', views.chapters_ofalbum),
    path('chapter_add/', views.chapter_add),
    path('chapter_edit/', views.chapter_edit),
]