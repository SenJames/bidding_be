# Generated by Django 4.1.7 on 2023-12-13 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bidding_app", "0006_alter_bid_recipient"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bid",
            name="time",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
