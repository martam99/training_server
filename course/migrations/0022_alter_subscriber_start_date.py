# Generated by Django 4.2.5 on 2023-10-19 11:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0021_alter_subscriber_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='дата подписки'),
        ),
    ]