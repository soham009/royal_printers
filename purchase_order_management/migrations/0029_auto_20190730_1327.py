# Generated by Django 2.2.2 on 2019-07-30 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_order_management', '0028_remove_punching_punching_size'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pasting',
            old_name='pasting_no_of_pasting',
            new_name='pasting_number_of_pasting',
        ),
        migrations.RemoveField(
            model_name='pasting',
            name='pasting_size',
        ),
    ]