# Generated by Django 3.1.7 on 2021-02-25 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_has_sizes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('brief_desc', models.TextField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('frequency', models.CharField(choices=[('', 'Select Payment Frequency Type'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('biannual', 'Biannual'), ('yearly', 'Yearly')], max_length=29)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]