# Generated by Django 4.0.6 on 2022-08-07 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_rename_reports_calculation'),
    ]

    operations = [
        migrations.AddField(
            model_name='calculation',
            name='cid',
            field=models.CharField(max_length=10000, null=True, verbose_name='Calculation task ID'),
        ),
    ]
