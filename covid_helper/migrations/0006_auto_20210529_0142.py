# Generated by Django 3.2.3 on 2021-05-28 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('covid_helper', '0005_contact_timestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='sno',
            new_name='sn0',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='timestamp',
        ),
    ]