# Generated by Django 3.1.7 on 2021-04-12 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0014_auto_20210412_2316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='member_profile',
        ),
    ]
