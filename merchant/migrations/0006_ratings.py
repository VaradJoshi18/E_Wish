# Generated by Django 4.1 on 2023-04-22 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('merchant', '0005_remove_product_productrating'),
    ]

    operations = [
        migrations.CreateModel(
            name='ratings',
            fields=[
                ('ratingID', models.AutoField(primary_key=True, serialize=False)),
                ('productRating', models.IntegerField(default=5)),
                ('productReview', models.TextField(max_length=500)),
                ('productId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merchant.product')),
            ],
        ),
    ]
