# Generated by Django 4.2.5 on 2023-09-14 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit_sharing', '0002_alter_unitsharing_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitsharing',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='unitsharing',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
