# Generated by Django 2.2.2 on 2019-07-30 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_order_management', '0033_remove_punch_punch_size'),
    ]

    operations = [
        migrations.RenameField(
            model_name='block',
            old_name='block_no_of',
            new_name='block_number_of_sheets',
        ),
        migrations.RemoveField(
            model_name='block',
            name='block_size',
        ),
    ]
