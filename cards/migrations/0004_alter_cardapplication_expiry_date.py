# Generated by Django 5.0.2 on 2024-02-27 10:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cards", "0003_alter_cardapplication_expiry_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cardapplication",
            name="expiry_date",
            field=models.DateField(
                default=datetime.datetime(2024, 2, 27, 15, 43, 44, 182092)
            ),
        ),
    ]