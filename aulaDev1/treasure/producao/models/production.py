from producao.models.base import BaseModel
from django.core.validators import MinLengthValidator
from django.db import models


class Production(BaseModel):
    nome = models.CharField(max_length=200)

    class Meta:
        abstract = False

    titulo = models.CharField(max_length=100, validators=[MinLengthValidator(1)])

    classificacao = models.CharField(max_length=10, validators=[MinLengthValidator(1)])

    duracao = models.DurationField()

    #genero = enums.genero

    tredimenter = models.IntegerField()

    reviews = models.FloatField()

    specs = models.CharField(max_length=50, validators=[MinLengthValidator(5)])

    sinopse = models.CharField(max_length=500, validators=[MinLengthValidator(10)])

    realease_date = models.DateField()

    def __str__(self):
        return self.title
