# Generated by Django 3.1.7 on 2021-04-14 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0016_auto_20210414_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='slug',
            field=models.SlugField(default=1, max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='usermembership',
            name='slug',
            field=models.SlugField(default=1, max_length=255, unique=True),
        ),
    ]