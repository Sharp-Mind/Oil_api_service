# Generated by Django 4.0.6 on 2022-08-02 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0003_tasks_alter_reports_options"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Tasks",
        ),
        migrations.AddField(
            model_name="reports",
            name="task_date",
            field=models.DateField(auto_now_add=True, null=True, verbose_name="Date of raw creation"),
        ),
        migrations.AlterField(
            model_name="reports",
            name="date",
            field=models.CharField(max_length=10000, verbose_name="Date"),
        ),
        migrations.AlterField(
            model_name="reports",
            name="liquid",
            field=models.CharField(max_length=10000, verbose_name="Liquid"),
        ),
        migrations.AlterField(
            model_name="reports",
            name="oil",
            field=models.CharField(max_length=10000, verbose_name="Oil"),
        ),
        migrations.AlterField(
            model_name="reports",
            name="water",
            field=models.CharField(max_length=10000, verbose_name="Water"),
        ),
        migrations.AlterField(
            model_name="reports",
            name="wct",
            field=models.CharField(max_length=10000, verbose_name="wct"),
        ),
    ]
