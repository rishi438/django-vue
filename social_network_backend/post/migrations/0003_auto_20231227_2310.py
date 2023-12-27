# Generated by Django 3.2.12 on 2023-12-27 17:40

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0002_alter_post_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes_count',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4,
                 editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, to='post.Like'),
        ),
    ]
