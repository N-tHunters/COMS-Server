# Generated by Django 3.1.2 on 2021-03-02 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('COMSAPI', '0008_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
