# Generated by Django 5.0.4 on 2024-04-22 05:30

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='color',
            field=models.CharField(choices=[('Black', 'Black'), ('White', 'White')], default=django.utils.timezone.now, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='phone',
            name='description',
            field=models.TextField(default=django.utils.timezone.now, verbose_name='Описание'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='phone',
            name='memory',
            field=models.CharField(choices=[('256 GB', 'Gb256'), ('512 GB', 'Gb512'), ('1 TB', 'Tb1')], default=django.utils.timezone.now, max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phone_images', to='images.image', verbose_name='Картинка'),
        ),
    ]
