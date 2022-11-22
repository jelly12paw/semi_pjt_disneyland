from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
    path('signup/', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('delete/', views.delete, name='delete'),
]