# Generated by Django 3.2.8 on 2021-11-01 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='copyrights',
            name='is_valid',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
