# Generated by Django 4.0.5 on 2022-06-19 11:16

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoodapp', '0004_alter_neighbourhood_authority_center_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighbourhood',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='neighbourhood',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
