# Generated by Django 5.0.2 on 2024-02-27 04:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cards", "0002_alter_cardapplication_expiry_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cardapplication",
            name="expiry_date",
            field=models.DateField(
                default=datetime.datetime(2024, 2, 27, 10, 8, 1, 726243)
            ),
        ),
    ]