# Generated by Django 4.0.6 on 2022-07-20 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweeter_api', '0003_rename_likes_tweet_tweet_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='tweet_likes',
        ),
    ]