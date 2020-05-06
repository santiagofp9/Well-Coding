from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Numero(models.Model):
	nombre = models.CharField(max_length=40)
	dato = models.IntegerField()

	class Meta:
		verbose_name = 'Número'
		verbose_name_plural = 'Números'

	def __str__(self):
		return str(self.nombre) 

class Aliado(models.Model):
	nombre = models.CharField(max_length=40)
	logo = models.ImageField()
	foto = models.ImageField(null=True)
	testimonio = models.CharField(max_length=400,null=True)
	autor = models.CharField(max_length=400,null=True)
	fecha = models.DateField(null=True)

	class Meta:
		verbose_name = 'Aliado'
		verbose_name_plural = 'Aliados'

	def __str__(self):
		return str(self.nombre)

class Programa(models.Model):
	nombre = models.CharField(max_length=40)
	descripcion = models.CharField(max_length=300)

	class Meta:
		verbose_name = 'Programa'
		verbose_name_plural = 'Programas'

	def __str__(self):
		return str(self.nombre)

class Promocion(models.Model):
    nombre = models.CharField(max_length=40)
    duracion = models.IntegerField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE,null=True)

    class Meta:
        verbose_name = 'Promoción'
        verbose_name_plural = 'Promociones'

    def __str__(self):
        return str(self.nombre)

class Alumni(models.Model):
	nombre = models.CharField(max_length=25)
	apellido = models.CharField(max_length=25)
	foto = models.ImageField(null=True)
	acerca_de = models.CharField(max_length=250,null=True)
	promocion = models.ForeignKey(Promocion, on_delete=models.CASCADE, null=True)
	cv = models.FileField( null = True)
	
	class Meta:
		verbose_name = 'Alumni'
		verbose_name_plural = 'Alumnis'

	def __str__(self):
		return str(self.nombre) 


class Contacto(models.Model):
    email = models.EmailField()
    nombre = models.CharField(max_length=40)

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __str__(self):
	    return str(self.nombre)
        

class Recurso(models.Model):
	nombre = models.CharField(max_length=40)
	archivo = models.FileField(null=True)
	link = models.URLField(max_length=500,null=True)
	programa = models.ForeignKey(Promocion, on_delete=models.CASCADE, null=True)

	class Meta:
		verbose_name = 'Recurso'
		verbose_name_plural = 'Recursos'

	def __str__(self):
		return str(self.nombre)


class Publicacion(models.Model):
	url = models.URLField(max_length=250)
	titulo = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=300)
	texto = models.TextField()
	foto = models.ImageField(null=True)
	fecha = models.DateField()
	autor = models.CharField(max_length=50)
	testimonio = models.BooleanField(default=False)
	home = models.BooleanField(default=False)
	
	class Meta:
		verbose_name = 'Publicación'
		verbose_name_plural = 'Publicaciones'

	def __str__(self):

		return str(self.titulo) + " " + str(self.fecha) 

class Prensa(models.Model):
	fecha = models.DateField()
	link = models.URLField(max_length=500)
	#medio = models.CharField(max_length=50)
	titulo = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=300)
	imagen = models.ImageField(upload_to = 'static/iemeges/', default = 'pic_folder/None/partner-3.png')
    
	class Meta:
		verbose_name = 'Prensa'
		verbose_name_plural = 'Prensa links'
		ordering = ["-fecha"] 

	def __str__(self):

		return str(self.titulo) + " " + str(self.descripcion) 


