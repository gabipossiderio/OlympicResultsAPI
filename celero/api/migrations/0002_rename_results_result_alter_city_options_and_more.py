# Generated by Django 4.0.5 on 2022-06-04 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Results',
            new_name='Result',
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name_plural': 'Cities'},
        ),
        migrations.AlterField(
            model_name='athlete',
            name='height',
            field=models.PositiveSmallIntegerField(help_text='Measurement Unit - centimeters'),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='weight',
            field=models.PositiveSmallIntegerField(help_text='Measurement Unit - kilograms'),
        ),
    ]
