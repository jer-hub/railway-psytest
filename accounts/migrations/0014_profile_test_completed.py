# Generated by Django 3.2.7 on 2022-02-09 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_profile_is_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='test_completed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
