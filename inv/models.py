from django.db import models
from bases.models import ClaseModelo

# Create your models here.


class Category(ClaseModelo):
    description = models.CharField(
        max_length=100,
        help_text='Descripcion de la Categoria',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.description)

    def save(self):
        self.description = self.description.upper()
        super(Category, self).save()

    class Meta:
        verbose_name_plural = "Categories"
