# Generated by Django 4.2.3 on 2023-07-22 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0003_user_is_verified'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Notes',
        ),
    ]