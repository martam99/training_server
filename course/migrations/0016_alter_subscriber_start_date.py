# Generated by Django 4.2.5 on 2023-10-17 12:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0015_alter_subscriber_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 17, 12, 39, 25, 357533, tzinfo=datetime.timezone.utc), verbose_name='дата подписки'),
        ),
    ]
