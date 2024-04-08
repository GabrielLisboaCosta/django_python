from exemplo.models.base import *
from django.core.validators import MinValueValidator


class Example(BaseModel):
    nome = models.CharField(max_length=200,
                            help_text="Nome do clube")
    torcedores = models.IntegerField(default=0,
                                      help_text="Quantidade de torcedores",
                                      validators=[MinValueValidator(0)])

    class Meta:
        abstract = False

    def __str__(self):
        return f"{self.nome}: {self.torcedores}"

#git config --global user.email "you@example.com"
#git config --global user.name "Your Name"
# git remote add <name> <url>
#git push <name>
