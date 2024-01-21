from django.urls import path
from petstagram.pets import views

urlpatterns = (
    path('add/', views.add_pet, name='add-pet'),
    path('<str:username>/pet/<slug:pet_slug>/', views.show_pet_details, name='pet-details'),
    path('<str:username>/pet/<slug:pet_slug>/edit/', views.edit_pet, name='edit-pet'),
    path('<str:username>/pet/<slug:pet_slug>/delete/', views.delete_pet, name='delete-pet'),
)
