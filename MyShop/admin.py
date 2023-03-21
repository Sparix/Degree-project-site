from django.contrib import admin
from django.utils.safestring import mark_safe
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

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
    list_display = ('id', 'name', 'get_html_photo', 'is_published', 'cost', 'content', 'manufactured')
    list_display_links = ('id', 'name',)
    search_fields = ('name', 'cost', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'name')
    prepopulated_fields = {"slug": ("name",)}
    fields = (
        'name', 'slug', 'cat', 'photo', 'is_published', 'cost', 'content', 'manufactured')
    readonly_fields = ('get_html_photo',)
    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")


'''class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_html_photo')
    list_display_links = ('user',)
    search_fields = ('user',)

    def get_html_photo(self, object):
        if object.avatar:
            return mark_safe(f"<img src='{object.avatar.url}' width=50>")
'''


class UserInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Доп. информация'


# Определяем новый класс настроек для модели User
class AdminUser(UserAdmin):
    inlines = (UserInline,)


# Перерегистрируем модель User
admin.site.unregister(User)
admin.site.register(User, AdminUser)

admin.site.register(Comment)
admin.site.register(Categories, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
'''admin.site.register(Videocard, VideoCardAdmin)'''
