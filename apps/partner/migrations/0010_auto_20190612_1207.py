# Generated by Django 2.2.2 on 2019-06-12 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0009_auto_20190611_1506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockrecord',
            name='currency',
        ),
        migrations.AlterField(
            model_name='stockrecord',
            name='price_currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partner.Currency'),
        ),
    ]
