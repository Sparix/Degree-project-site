# Generated by Django 4.0.4 on 2022-12-23 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyShop', '0002_motherboard_sockets'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='motherboard',
            options={'ordering': ['-cost', 'name']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={},
        ),
    ]