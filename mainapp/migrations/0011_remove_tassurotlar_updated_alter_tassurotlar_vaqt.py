# Generated by Django 4.0.6 on 2022-07-21 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_tassurotlar_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tassurotlar',
            name='updated',
        ),
        migrations.AlterField(
            model_name='tassurotlar',
            name='vaqt',
            field=models.DateField(auto_now_add=True, verbose_name='Vaqtni avtomat tanlaydi.'),
        ),
    ]