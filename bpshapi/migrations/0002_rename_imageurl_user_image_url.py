# Generated by Django 4.1.3 on 2023-08-17 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bpshapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='imageUrl',
            new_name='image_url',
        ),
    ]
