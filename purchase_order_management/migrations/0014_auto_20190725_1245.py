# Generated by Django 2.2.2 on 2019-07-25 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_order_management', '0013_auto_20190725_1224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaseorder',
            name='purchase_order_process_relation',
        ),
        migrations.AddField(
            model_name='process',
            name='process_purchase_order_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='purchase_order_management.PurchaseOrder'),
            preserve_default=False,
        ),
    ]
