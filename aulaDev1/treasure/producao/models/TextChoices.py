from django.utils.translation import gettext_lazy as _
from django.db import models


class genero(models.TextChoices):
    ACTION = "ACT", _("Ação")
    ADVENTURE = "ADV", _("Aventura")
    HORROR = "HOR", _("Horor")
    SCI_FI = "FIC", _("Ficção")
    THRILLER = "THR", _("Suspense")
    WAR = "WAR", _("Guerra")
