# Generated by Django 5.0.3 on 2024-04-23 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchedulingApp', '0004_lab_lab_name_section_section_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='lab',
            name='start_time',
            field=models.TimeField(),
        ),
    ]
