# Generated by Django 5.0.1 on 2024-01-27 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_rename_imagee_team_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='name',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Work name'),
        ),
    ]
