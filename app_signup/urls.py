from django.urls import path
from .views import *

urlpatterns = [
    path('', SignupView.as_view()),
    # path('AccountActivation/', AccountActivationView.as_view())
]
