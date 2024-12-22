from django.urls import path
from . import views

urlpatterns = [
    path('', views.subject_input, name='subject_input'),  # Subject selection page
    path('upload/<int:subject_id>/', views.file_upload, name='file_upload'),  # File upload page
]
