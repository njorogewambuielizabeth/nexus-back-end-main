# Generated by Django 3.2.12 on 2023-09-17 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meter_reading', '0004_auto_20230917_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='meter',
            name='meter_number',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
