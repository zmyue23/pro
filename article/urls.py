from django.urls import path
from article import views
app_name = 'article'

urlpatterns = [
    path('get_article/', views.get_article),
    path('pic_upload/', views.upload_img),
    path('get_all_pic/', views.get_img),
    path('add_article/', views.add_article),
    path('edit/', views.edit),
    path('del_article/', views.article_del),
]
