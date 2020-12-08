from django.urls import path
from myapp import views

app_name = 'myapp'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('add/', views.add, name = 'add'),
    path('info/', views.info, name = 'info'),
    path('update/', views.update, name = 'update'),
    path('delete/', views.delete, name = 'delete'),
    
]
