# Generated by Django 3.2.23 on 2024-02-08 20:16

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0007_rename_hash_tag_trends_hashtag"),
    ]

    operations = [
        migrations.AddField(
            model_name="trends",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]