# Generated by Django 4.2.5 on 2023-10-16 11:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_alter_subscriber_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 16, 11, 27, 50, 518041, tzinfo=datetime.timezone.utc), verbose_name='дата подписки'),
        ),
    ]
