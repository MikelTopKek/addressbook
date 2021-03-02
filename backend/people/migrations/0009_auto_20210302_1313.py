# Generated by Django 3.1.7 on 2021-03-02 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0008_auto_20210302_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(default=None, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(default=None, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(default=None, max_length=64, null=True),
        ),
    ]