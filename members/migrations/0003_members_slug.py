# Generated by Django 4.1.6 on 2023-02-23 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_members_joined_date_members_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='slug',
            field=models.SlugField(default='', null=True),
        ),
    ]
