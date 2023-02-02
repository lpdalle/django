from rest_framework import serializers

from api import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'


class GenerationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Generation
        fields = '__all__'


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Images
        fields = '__all__'
