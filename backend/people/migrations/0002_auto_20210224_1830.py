# Generated by Django 3.1.7 on 2021-02-24 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='people',
            old_name='adress',
            new_name='address',
        ),
    ]
