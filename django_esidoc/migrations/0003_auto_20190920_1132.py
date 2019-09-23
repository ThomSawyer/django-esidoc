# Generated by Django 2.2.4 on 2019-09-20 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("django_esidoc", "0002_institution_ends_at")]

    operations = [
        migrations.AddField(
            model_name="institution",
            name="ent",
            field=models.CharField(
                choices=[("ESIDOC", "Esidoc"), ("HDF", "Hauts-de-France")],
                default="ESIDOC",
                max_length=6,
                verbose_name="Environnements Numériques de Travail",
            ),
        ),
        migrations.AlterField(
            model_name="institution",
            name="uai",
            field=models.CharField(
                max_length=8,
                unique=True,
                verbose_name="Unité Administrative Immatriculée",
            ),
        ),
    ]