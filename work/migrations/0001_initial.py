# Generated by Django 4.1 on 2023-01-06 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkModel',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('create_user', models.CharField(max_length=100)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('update_user', models.CharField(max_length=100)),
                ('is_deleted', models.IntegerField(default=0)),
                ('work_id', models.AutoField(primary_key=True, serialize=False)),
                ('work_date', models.DateField()),
                ('work_weekday', models.IntegerField(default=0)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('work_hour', models.FloatField()),
                ('comments', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
