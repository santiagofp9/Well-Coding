from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from modeltranslation.manager import MultilingualManager
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
	link = models.URLField(max_length=500,null=True)
	logo = models.ImageField()
	foto = models.ImageField(null=True)
	testimonio = models.CharField(max_length=400,blank=True,null=True)
	autor = models.CharField(max_length=400,null=True)
	fecha = models.DateField(null=True)
	
	class Meta:
		verbose_name = 'Aliado'
		verbose_name_plural = 'Aliados'

	def __str__(self):
		return str(self.nombre)


class Programa(models.Model):
	nombrePrograma = models.CharField(max_length=40,null=True)
	descripcion = models.CharField(max_length=300,null=True)
	order = models.IntegerField()
	inicio = models.DateField()
	lugar = models.CharField(max_length=100,null=True)
	horas = models.IntegerField()
	contenido = models.CharField(max_length=400,null=True)
	requisitos = models.CharField(max_length=300,null=True)
	patrocinador = models.CharField(max_length=300,null=True)
	imagen = models.ImageField(upload_to ='programa/', null = True)

	class Meta:
		verbose_name = 'Programa'
		verbose_name_plural = 'Programas'
		ordering = ['order']

	def __str__(self):
		return str(self.nombrePrograma)
		

class Promocion(models.Model):
    nombrePromo = models.CharField(max_length=40)
    duracion = models.IntegerField()
    inicio = models.DateField()
    fin = models.DateField()
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE,null=True)
    imagen = models.ImageField(upload_to ='edicion/', null = True)

    class Meta:
        verbose_name = 'Promocion'
        verbose_name_plural = 'Promociones'

    def __str__(self):
        return str(self.nombrePromo)


class Alumni(models.Model):
	nombre = models.CharField(max_length=25,blank=True,null=True)
	apellido = models.CharField(max_length=25,blank=True,null=True)
	foto = models.ImageField(null=True)
	acerca_de = models.CharField(max_length=550,blank=True,null=True)
	promocion = models.ForeignKey(Promocion, on_delete=models.CASCADE, null=True)
	cv = models.FileField( null = True)
	
	class Meta:
		verbose_name = 'Alumni'
		verbose_name_plural = 'Alumnis'

	def __str__(self):
		return str(self.nombre) 
        

class Recurso(models.Model):
	nombreRec = models.CharField(max_length=40)
	archivo = models.FileField(null=True,upload_to='archivos/')
	link = models.URLField(null=True, blank=True)
	programa = models.ForeignKey(Programa, on_delete=models.CASCADE, null=True)
	imagen = models.ImageField(upload_to ='recimg/', null = True)


	class Meta:
		verbose_name = 'Recurso'
		verbose_name_plural = 'Recursos'

	def __str__(self):
		return str(self.nombreRec)



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
	fecha = models.DateField(blank=True, null=True)
	link = models.URLField(max_length=500)
	titulo = models.CharField(max_length=100,blank=True, null=True)
	descripcion = models.CharField(max_length=300,blank=True, null=True)
	imagen = models.ImageField(upload_to = 'prensa/', default = 'pic_folder/None/partner-3.png')
	order = models.IntegerField(blank=True, null=True)
	body = models.TextField(blank=True, null=True)
	slug = models.SlugField(max_length=200,default='', blank=True)
	
	class Meta:
		verbose_name = 'Prensa'
		verbose_name_plural = 'Prensa links'
		ordering = ["-fecha"] 

	def save(self):
		self.slug = slugify(self.titulo)
		super(Prensa, self).save()

	def __str__(self):
		return str(self.order) + " " + str(self.titulo)+ " " + str(self.descripcion) 



