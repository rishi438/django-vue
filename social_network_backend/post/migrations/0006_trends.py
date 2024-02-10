# Generated by Django 3.2.23 on 2024-02-07 20:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0005_auto_20240108_2123"),
    ]

    operations = [
        migrations.CreateModel(
            name="Trends",
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
                ("hash_tag", models.CharField(max_length=255)),
                ("occurences", models.IntegerField()),
            ],
        ),
    ]