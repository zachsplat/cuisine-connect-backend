from django.urls import path
from .views import FeatureList, EarlyAccessSignupCreate

urlpatterns = [
    path('features/', FeatureList.as_view()),
    path('signup/', EarlyAccessSignupCreate.as_view()),
]
