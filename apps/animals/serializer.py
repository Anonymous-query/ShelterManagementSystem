from rest_framework import serializers
from apps.animals.models import AdoptionRequest, Animals

class AnimalSerializer(serializers.ModelSerializer):
    species = serializers.CharField(source="species.name")
    breed = serializers.CharField(source="breed.name")
    
    class Meta:
        model = Animals
        fields = ['id', 'species', 'breed', 'age', 'health_status', 'adoption_status']


class AdoptionRequestSerializer(serializers.ModelSerializer):
     class Meta:
        model = AdoptionRequest
        fields = ['id', 'user', 'animal', 'status']