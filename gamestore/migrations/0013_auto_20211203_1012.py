# Generated by Django 3.2.9 on 2021-12-03 06:12

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0012_auto_20211203_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pur_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 3, 6, 12, 10, 294957, tzinfo=utc), verbose_name='Date and Time of purchase'),
        ),
        migrations.AlterField(
            model_name='orderthing',
            name='order',
            field=models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='gamestore.order'),
        ),
    ]
