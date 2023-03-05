from django.urls import path, include

from . import views


urlpatterns = [
    path("pets/my", views.MyPetsListCreateView.as_view(), name="my_pets"),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
