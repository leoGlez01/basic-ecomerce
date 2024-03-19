from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=100, null=True, blank=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    cantidad = models.IntegerField(null= False, blank = False)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        db_table = "producto"

    def __str__(self) -> str:
        return self.nombre
