# Generated by Django 2.2.2 on 2019-07-30 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_order_management', '0027_remove_cutting_cutting_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='punching',
            name='punching_size',
        ),
    ]
