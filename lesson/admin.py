from django.contrib import admin
from . import models

# Register your models here.


# admin.site.register(models.Material)

@admin.register(models.Material)
class MeterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'material_type', 'publish')
    list_filter = ('created_at', 'updated_at', 'material_type')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title', )}
    date_hierarchy = 'publish'
    ordering = ('material_type', 'publish')