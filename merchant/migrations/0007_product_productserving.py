# Generated by Django 4.1 on 2023-04-23 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchant', '0006_ratings'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='productServing',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]
