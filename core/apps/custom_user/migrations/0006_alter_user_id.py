# Generated by Django 5.0.7 on 2024-08-06 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("custom_user", "0005_user_verification_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.BigAutoField(
                auto_created=True,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
        ),
    ]
