# Generated by Django 4.2.6 on 2023-12-13 07:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Data_Analyst", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="villageboundarymodel",
            old_name="distric",
            new_name="district",
        ),
    ]
