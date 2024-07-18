from rest_framework import serializers
from .models import Feature, EarlyAccessSignup

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ['id', 'title', 'description', 'icon']

class EarlyAccessSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = EarlyAccessSignup
        fields = ['email']
