# Generated by Django 3.2.9 on 2021-11-29 10:35

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0008_auto_20211129_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pur_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 29, 10, 35, 26, 307838, tzinfo=utc), verbose_name='Date and Time of purchase'),
        ),
        migrations.AlterField(
            model_name='orderthing',
            name='console',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='gamestore.console'),
        ),
        migrations.AlterField(
            model_name='orderthing',
            name='game',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='gamestore.game'),
        ),
        migrations.AlterField(
            model_name='orderthing',
            name='item',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='gamestore.item'),
        ),
        migrations.AlterField(
            model_name='orderthing',
            name='order',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='gamestore.order'),
        ),
        migrations.AlterField(
            model_name='orderthing',
            name='pc',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='gamestore.pc'),
        ),
    ]
