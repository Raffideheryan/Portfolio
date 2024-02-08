# Generated by Django 5.0.1 on 2024-01-25 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100, verbose_name='About Topic')),
                ('text1', models.TextField(verbose_name='About Text 1')),
                ('text2', models.TextField(verbose_name='About Text 2')),
                ('image', models.ImageField(upload_to='images/', verbose_name='About image')),
                ('button_text', models.CharField(max_length=50, verbose_name='About button text')),
            ],
        ),
    ]