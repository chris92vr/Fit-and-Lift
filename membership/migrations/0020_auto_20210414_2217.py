# Generated by Django 3.1.7 on 2021-04-14 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0019_auto_20210414_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='usermembership',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]
