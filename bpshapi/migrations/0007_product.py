# Generated by Django 4.1.3 on 2023-08-18 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bpshapi', '0006_userfavorite'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('image_url', models.CharField(max_length=255)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shops', to='bpshapi.shop')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='bpshapi.user')),
            ],
        ),
    ]
