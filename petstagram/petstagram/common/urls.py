from django.urls import path
from petstagram.common import views
from django.conf.urls.static import static
from petstagram import settings

urlpatterns = (
    path('', views.show_home_page, name='home'),
)
