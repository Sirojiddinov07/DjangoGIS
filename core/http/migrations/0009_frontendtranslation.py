# Generated by Django 5.0.2 on 2024-02-16 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('http', '0008_remove_pendinguser_code_pendinguser_first_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrontendTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255, unique=True)),
                ('value', models.TextField()),
            ],
            options={
                'verbose_name': 'Frontend Translation',
                'verbose_name_plural': 'Frontend Translations',
            },
        ),
    ]