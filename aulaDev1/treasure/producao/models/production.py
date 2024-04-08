from producao.models.base import *
from django.core.validators import MinLengthValidator


class Production(BaseModel):
    nome = models.CharField(max_length=200)

    class Meta:
        abstract = False

    # title = models.CharField(max_length=100, validators=[MinLengthValidador(1)])
    #
    # advisory_certificate = models.CharField(max_length=10, validators=[MinLengthValidador(1)])
    #
    # lengh = models.DurationField()
    #
    # #genre =
    #
    # tredimenter = models.IntergerField()
    #
    # reviews = models.FloatField()
    #
    # specs = models.CharField(max_length=50, validators=[MinLengthValidador(5)])
    #
    # sinopse = models.CharField(max_length=500, validators=[MinLengthValidador(10)])
    #
    # realease_date = models.DateFiled()

    def __str__(self):
        return self.title
