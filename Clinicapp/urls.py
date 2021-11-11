from django.urls import path
from .views import RegisterView

urlpattern = [
    path('register/', RegisterView.as_view(), name="register")
]