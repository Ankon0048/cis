# Generated by Django 4.2.7 on 2023-12-03 06:41

from django.db import migrations, models
import myapp.models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0060_case_fir_additional_info"),
    ]

    operations = [
        migrations.AlterField(
            model_name="emergency",
            name="timestamp",
            field=models.TimeField(default=myapp.models.get_current_time),
        ),
    ]