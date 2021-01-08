from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError

class Categoria(models.Model):
	cat_nom = models.CharField(max_length=200, help_text="Ingrese el nombre de la categoria", null='True')

	def __str__(self):
		return self.cat_nom

class Imagen(models.Model):
  imagen = models.ImageField(null='True', upload_to='perfil')
  user = models.ForeignKey(User, on_delete=models.CASCADE, blank='True')
  titulo = models.CharField(max_length=100, help_text="Ingrese el nombre de la imagen", null='True')
  descripcion = models.CharField(max_length=1000, help_text="Ingrese su descripcion", null='True')
  fecha_subida = models.DateTimeField(auto_now_add='True', null='True')

class Favorito(models.Model):
  idImagen= models.ForeignKey(Imagen, on_delete=models.CASCADE, blank='True')
  user = models.ForeignKey(User, on_delete=models.CASCADE, blank='True')
  def clean(self):
        direct = Favorito.objects.filter(idImagen = self.idImagen, user = self.user)
        reverse = Favorito.objects.filter(user = self.user, idImagen = self.idImagen)
        if direct.exists() or reverse.exists():
            return 1
        else:
          return 0

class Tarde(models.Model):
  idImagen= models.ForeignKey(Imagen, on_delete=models.CASCADE, blank='True')
  user = models.ForeignKey(User, on_delete=models.CASCADE, blank='True')
  def clean(self):
        direct = Tarde.objects.filter(idImagen = self.idImagen, user = self.user)
        reverse = Tarde.objects.filter(user = self.user, idImagen = self.idImagen) 

        if direct.exists() or reverse.exists():
            return 1
        else:
          return 0

  


  