# Generated by Django 4.0.6 on 2022-08-04 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0014_delete_tasks_remove_reports_task_date_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="reports",
            name="date_fin",
        ),
        migrations.RemoveField(
            model_name="reports",
            name="date_start",
        ),
        migrations.RemoveField(
            model_name="reports",
            name="lag",
        ),
    ]
