# Generated by Django 3.2.12 on 2023-12-25 07:32

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(
                related_name='_account_user_friends_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='FriendRequest',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4,
                 editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[
                 (0, 'SENT'), (1, 'ACCEPTED'), (2, 'REJECTED')], default=0)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='created_friend_request', to=settings.AUTH_USER_MODEL)),
                ('created_for', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='recieved_friend_request', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]