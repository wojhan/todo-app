# Generated by Django 4.1.10 on 2023-08-30 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="case",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tasks",
                to="api.case",
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="done_at",
            field=models.DateTimeField(null=True),
        ),
    ]