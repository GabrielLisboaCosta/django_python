from django.db import models
from exemplo.models.base import BaseModel


class Reporter(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return f'{self.name}: {self.email}'
