# Generated by Django 4.2.7 on 2023-11-30 04:38

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "edc_form_runners",
            "0004_remove_issue_unique_label_lower_subject_identifier_etc_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="issue",
            name="status",
        ),
    ]