from django.shortcuts import render


# Create your views here.
def add_pet(request):
    return render(request, template_name='pets/pet-add-page.html')


def show_pet_details(request, username, pet_slug):
    return render(request, template_name='pets/pet-details-page.html')


def edit_pet(request, username, pet_slug):
    return render(request, template_name='pets/pet-edit-page.html')


def delete_pet(request, username, pet_slug):
    return render(request, template_name='pets/pet-delete-page.html')
