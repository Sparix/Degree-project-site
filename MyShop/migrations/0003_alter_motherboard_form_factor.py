# Generated by Django 4.0.4 on 2023-01-11 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyShop', '0002_alter_product_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motherboard',
            name='form_factor',
            field=models.CharField(blank=True, help_text='Форм-фактор', max_length=100, verbose_name='Форм-фактор'),
        ),
    ]
