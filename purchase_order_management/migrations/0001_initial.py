# Generated by Django 2.2.1 on 2019-07-17 12:59

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_role', models.PositiveSmallIntegerField(choices=[(2, 'admin'), (1, 'super_admin')], default=2)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('process_created_on', models.DateTimeField(auto_now_add=True)),
                ('process_updated_on', models.DateTimeField(auto_now=True)),
                ('process_size', models.CharField(max_length=100)),
                ('process_amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(max_length=200)),
                ('vendor_address', models.CharField(max_length=400)),
                ('vendor_total_amount', models.FloatField()),
                ('vendor_amount_due', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Binding',
            fields=[
                ('process_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='purchase_order_management.Process')),
                ('binding_pf', models.CharField(max_length=100)),
                ('binding_type', models.CharField(choices=[('side', 'side'), ('top', 'top')], max_length=100)),
                ('binding_product', models.CharField(choices=[('book', 'book'), ('pad', 'pad')], max_length=100)),
                ('binding_quantity', models.IntegerField()),
                ('binding_binding_type', models.CharField(choices=[('sada', 'sada'), ('dp', 'dp'), ('threefold', 'threefold'), ('rexin', 'rexin'), ('cloth', 'cloth'), ('packet', 'packet'), ('custom', 'custom')], max_length=100)),
                ('binding_rate', models.FloatField()),
            ],
            bases=('purchase_order_management.process',),
        ),
        migrations.CreateModel(
            name='Block',
            fields=[
                ('process_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='purchase_order_management.Process')),
                ('block_size', models.CharField(max_length=100)),
                ('block_no_of', models.IntegerField()),
            ],
            bases=('purchase_order_management.process',),
        ),
        migrations.CreateModel(
            name='Creasing',
            fields=[
                ('process_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='purchase_order_management.Process')),
                ('creasing_impression', models.FloatField()),
                ('creasing_size', models.CharField(max_length=100)),
                ('creasing_quantity', models.IntegerField()),
                ('creasing_rate', models.FloatField()),
            ],
            bases=('purchase_order_management.process',),
        ),
        migrations.CreateModel(
            name='CTP',
            fields=[
                ('process_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='purchase_order_management.Process')),
                ('ctp_size', models.CharField(max_length=100)),
                ('ctp_type', models.CharField(choices=[('new', 'new'), ('old', 'old')], max_length=100)),
                ('ctp_no_of_plates', models.IntegerField()),
                ('ctp_rate', models.FloatField()),
                ('ctp_quantity', models.FloatField()),
            ],
            bases=('purchase_order_management.process',),
        ),
        migrations.CreateModel(
            name='Cutting',
            fields=[
                ('process_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='purchase_order_management.Process')),
                ('cutting_size', models.CharField(max_length=100)),
                ('cutting_quantity', models.CharField(max_length=100)),
                ('cutting_paper', models.CharField(max_length=100)),
                ('cutting_rate', models.CharField(max_length=100)),
            ],
            bases=('purchase_order_management.process',),
        ),
        migrations.CreateModel(
            name='Folding',
            fields=[
                ('process_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='purchase_order_management.Process')),
                ('folding_no_of_folds', models.IntegerField()),
                ('folding_quantity', models.IntegerField()),
                ('folding_rate', models.IntegerField()),
                ('folding_impression', models.IntegerField()),
            ],
            bases=('purchase_order_management.process',),
        ),
        migrations.CreateModel(
            name='FourCol',
            fields=[
                ('process_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='purchase_order_management.Process')),
                ('fourcol_for', models.CharField(choices=[('vcard', 'vcard'), ('lheads', 'lheads'), ('env', 'env'), ('pamp', 'pamp')], max_length=100)),
                ('fourcol_size', models.FloatField()),
                ('fourcol_type', models.CharField(choices=[('single', 'single'), ('frontback', 'frontback')], max_length=100)),
                ('fourcol_rate', models.FloatField()),
                ('fourcol_unit', models.IntegerField()),
            ],
            bases=('purchase_order_management.process',),
        ),
        migrations.CreateModel(
            name='Lamination',
            fields=[
                ('process_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='purchase_order_management.Process')),
                ('lamination_type', models.CharField(choices=[('pvc', 'pvc'), ('bopp', 'bopp'), ('matt', 'matt'), ('thermal', 'thermal'), ('custom', 'custom')], max_length=100)),
                ('lamination_size', models.CharField(max_length=100)),
                ('lamination_no_of_sheets', models.IntegerField()),
                ('lamination_quantity', models.IntegerField()),
                ('lamination_length', models.FloatField()),
                ('lamination_breadth', models.FloatField()),
                ('lamination_rate', models.FloatField()),
            ],
            bases=('purchase_order_management.process',),
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('process_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='purchase_order_management.Process')),
                ('paper_color', models.CharField(max_length=100)),
                ('paper_gsm', models.CharField(max_length=100)),
                ('paper_no_of_sheets', models.IntegerField()),
                ('paper_quantity', models.IntegerField()),
                ('paper_rate', models.FloatField()),
            ],
            bases=('purchase_order_management.process',),
        ),
        migrations.CreateModel(
            name='Pasting',
            fields=[
                ('process_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='purchase_order_management.Process')),
                ('pasting_impression', models.FloatField()),
                ('pasting_size', models.CharField(max_length=100)),
                ('pasting_no_of_pasting', models.IntegerField()),
                ('pasting_quantity', models.IntegerField()),
                ('pasting_rate', models.FloatField()),
            ],
            bases=('purchase_order_management.process',),
        ),
        migrations.CreateModel(
            name='Positive',
            fields=[
                ('process_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='purchase_order_management.Process')),
                ('positive_type', models.CharField(choices=[('pvc', 'pvc'), ('bopp', 'bopp'), ('matt', 'matt'), ('thermal', 'thermal'), ('custom', 'custom')], max_length=100)),
                ('positive_size', models.CharField(max_length=100)),
                ('positive_no_of_sheets', models.IntegerField()),
                ('positive_quantity', models.IntegerField()),
                ('positive_length', models.FloatField()),
                ('positive_breadth', models.FloatField()),
                ('positive_rate', models.FloatField()),
            ],
            bases=('purchase_order_management.process',),
        ),
        migrations.CreateModel(
            name='Printing',
            fields=[
                ('process_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='purchase_order_management.Process')),
                ('printing_quantity', models.IntegerField()),
                ('printing_detail', models.CharField(max_length=300)),
                ('printing_no_of_cols', models.IntegerField()),
                ('printing_impression', models.FloatField()),
                ('printing_rate', models.FloatField()),
            ],
            bases=('purchase_order_management.process',),
        ),
        migrations.CreateModel(
            name='Punch',
            fields=[
                ('process_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='purchase_order_management.Process')),
                ('punch_size', models.CharField(max_length=100)),
                ('punch_no_of', models.IntegerField()),
            ],
            bases=('purchase_order_management.process',),
        ),
        migrations.CreateModel(
            name='Punching',
            fields=[
                ('process_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='purchase_order_management.Process')),
                ('punching_size', models.CharField(max_length=100)),
                ('punching_quantity', models.IntegerField()),
                ('punching_impression', models.FloatField()),
                ('punching_rate', models.FloatField()),
            ],
            bases=('purchase_order_management.process',),
        ),
        migrations.CreateModel(
            name='RaiseUV',
            fields=[
                ('process_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='purchase_order_management.Process')),
                ('raiseuv_type', models.CharField(choices=[('pvc', 'pvc'), ('bopp', 'bopp'), ('matt', 'matt'), ('thermal', 'thermal'), ('custom', 'custom')], max_length=100)),
                ('raiseuv_size', models.CharField(max_length=100)),
                ('raiseuv_no_of_sheets', models.IntegerField()),
                ('raiseuv_quantity', models.IntegerField()),
                ('raiseuv_length', models.FloatField()),
                ('raiseuv_breadth', models.FloatField()),
                ('raiseuv_rate', models.FloatField()),
            ],
            bases=('purchase_order_management.process',),
        ),
        migrations.CreateModel(
            name='SpecialProcess',
            fields=[
                ('process_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='purchase_order_management.Process')),
                ('special_process_type', models.CharField(choices=[('embossing', 'embossing'), ('debossing', 'debossing'), ('foiling', 'foiling')], max_length=100)),
                ('specialprocess_quantity', models.IntegerField()),
                ('specialprocess_impression', models.FloatField()),
                ('specialprocess_size', models.CharField(max_length=100)),
                ('specialprocess_rate', models.FloatField()),
            ],
            bases=('purchase_order_management.process',),
        ),
        migrations.CreateModel(
            name='Varnish',
            fields=[
                ('process_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='purchase_order_management.Process')),
                ('varnish_type', models.CharField(choices=[('pvc', 'pvc'), ('bopp', 'bopp'), ('matt', 'matt'), ('thermal', 'thermal'), ('custom', 'custom')], max_length=100)),
                ('varnish_size', models.CharField(max_length=100)),
                ('varnish_no_of_sheets', models.IntegerField()),
                ('varnish_quantity', models.IntegerField()),
                ('varnish_length', models.FloatField()),
                ('varnish_breadth', models.FloatField()),
                ('varnish_rate', models.FloatField()),
            ],
            bases=('purchase_order_management.process',),
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_order_client_name', models.CharField(max_length=200)),
                ('purchase_order_item', models.CharField(max_length=200)),
                ('purchase_order_item_quantity', models.IntegerField()),
                ('purchase_order_size', models.CharField(max_length=200)),
                ('purchase_order_no_cols', models.IntegerField(blank=True)),
                ('purchase_order_date_created_on', models.DateTimeField(auto_now_add=True)),
                ('purchase_order_date_updated_on', models.DateTimeField(auto_now=True)),
                ('purchase_order_process_relation', models.ManyToManyField(to='purchase_order_management.Process')),
                ('purchase_order_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='process',
            name='process_vendor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchase_order_management.Vendor'),
        ),
    ]
