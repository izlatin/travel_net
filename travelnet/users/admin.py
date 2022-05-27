from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserCreationForm
from .models import Profile, CustomUser


class ProfileInlined(admin.StackedInline):
    model = Profile
    can_delete = False


class CustomUserAdmin(BaseUserAdmin):
    model = CustomUser
    fieldsets = ((None, {
        'fields': ('username', 'email', 'image')
    }),)
    list_display = ('username', 'email', 'image_tmb', 'is_staff', 'is_active',)
    list_filter = ('username', 'email', 'is_staff', 'is_active',)
    inlines = (ProfileInlined,)
    ordering = ('username',)
    add_form = UserCreationForm


admin.site.register(CustomUser, CustomUserAdmin)
