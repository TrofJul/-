from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.file, name='file'),
    path('create/', views.create, name='create'),
    path('<int:id>/delete_file', views.delete_file, name='delete_file'),
    path('<int:id>/edit_file', views.edit_file, name='edit_file'),
    path('<int:id>/edit_done', views.edit_done, name='edit_done')
]
