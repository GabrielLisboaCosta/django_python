from producao.models.base import BaseModel
from django.core.validators import MinLengthValidator
from django.db import models
from enums import genero


class Production(BaseModel):
    nome = models.CharField(max_length=200)

    class Meta:
        abstract = False

    titulo = models.CharField(max_length=100, validators=[MinLengthValidator(1)])

    sinopse = models.CharField(max_length=500, validators=[MinLengthValidator(10)])

    genero = genero.DEFAULT

    classificacao = models.CharField(max_length=10, validators=[MinLengthValidator(1)])

    quantidade_avaliacoes = models.IntegerField(validators=[MinLengthValidator(1)])

    nota = models.IntegerField(max_length=10, validators=[MinLengthValidator(1)])

    duracao = models.DurationField()

    populadidade = models.IntegerField(max_length=100, validators=[MinLengthValidator(0)])

    especificacoes = models.CharField(max_length=50, validators=[MinLengthValidator(5)])

    lancamento = models.DateField()

    def __str__(self):
        return self.title

    def alterar_genero(self, gen: genero):
        if isinstance(gen, genero):
            self.genero = gen
            return True
        else:
            return False

    def avaliar(self, nova_nota):
        self.nota = float(nova_nota)
        return print(f'Nota: {self.nota}')

    def alterar_popularidade(self, alteracao: int):
        self.populadidade = alteracao
        return print(f'Popularidade: {self.populadidade}')
    