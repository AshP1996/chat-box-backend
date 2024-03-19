from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils import timezone  # Import timezone module
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    ordering = ['email']
    list_display = ['email', 'first_name', 'last_name', 'is_active', 'is_staff']

    # Override init method to set related names
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        CustomUser._meta.get_field('groups').remote_field.related_name = 'customuser_groups'
        CustomUser._meta.get_field('user_permissions').remote_field.related_name = 'customuser_user_permissions'

admin.site.register(CustomUser, CustomUserAdmin)
