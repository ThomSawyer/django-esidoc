# Generated by Django 2.2.4 on 2019-10-02 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("django_esidoc", "0003_auto_20190920_1132")]

    operations = [
        migrations.AlterField(
            model_name="institution",
            name="ent",
            field=models.CharField(
                choices=[
                    ("ESIDOC", "Esidoc"),
                    ("HDF", "Hauts-de-France"),
                    ("GAR", "GAR"),
                ],
                default="ESIDOC",
                max_length=6,
                verbose_name="Environnements Numériques de Travail",
            ),
        )
    ]
