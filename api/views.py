from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import PetSerializer
from .models import Pet

# Create your views here.
class MyPetsListCreateView(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.pets.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
