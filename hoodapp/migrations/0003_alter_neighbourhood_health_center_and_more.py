# Generated by Django 4.0.5 on 2022-06-19 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoodapp', '0002_alter_neighbourhood_health_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighbourhood',
            name='health_center',
            field=models.CharField(default=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='neighbourhood',
            name='health_email',
            field=models.EmailField(default=True, max_length=100),
        ),
    ]
