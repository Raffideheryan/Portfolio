# Generated by Django 5.0.1 on 2024-01-25 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_topic', models.CharField(max_length=60, verbose_name='Service main topic')),
                ('service_topic', models.CharField(max_length=60, verbose_name='Service topic')),
                ('text', models.TextField(verbose_name='Service text')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Service image')),
            ],
        ),
    ]
