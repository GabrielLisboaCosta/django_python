from django.db import models
from exemplo.models.person import Person
from producao.models.base import BaseModel


class Passaport(BaseModel):
    number = models.CharField(max_length=100, verbose_name='Passaport Nuber')
    #issue_date = models.DateField(verbose_name='Issue Date')
    expiration_date = models.DateField(verbose_name='Expiration Date')
    owner = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        abstract = False

    def __str__(self):
        return f'{self.number} - {self.owner.name}'
