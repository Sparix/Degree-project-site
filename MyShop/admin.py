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


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_html_photo', 'is_published', 'cost')
    list_display_links = ('id', 'name',)
    search_fields = ('name', 'cost')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'name')
    prepopulated_fields = {"slug": ("name",)}
    fields = ('name', 'slug', 'cat', 'photo', 'is_published', 'cost', 'content',)
    readonly_fields = ('get_html_photo',)
    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")


admin.site.register(Categories, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
