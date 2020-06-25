from django.db import models

SUBJECT_CHOICES = [
    ('AnNuMa', 'Analysis und Numerik'),
    ('Algo1', 'Algorithmen und Datenstrukturen 1'),
    ('PDB', 'Programmieren von Datenbanken'),
    ('PPDC', 'Programmierparadigmen und Compilerbau'),
    ('RTKS', 'Rechnertechnologie und kombinatorische Schaltungen'),
    ('Kaggle', 'Kaggle'),
    ('edx', 'edx'),
    ('WebProgramming', 'WebProgramming')
]

class Timestamp(models.Model):
    subject = models.CharField(max_length=128, choices=SUBJECT_CHOICES)
    date = models.DateField(auto_now_add=False)
    time_spend = models.DurationField()
