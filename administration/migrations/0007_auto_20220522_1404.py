# Generated by Django 3.2.7 on 2022-05-22 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0006_remove_adminscheduledconsultation_approved_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adminscheduledconsultation',
            old_name='user',
            new_name='client',
        ),
        migrations.RemoveField(
            model_name='adminscheduledconsultation',
            name='is_done',
        ),
    ]