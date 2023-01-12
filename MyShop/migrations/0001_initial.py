# Generated by Django 4.0.4 on 2023-01-09 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('photo', models.ImageField(upload_to='photos/categories')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('content', models.TextField(blank=True)),
                ('manufactured', models.CharField(max_length=100)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
                ('cost', models.IntegerField()),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MyShop.categories')),
            ],
        ),
        migrations.CreateModel(
            name='Motherboard',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MyShop.product')),
                ('form_factor', models.CharField(blank=True, max_length=100, verbose_name='Форм-фактор')),
                ('sockets', models.CharField(blank=True, max_length=100, verbose_name='Сокет')),
                ('chipsets', models.CharField(blank=True, max_length=100, verbose_name='Чіпсет')),
                ('platforms', models.CharField(blank=True, max_length=100, verbose_name='Платформа')),
                ('memory_type', models.CharField(blank=True, max_length=100, verbose_name='Тип памяті')),
                ('power_phase', models.CharField(blank=True, max_length=100, verbose_name='Кільскість фаз живлення')),
                ('max_volume', models.CharField(blank=True, max_length=100, verbose_name='Максимальний обсяг')),
                ('slots', models.CharField(blank=True, max_length=100, verbose_name='Кількість слотів')),
                ('frequency', models.CharField(blank=True, max_length=100, verbose_name='Частота')),
            ],
            options={
                'ordering': ['-cost', 'name'],
            },
            bases=('MyShop.product',),
        ),
    ]
