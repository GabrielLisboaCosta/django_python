from django.db import models
from producao.models.base import BaseModel


class Person(BaseModel):
    name = models.CharField(max_length=100, verbose_name='Full name')
    birth_date = models.DateField(verbose_name='Birth Date')
    cpf = models.CharField(max_length=100, verbose_name='CPF Number')

    def __str__(self):
        return f'{self.name}'
