# Generated by Django 3.1.2 on 2020-10-10 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20201010_0311'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='comment',
            field=models.TextField(blank=True),
        ),
    ]
