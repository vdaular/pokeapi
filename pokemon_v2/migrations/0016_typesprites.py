# Generated by Django 3.2.23 on 2024-07-29 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("pokemon_v2", "0015_pokemoncries"),
    ]

    operations = [
        migrations.CreateModel(
            name="TypeSprites",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sprites", models.JSONField()),
                (
                    "type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="typesprites",
                        to="pokemon_v2.type",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
