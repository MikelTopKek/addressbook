# Generated by Django 3.1.7 on 2021-02-26 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_auto_20210224_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='url',
            field=models.CharField(default='', max_length=255),
        ),
    ]