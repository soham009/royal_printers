# Generated by Django 2.2.2 on 2019-07-24 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_order_management', '0009_purchaseorder_purchase_order_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='purchase_order_amount_due',
            field=models.FloatField(default=1000),
            preserve_default=False,
        ),
    ]
