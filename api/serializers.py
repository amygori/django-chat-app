from rest_framework import serializers


from .models import Pet, User


class PetSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(slug_field="username", read_only=True)
    class Meta:
      model = Pet
      fields = ("pk", "name", "type", "owner",)
