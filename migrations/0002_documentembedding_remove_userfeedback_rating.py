# Generated by Django 5.1.2 on 2024-11-05 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chatbot", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="DocumentEmbedding",
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
                ("content", models.TextField()),
                ("embedding", models.BinaryField()),
                ("source_url", models.URLField(blank=True, null=True)),
                ("metadata", models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="userfeedback",
            name="rating",
        ),
    ]
