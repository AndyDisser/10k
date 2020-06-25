# Generated by Django 3.0.5 on 2020-06-06 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datacollection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timestamp',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='timestamp',
            name='subject',
            field=models.CharField(choices=[('AnNuMa', 'Analysis und Numerik'), ('Algo1', 'Algorithmen und Datenstrukturen 1'), ('PDB', 'Programmieren von Datenbanken'), ('PPDC', 'Programmierparadigmen und Compilerbau'), ('RTKS', 'Rechnertechnologie und kombinatorische Schaltungen'), ('Kaggle', 'Kaggle'), ('edx', 'edx')], max_length=128),
        ),
    ]