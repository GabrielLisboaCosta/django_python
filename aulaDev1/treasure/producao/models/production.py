from producao.models.base import *
from django.core.validators import MinLengthValidator
from django.db import models


class Production(BaseModel):
    nome = models.CharField(max_length=200)

    class Meta:
        abstract = False

    title = models.CharField(max_length=100, validators=[MinLengthValidator(1)])

    advisory_certificate = models.CharField(max_length=10, validators=[MinLengthValidator(1)])

    lengh = models.DurationField()

    #genre =

    tredimenter = models.IntegerField()

    reviews = models.FloatField()

    specs = models.CharField(max_length=50, validators=[MinLengthValidator(5)])

    sinopse = models.CharField(max_length=500, validators=[MinLengthValidator(10)])

    realease_date = models.DateField()

    def __str__(self):
        return self.title
