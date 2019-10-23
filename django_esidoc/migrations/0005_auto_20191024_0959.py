# Generated by Django 2.2.6 on 2019-10-24 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_esidoc', '0004_auto_20191002_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='ent',
            field=models.CharField(choices=[('ESIDOC', 'Esidoc'), ('HDF', 'Hauts-de-France'), ('GAR', 'GAR'), ('OCCITANIE', 'Occitanie'), ('OCCITANIEAGR', 'Occitanie lycée agricole')], default='ESIDOC', max_length=12, verbose_name='Environnements Numériques de Travail'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='uai',
            field=models.CharField(max_length=14, unique=True, verbose_name='Unité Administrative Immatriculée'),
        ),
    ]
