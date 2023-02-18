from django.urls import path

from . import views


urlpatterns = [
    path("pets/my", views.MyPetsListCreateView.as_view(), name="my_pets"),
]
