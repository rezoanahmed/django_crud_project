from django.urls import path
from myapp import views

app_name = 'myapp'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('add/', views.add, name = 'add'),
    path('info/<int:student_id>/', views.info, name = 'info'),
    path('update/<int:student_id>/', views.update, name = 'update'),
    path('delete/<int:student_id>/', views.delete, name = 'delete'),
    
]
