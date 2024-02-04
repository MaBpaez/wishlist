from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=90)
    slug = models.SlugField(max_length=250, unique_for_date="publish")
    brand = models.CharField(max_length=90)
    price = models.CharField(max_length=30)

    # neceario blan=True y null=True
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    publish = models.DateTimeField("fecha de publicación", default=timezone.now)
    created = models.DateTimeField("fecha de creación", auto_now_add=True)
    updated = models.DateTimeField("fecha de modificación", auto_now=True)

    class Meta:
        ordering = ["-publish"]

    def get_absolute_url(self):
        return reverse(
            "inventory:product_detail",
            args=[self.publish.year, self.publish.month, self.publish.day, self.slug],
        )

    def __str__(self):
        return self.name


'''
Si un pedido puede contener varios productos, entonces necesitarías una relación de
muchos a muchos entre Pedido y Producto. Esto se puede lograr en Django utilizando el
campo ManyToManyField. Aquí te muestro cómo se vería:
'''

# class Cliente(models.Model):
#     nombre = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)

# class Producto(models.Model):
#     nombre = models.CharField(max_length=100)
#     precio = models.DecimalField(max_digits=10, decimal_places=2)

# class Pedido(models.Model):
#     cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
#     productos = models.ManyToManyField(Producto, through='DetallePedido')
#     fecha = models.DateField()

# class DetallePedido(models.Model):
#     pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
#     producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
#     cantidad = models.IntegerField()

'''
En este modelo, DetallePedido es una tabla de unión que permite la relación de muchos a
muchos entre Pedido y Producto. Cada fila en DetallePedido representa una transacción
única donde un pedido incluye un producto específico con una cantidad específica.

El argumento through en el campo ManyToManyField se utiliza para especificar una tabla
intermedia personalizada. En este caso, DetallePedido es la tabla intermedia que estamos
utilizando para manejar la relación de muchos a muchos entre Pedido y Producto.

La tabla DetallePedido nos permite almacenar información adicional sobre la relación
entre Pedido y Producto, que en este caso es la cantidad de cada producto en el pedido.

Sin una tabla intermedia personalizada, Django automáticamente genera una para manejar
la relación de muchos a muchos, pero no tendríamos un lugar para almacenar la cantidad
de cada producto en el pedido.
'''
