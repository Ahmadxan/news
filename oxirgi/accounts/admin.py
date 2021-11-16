from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.forms import Textarea

from accounts.models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    search_fields = ('email', 'username', 'full_name',)
    list_filter = ('email', 'username', 'full_name', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('email', 'username', 'full_name',
                    'is_active', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'full_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('about',)}),
        ('Group Permissions', {
            'classes': ('collapse',),
            'fields': ('groups', 'user_permissions',)
        })
    )
    formfield_overrides = {
        CustomUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'full_name', 'password1', 'password2', 'groups', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
