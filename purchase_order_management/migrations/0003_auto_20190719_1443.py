# Generated by Django 2.2.2 on 2019-07-19 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_order_management', '0002_process_process_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=200)),
                ('client_amount', models.FloatField()),
                ('client_amount_due', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='purchaseorder',
            name='purchase_order_client_name',
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='purchase_order_client_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='purchase_order_management.Client'),
            preserve_default=False,
        ),
    ]
