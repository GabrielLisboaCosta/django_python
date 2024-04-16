from django.db import models
from exemplo.models.base import BaseModel


class Magazine(BaseModel):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title
