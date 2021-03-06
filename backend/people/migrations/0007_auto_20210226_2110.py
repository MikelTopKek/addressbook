# Generated by Django 3.1.7 on 2021-02-26 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0006_auto_20210226_2059'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=8)),
                ('city', models.CharField(max_length=16)),
                ('street', models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name='people',
            name='name',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='people',
            name='surname',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='people',
            name='telephone',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='people',
            name='url',
            field=models.CharField(default=None, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='address',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='people.address'),
        ),
    ]
