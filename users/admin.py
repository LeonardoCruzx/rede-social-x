from django.contrib import admin

from .models import User
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('nick','email','last_login','is_staff','is_superuser')
    list_filter = ('last_login','date_joined')
    search_fields = ['nick','email']
