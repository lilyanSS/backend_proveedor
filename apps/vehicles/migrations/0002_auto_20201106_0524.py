# Generated by Django 2.2.16 on 2020-11-06 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='image_url',
            field=models.ImageField(blank=True, upload_to='static/photos'),
        ),
    ]
