# Generated by Django 3.2.9 on 2021-11-29 10:29

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0006_auto_20211128_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='console',
            name='accessories',
            field=models.ForeignKey(blank=True, default='None', null=True, on_delete=django.db.models.deletion.CASCADE, to='gamestore.item'),
        ),
        migrations.AlterField(
            model_name='device',
            name='device',
            field=models.CharField(default='None', max_length=30),
        ),
        migrations.AlterField(
            model_name='order',
            name='pur_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 29, 10, 29, 27, 875550, tzinfo=utc), verbose_name='Date and Time of purchase'),
        ),
    ]
