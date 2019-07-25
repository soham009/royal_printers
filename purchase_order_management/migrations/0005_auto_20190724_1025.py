# Generated by Django 2.2.2 on 2019-07-24 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_order_management', '0004_auto_20190719_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='purchase_order_date_purchase_by',
            field=models.DateField(default='2001-01-01'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='purchase_order_date_purchase_date',
            field=models.DateField(default='2001-01-01'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='purchase_order_name',
            field=models.CharField(default='test', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='purchase_order_number',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='purchase_order_po_number',
            field=models.IntegerField(default=200),
            preserve_default=False,
        ),
    ]
