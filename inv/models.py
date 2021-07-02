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


class SubCategory(ClaseModelo):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(
        max_length=100,
        help_text='Descripcion de la Categoria'
    )

    def __str__(self):
        return '{}:{}'.format(self.category.description, self.description)

    def save(self):
        self.description = self.description.upper()
        super(SubCategory, self).save()

    class Meta:
        verbose_name_plural = "Sub Categorias"
        unique_together = ('category', 'description')


class Marca(ClaseModelo):
    description = models.CharField(
        max_length=100,
        help_text='Descripcion de la Marca'
    )

    def __str__(self):
        return '{}'.format(self.description)

    def save(self):
        self.description = self.description.upper()
        super(Marca, self).save()

    class Meta:
        verbose_name_plural = "Marcas"


class UnidadMedida(ClaseModelo):
    description = models.CharField(
        max_length=100,
        help_text='Unidad de Medida'
    )

    def __str__(self):
        return '{}'.format(self.description)

    def save(self):
        self.description = self.description.upper()
        super(UnidadMedida, self).save()

    class Meta:
        verbose_name_plural = "Unidades de Medidad"


class Producto(ClaseModelo):
    codigo = models.CharField(
        max_length=20,
        unique=True
    )
    codigo_barras = models.CharField(
        max_length=50)
    descripcion = models.CharField(
        max_length=200,
    )
    precio = models.FloatField(default=0)
    existencia = models.IntegerField(default=0)
    ultima_compra = models.DateField(null=True, blank=True)

    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Producto, self).save()

    class Meta:
        verbose_name_plural = "Productos"
        unique_together = ('codigo', 'codigo_barras')
