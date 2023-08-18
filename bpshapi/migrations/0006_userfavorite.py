# Generated by Django 4.1.3 on 2023-08-18 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bpshapi', '0005_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFavorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bpshapi.shop')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bpshapi.user')),
            ],
        ),
    ]
