from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    #path('password_reset/', views.WebPasswordResetView.as_view(), name='password_reset'),
]