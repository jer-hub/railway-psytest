# Generated by Django 3.2.7 on 2022-10-06 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0039_auto_20220524_2120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_result',
        ),
    ]
