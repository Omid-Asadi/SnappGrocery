# Generated by Django 4.2 on 2024-04-06 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_time", models.DateTimeField(auto_now_add=True)),
                ("modified_time", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=256)),
                ("body", models.TextField(max_length=512)),
            ],
            options={"abstract": False,},
        ),
    ]
