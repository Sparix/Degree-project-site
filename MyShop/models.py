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
    manufactured = models.CharField(max_length=100, help_text="Виробник")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Categories', on_delete=models.PROTECT)
    cost = models.IntegerField()


class Motherboard(Product):
    form_factor = models.CharField(max_length=100, blank=True, verbose_name='Форм-фактор', help_text="Форм-фактор")
    sockets = models.CharField(max_length=100, blank=True, verbose_name='Сокет', help_text="Роз'єм (Socket)")
    chipsets = models.CharField(max_length=100, blank=True, verbose_name='Чіпсет', help_text="Чіпсет")
    platforms = models.CharField(max_length=100, blank=True, verbose_name='Платформа', help_text="Платформа")
    memory_type = models.CharField(max_length=100, blank=True, verbose_name='Тип памяті', help_text="Тип пам'яті")
    power_phase = models.CharField(max_length=100, blank=True, verbose_name='Кільскість фаз живлення',
                                   help_text="Кількість фаз живлення")
    max_volume = models.CharField(max_length=100, blank=True, verbose_name='Максимальний обсяг',
                                  help_text="Максимальний обсяг")
    slots = models.CharField(max_length=100, blank=True, verbose_name='Кількість слотів', help_text="Кількість слотів")
    frequency = models.CharField(max_length=100, blank=True, verbose_name='Частота', help_text="Частота")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug, })

    class Meta:
        ordering = ['-cost', 'name']


'''class Videocard(Product):
    model_card = models.CharField(max_length=100, blank=True, verbose_name='Модель', help_text="Модель")
    power = models.CharField(max_length=100, blank=True, verbose_name='Додаткове живлення', help_text="Живлення")
    memory = models.CharField(max_length=100, blank=True, verbose_name="Обсяг пам'яті", help_text="Обсяг пам'яті")
    type_memory = models.CharField(max_length=100, blank=True, verbose_name="Тип пам'яті", help_text="Тип пам'яті")
    memory_frequency = models.CharField(max_length=100, blank=True, verbose_name="Частота пам'яті",
                                        help_text="Частота пам'яті")
    core_gpu = models.CharField(max_length=100, blank=True, verbose_name="Частота ядра",
                                help_text="Частота ядра GPU")
    mini_power = models.CharField(max_length=100, blank=True, default='-',
                                  verbose_name="Необхідна потужність БЖ",
                                  help_text="Необхідна потужність БЖ")
    version_DirectX = models.CharField(max_length=100, blank=True, verbose_name="Версія DirectX",
                                       help_text="Версія DirectX")
    type_cooling = models.CharField(max_length=100, blank=True, verbose_name="Тип охолодження",
                                    help_text="Тип охолодження")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug, })

    class Meta:
        ordering = ['-cost', 'name']'''