from rest_framework import generics
from .models import Feature, EarlyAccessSignup
from .serializers import FeatureSerializer, EarlyAccessSignupSerializer

class FeatureList(generics.ListAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer

class EarlyAccessSignupCreate(generics.CreateAPIView):
    queryset = EarlyAccessSignup.objects.all()
    serializer_class = EarlyAccessSignupSerializer
