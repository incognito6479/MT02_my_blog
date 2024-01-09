from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home_view'),
    path('login/', LoginView.as_view(), name='login_view'),
    path('register/', RegisterView.as_view(), name='register_view'),
]