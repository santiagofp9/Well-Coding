from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre
      
class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    descripcion = models.TextField(max_length=300)
    precio = models.DecimalField(decimal_places=2, max_digits=6)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to = 'static/iemeges/')

    def __str__(self):
        return self.nombre

class Carrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete= models.CASCADE, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(decimal_places=2, max_digits=6)