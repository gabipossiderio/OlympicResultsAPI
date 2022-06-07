# Generated by Django 4.0.5 on 2022-06-06 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_athlete_age_alter_athlete_height_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='athlete',
            name='age',
        ),
        migrations.AddField(
            model_name='athlete',
            name='date_of_birth',
            field=models.CharField(default='NA', max_length=4),
        ),
    ]