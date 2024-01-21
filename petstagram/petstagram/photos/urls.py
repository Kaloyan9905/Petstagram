from django.urls import path
from petstagram.photos import views

urlpatterns = (
    path('add/', views.add_photo, name='add-photo'),
    path('<int:pk>/', views.show_photo_details, name='photo-details'),
    path('edit/<int:pk>/', views.edit_photo, name='edit-photo'),
    path('delete/<int:pk>/', views.delete_photo, name='delete-photo'),
)


