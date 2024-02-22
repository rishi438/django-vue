# -*- coding: utf-8 -*-

import os
import sys
from datetime import timedelta

import django
from django.utils import timezone

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "social_network_backend.settings")
django.setup()

from collections import Counter

from post.models import Post, Trends


def extract_hastags(text, trends):
    """This funtion extracts Hastags

    Args:
        text (str): hastag text
        trends (list): empty list

    Returns:
        trends(list): list of words with most comman tags
    """
    for word in text.split():
        if word[0] == "#":
            trends.append(word[1:])
    return trends


this_hour = timezone.now().replace(minute=0, second=0, microsecond=0)
twenty_four_hrs = this_hour - timedelta(hours=24)

for trend in Trends.objects.all():
    trend.delete()

trends = []
for post in Post.objects.filter(created_at__gte=twenty_four_hrs):
    extract_hastags(post.body, trends)

for trend in Counter(trends).most_common(10):
    Trends.objects.create(hashtag=trend[0], occurences=trend[1])
