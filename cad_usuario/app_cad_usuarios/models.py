from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(
        db_column='id',
        primary_key=True)
    
    nome = models.TextField(
        db_column='nome',
        max_length=70,
        null=False
    )

    idade = models.IntegerField(
        db_column='idade',
        null=False
    )