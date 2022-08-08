# Generated by Django 4.0.6 on 2022-08-08 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_user_birthday'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birthday',
        ),
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
    ]
