# Generated by Django 4.1.7 on 2023-05-24 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("iot", "0008_dht_humi_standard_humi_dht_temp_standard_temp"),
    ]

    operations = [
        migrations.CreateModel(
            name="StandardHumidity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("standard_humi", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="StandardTemperature",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("standard_temp", models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name="dht_humi",
            name="standard_humi",
        ),
        migrations.RemoveField(
            model_name="dht_temp",
            name="standard_temp",
        ),
    ]