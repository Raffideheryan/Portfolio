# Generated by Django 5.0.1 on 2024-01-25 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Work name')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Work Image')),
            ],
        ),
    ]
