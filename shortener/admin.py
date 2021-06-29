from django.contrib import admin
from .models import ShortURL


@admin.register(ShortURL)
class ShortURLAdmin(admin.ModelAdmin):
    """
    Register ShortURL in the admin for easy management
    """
    fields = ['url', 'hit_count']
