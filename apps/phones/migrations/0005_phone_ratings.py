# Generated by Django 5.0.4 on 2024-04-23 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0004_phone_is_active_phone_is_exists'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='ratings',
            field=models.FloatField(default=0, verbose_name='Оценка'),
        ),
    ]