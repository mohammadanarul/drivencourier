# Generated by Django 4.0.3 on 2022-03-17 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('percels', '0002_percel_pickup_location_alter_percel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='percel',
            name='traking_id',
            field=models.CharField(max_length=12, verbose_name='traking id'),
        ),
    ]
