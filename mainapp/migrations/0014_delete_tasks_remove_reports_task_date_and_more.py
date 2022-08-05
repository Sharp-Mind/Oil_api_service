# Generated by Django 4.0.6 on 2022-08-04 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("django_celery_results", "0011_taskresult_periodic_task_name"),
        ("mainapp", "0013_alter_reports_date_alter_reports_date_fin_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Tasks",
        ),
        migrations.RemoveField(
            model_name="reports",
            name="task_date",
        ),
        migrations.RemoveField(
            model_name="reports",
            name="task_id",
        ),
        migrations.RemoveField(
            model_name="reports",
            name="task_state",
        ),
        migrations.AddField(
            model_name="reports",
            name="task",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="django_celery_results.taskresult",
            ),
        ),
    ]
