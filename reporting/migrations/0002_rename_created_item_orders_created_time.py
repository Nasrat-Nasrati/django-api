# Generated by Django 5.2 on 2025-04-12 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='created_item',
            new_name='created_time',
        ),
    ]
