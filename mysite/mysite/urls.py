from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index, name='index'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update')
    
]
