from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    list_display_links = ('id', 'username')
    search_fields = ('username', 'email')
    ordering = ('id',)
