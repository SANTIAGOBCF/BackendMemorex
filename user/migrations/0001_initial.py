# Generated by Django 4.1.4 on 2022-12-24 12:57

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(blank=True, null=True, verbose_name="last login"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        error_messages={
                            "unique": "A user with that email address already exists."
                        },
                        max_length=254,
                        unique=True,
                        verbose_name="email address",
                    ),
                ),
                ("first_name", models.CharField(max_length=80)),
                ("last_name", models.CharField(max_length=80)),
                ("profile_image", models.CharField(max_length=250, null=True)),
                ("role", models.CharField(max_length=80)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
