# Generated by Django 4.0.1 on 2023-03-20 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyShop', '0011_comment_name_alter_comment_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='advantages',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='disadvantages',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
