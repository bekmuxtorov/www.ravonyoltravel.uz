# Generated by Django 4.0.6 on 2022-10-12 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainapp', '0019_delete_order_alter_rasmlar_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default='9834bd21-c071-4e96-ba51-170cd31afb9f', editable=False, max_length=50)),
                ('is_approved', models.BooleanField(default=False)),
                ('is_payed', models.BooleanField(default=False)),
                ('customer_full_name', models.CharField(max_length=255)),
                ('customer_phone_number', models.CharField(max_length=255)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.travel', verbose_name='Sayohat')),
            ],
        ),
    ]
