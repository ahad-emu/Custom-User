from django.contrib import admin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUserModel
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUserModel
    list_display = ['username', 'first_name','last_name', 'email', 'age', 'is_staff']

admin.site.register(CustomUserModel, CustomUserAdmin)