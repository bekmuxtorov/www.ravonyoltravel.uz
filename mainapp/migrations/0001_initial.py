# Generated by Django 4.0.6 on 2022-07-19 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qayerdan', models.CharField(max_length=50)),
                ('qayerga', models.CharField(max_length=50)),
                ('qisqa_mal', models.TextField()),
                ('davomiyligi', models.CharField(max_length=20)),
                ('narxi', models.CharField(max_length=20)),
                ('qoliq_mal', models.TextField()),
            ],
        ),
    ]
