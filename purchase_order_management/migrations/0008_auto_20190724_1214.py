# Generated by Django 2.2.2 on 2019-07-24 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_order_management', '0007_auto_20190724_1209'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchaseorder',
            old_name='purchase_order_no_cols',
            new_name='purchase_order_number_of_columns',
        ),
    ]
