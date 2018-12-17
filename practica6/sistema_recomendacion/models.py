from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
from django.core.exceptions import ValidationError

# Create your models here.
class Pelicula(models.Model):
    Id = models.CharField(max_length=100, unique=True, primary_key=True)
    Titulo = models.CharField(max_length=50)
    FechaEstrenoVideo=models.CharField(max_length=50)
    IMDbURL=models.CharField(max_length=50)
    Categorias=models.CharField(max_length=50)


class Usuario(models.Model):
    Id = models.CharField(max_length=100, unique=True,primary_key=True)
    peliculas=models.ManyToManyField(Pelicula,through='Puntuacion')
    Sexo=models.CharField(max_length=2)
    Ocupacion=models.CharField(max_length=50)
    CodigoPostal=models.IntegerField()

class Puntuacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    puntuacion = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    fecha = models.DateTimeField(default=datetime.now(), blank=True)




