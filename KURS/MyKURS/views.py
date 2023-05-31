from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm

def index_page(request):
    return render(request, 'index.html')

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def login_page(request):
    return render(request, 'login.html')

def profile_view(request):
    return render(request, 'profile.html')

#def WebPasswordResetView(PasswordResetView):
#    pass