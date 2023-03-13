from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


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
    manufactured = models.CharField(max_length=100, db_index=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Categories', on_delete=models.PROTECT)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    content = models.JSONField(default=dict)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug, })

    class Meta:
        ordering = ['-cost', 'name']


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="profile_images", verbose_name='Изображение')

    def __unicode__(self):
        return self.user

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
