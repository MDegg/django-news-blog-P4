# Generated by Django 4.0 on 2022-01-10 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0013_comment_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
    ]