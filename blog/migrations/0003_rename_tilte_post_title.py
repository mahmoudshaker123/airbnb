# Generated by Django 4.1.3 on 2023-05-19 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tilte',
            new_name='title',
        ),
    ]
