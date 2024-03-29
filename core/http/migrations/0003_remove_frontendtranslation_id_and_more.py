# Generated by Django 5.0.2 on 2024-03-09 12:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('http', '0002_comment_alter_post_options_remove_post_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='frontendtranslation',
            name='id',
        ),
        migrations.AddField(
            model_name='frontendtranslation',
            name='basecomment_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='http.basecomment'),
            preserve_default=False,
        ),
    ]