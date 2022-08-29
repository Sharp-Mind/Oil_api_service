# Generated by Django 4.0.6 on 2022-08-02 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0009_reports_date_fin_reports_date_start_reports_lag_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="reports",
            name="task_state",
            field=models.CharField(default=None, max_length=36, verbose_name="Task state"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="reports",
            name="date_fin",
            field=models.DateField(verbose_name="nput date of finish"),
        ),
        migrations.AlterField(
            model_name="reports",
            name="date_start",
            field=models.DateField(verbose_name="Input date of start"),
        ),
        migrations.AlterField(
            model_name="reports",
            name="lag",
            field=models.IntegerField(verbose_name="Lag"),
        ),
    ]
