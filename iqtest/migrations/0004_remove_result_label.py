# Generated by Django 3.2.7 on 2022-12-31 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iqtest', '0003_result'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='label',
        ),
    ]
