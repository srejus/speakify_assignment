# Generated by Django 4.2.1 on 2023-06-01 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="is_online",
            field=models.BooleanField(default=False),
        ),
    ]
