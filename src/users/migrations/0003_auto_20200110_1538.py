# Generated by Django 2.2.5 on 2020-01-10 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_auto_20200110_1530"),
    ]

    operations = [
        migrations.AddField(
            model_name="user", name="birth_date", field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="currency",
            field=models.CharField(
                blank=True,
                choices=[("usd", "USD"), ("usd", "KRW")],
                max_length=3,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="is_super_host",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="language",
            field=models.CharField(
                blank=True,
                choices=[("en", "Male"), ("kr", "Female")],
                max_length=2,
                null=True,
            ),
        ),
    ]
