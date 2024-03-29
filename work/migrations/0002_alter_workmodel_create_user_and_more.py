# Generated by Django 4.1 on 2023-01-06 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workmodel',
            name='create_user',
            field=models.CharField(default='leesure', max_length=100),
        ),
        migrations.AlterField(
            model_name='workmodel',
            name='update_user',
            field=models.CharField(default='leesure', max_length=100),
        ),
        migrations.AlterField(
            model_name='workmodel',
            name='work_weekday',
            field=models.CharField(choices=[('Mon', 'Mondy'), ('Tue', 'Tuesday'), ('Wed', 'Wednesday'), ('Thu', 'Thuresday'), ('Fri', 'Friday'), ('Sat', 'Saturday'), ('Sun', 'Sunday')], max_length=50),
        ),
    ]
