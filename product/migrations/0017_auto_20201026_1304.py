# Generated by Django 3.1.2 on 2020-10-26 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_auto_20201013_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='stock',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]
