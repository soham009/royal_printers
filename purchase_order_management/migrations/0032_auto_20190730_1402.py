# Generated by Django 2.2.2 on 2019-07-30 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_order_management', '0031_remove_creasing_creasing_size'),
    ]

    operations = [
        migrations.RenameField(
            model_name='punch',
            old_name='punch_no_of',
            new_name='punch_number_of_sheets',
        ),
    ]
