# Generated by Django 5.0.1 on 2024-02-09 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_portfolio_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Service text'),
        ),
    ]