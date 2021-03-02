# Generated by Django 3.1.7 on 2021-02-26 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_people_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='image',
            field=models.FileField(default=None, upload_to=''),
        ),
        migrations.AlterField(
            model_name='people',
            name='url',
            field=models.CharField(default=None, max_length=255),
        ),
    ]