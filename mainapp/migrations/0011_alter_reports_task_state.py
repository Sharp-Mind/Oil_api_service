# Generated by Django 4.0.6 on 2022-08-02 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0010_reports_task_state_alter_reports_date_fin_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reports",
            name="task_state",
            field=models.CharField(max_length=36, null=True, verbose_name="Task state"),
        ),
    ]
