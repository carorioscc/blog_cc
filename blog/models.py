# Create your models here.
# FROM O IMPORT se usa para agregar otros archivos, se pueden incluir algunas cosas de los archivos

from django.conf import settings
from django.db import models
from django.utils import timezone

#Define el modelo es un objeto
#class define un objeto
#Post en este caso es el nombre de nuestro modelo.
#models.Model es significa que es un modelo de django
class Post(models.Model):
	#declaraciones de las propiedades.
	# models.CharField, así es como defines un texto con un número limitado de caracteres.
	# models.TextField, este es para texto largo sin límite. Suena perfecto para el contenido de la entrada del blog, ¿no?
	# models.DateTimeField, este es fecha y hora.pur
	# modelos.ForeignKey, este es una relación (link) con otro modelo.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    #def significa funcion publish nombre de metodo o funcion 
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title