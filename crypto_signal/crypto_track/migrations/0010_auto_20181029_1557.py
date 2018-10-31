# Generated by Django 2.1.2 on 2018-10-29 14:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_track', '0009_auto_20181029_1500'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CryptoCandleHistory',
        ),
        migrations.AddField(
            model_name='pytrends',
            name='trend_ratio',
            field=models.DecimalField(decimal_places=5, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='cryptocandle',
            name='update_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 29, 14, 57, 6, 806700, tzinfo=utc)),
        ),
    ]
