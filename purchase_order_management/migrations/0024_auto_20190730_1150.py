# Generated by Django 2.2.2 on 2019-07-30 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_order_management', '0023_auto_20190730_1139'),
    ]

    operations = [
        migrations.RenameField(
            model_name='positive',
            old_name='positive_no_of_sheets',
            new_name='positive_number_of_sheets',
        ),
    ]