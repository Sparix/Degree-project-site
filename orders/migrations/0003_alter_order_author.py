# Generated by Django 4.0.1 on 2023-03-15 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='author',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
