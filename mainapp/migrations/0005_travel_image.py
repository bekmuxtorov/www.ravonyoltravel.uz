# Generated by Django 4.0.6 on 2022-07-20 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_rename_qoliq_mal_travel_toliq_mal'),
    ]

    operations = [
        migrations.AddField(
            model_name='travel',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
