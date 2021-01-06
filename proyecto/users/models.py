from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Categoria(models.Model):
	cat_nom = models.CharField(max_length=200, help_text="Ingrese el nombre de la categoria", null='True')

	def __str__(self):
		return self.cat_nom

class Imagen(models.Model):
  imagen = models.ImageField(null='True', upload_to='perfil')
  user = models.ForeignKey(User, on_delete='models.CASCADE', blank='True')
  titulo = models.CharField(max_length=100, help_text="Ingrese el nombre de la imagen", null='True')
  descripcion = models.CharField(max_length=1000, help_text="Ingrese su descripcion", null='True')
  fecha_subida = models.DateTimeField(auto_now_add='True', null='True')

  


  