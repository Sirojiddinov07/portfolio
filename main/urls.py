from django.urls import path
from main.views import * 




urlpatterns = [
    path('', index, name='index'),
    path('project_detail/<int:pk>/', project_detail, name='project_detail'),
    path('blog_detail/<int:pk>/', blog_detail, name='blog_detail'),

]