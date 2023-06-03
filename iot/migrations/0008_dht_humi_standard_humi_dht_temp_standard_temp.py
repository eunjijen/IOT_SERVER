# Generated by Django 4.1.7 on 2023-05-23 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("iot", "0007_controlaircon_controldehumidifier_controlheater_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="dht_humi",
            name="standard_humi",
            field=models.FloatField(default=65),
        ),
        migrations.AddField(
            model_name="dht_temp",
            name="standard_temp",
            field=models.FloatField(default=24),
        ),
    ]
