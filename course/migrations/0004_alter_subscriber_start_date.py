# Generated by Django 4.2.5 on 2023-10-11 10:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_subscriber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 11, 10, 34, 29, 882470, tzinfo=datetime.timezone.utc), verbose_name='дата подписки'),
        ),
    ]