# Generated by Django 3.1.7 on 2021-03-02 23:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0003_auto_20210302_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]