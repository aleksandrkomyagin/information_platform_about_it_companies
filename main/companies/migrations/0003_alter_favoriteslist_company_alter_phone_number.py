# Generated by Django 4.1 on 2023-11-18 19:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("companies", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="phone",
            name="number",
            field=models.CharField(default="undefined", max_length=18),
            preserve_default=False,
        ),
    ]
