from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .forms import CustomUserCreationForm, CustomChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserCreationForm
    list_display = ['email', 'username', 'phone_number']
    model = CustomUser

admin.site.register(CustomUser, CustomUserAdmin)