# Generated by Django 3.1.7 on 2021-02-26 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_remove_orderlineitem_membership'),
        ('products', '0003_membership'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Membership',
        ),
    ]
