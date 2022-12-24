from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Categories(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    photo = models.ImageField(upload_to="photos/categories")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, db_index=True)
    content = models.TextField(blank=True)
    manufactured = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Categories', on_delete=models.PROTECT)
    cost = models.IntegerField()


class Motherboard(Product):
    form_factor = models.CharField(max_length=100, blank=True, verbose_name='Форм-фактор')
    sockets = models.CharField(max_length=100, blank=True, verbose_name='Сокет')
    chipsets = models.CharField(max_length=100, blank=True, verbose_name='Чіпсет')
    platforms = models.CharField(max_length=100, blank=True, verbose_name='Платформа')
    memory_type = models.CharField(max_length=100, blank=True, verbose_name='Тип памяті')
    power_phase = models.CharField(max_length=100, blank=True, verbose_name='Кільскість фаз живлення')
    max_volume = models.CharField(max_length=100, blank=True, verbose_name='Максимальний обсяг')
    slots = models.CharField(max_length=100, blank=True, verbose_name='Кількість слотів')
    frequency = models.CharField(max_length=100, blank=True, verbose_name='Частота')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug, })

    class Meta:
        ordering = ['-cost', 'name']
