# Generated by Django 4.0.6 on 2022-08-02 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0006_alter_reports_task_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reports",
            name="task_date",
            field=models.DateField(auto_now_add=True, verbose_name="Date of row creation"),
        ),
    ]
