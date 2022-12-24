from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")


class MotherboardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_html_photo', 'is_published', 'cost', 'manufactured', 'platforms')
    list_display_links = ('id', 'name',)
    search_fields = ('name', 'cost', 'manufactured')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'name')
    prepopulated_fields = {"slug": ("name",)}
    fields = (
        'name', 'slug', 'cat', 'photo', 'is_published', 'cost', 'content', 'manufactured', 'sockets', 'form_factor',
        'chipsets',
        'platforms', 'memory_type', 'power_phase', 'max_volume', 'slots', 'frequency')
    readonly_fields = ('get_html_photo',)
    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")


admin.site.register(Categories, CategoryAdmin)
admin.site.register(Motherboard, MotherboardAdmin)
