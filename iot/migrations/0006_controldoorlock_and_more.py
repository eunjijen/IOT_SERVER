# Generated by Django 4.1.7 on 2023-05-19 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("iot", "0005_controlcurtain"),
    ]

    operations = [
        migrations.CreateModel(
            name="ControlDoorlock",
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
                ("doorlockcontrol", models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameField(
            model_name="controlcurtain",
            old_name="control",
            new_name="curtaincontrol",
        ),
    ]
