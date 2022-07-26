# Generated by Django 4.0.6 on 2022-07-25 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_fikrlar'),
    ]

    operations = [
        migrations.AddField(
            model_name='fikrlar',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default='21/07/2022'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fikrlar',
            name='text',
            field=models.TextField(max_length=300, verbose_name='Fikrlaringizni kiriting: '),
        ),
    ]
