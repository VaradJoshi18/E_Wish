# Generated by Django 4.1 on 2023-04-22 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchant', '0003_remove_product_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='productRating',
            field=models.TextField(default=5, max_length=150),
            preserve_default=False,
        ),
    ]
