from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('la/', views.la, name='la'),
    path('paris/', views.paris, name='paris'),
    path('tokyo/', views.tokyo, name='tokyo'),
    path('hk/', views.hk, name='hk'),
    path('reindex/', views.reindex, name='reindex'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'), 
    path('delete/<int:pk>', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
]