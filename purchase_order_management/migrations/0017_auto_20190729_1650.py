# Generated by Django 2.2.2 on 2019-07-29 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_order_management', '0016_auto_20190729_1349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='specialprocess',
            old_name='special_process_type',
            new_name='specialprocess_type',
        ),
    ]