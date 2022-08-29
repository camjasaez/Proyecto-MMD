from django.db import models

# Create your models here.


class Universidad(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)


class Bodeguero(models.Model):
    nombre = models.CharField(max_length=50)


class Elemento(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)


class Ciudad(models.Model):
    nombre = models.CharField(max_length=50, unique=True)


class Region(models.Model):
    nombre = models.CharField(max_length=50)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)


class Delegacion(models.Model):
    nombre = models.CharField(max_length=50)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    universidad = models.ForeignKey(Universidad, on_delete=models.CASCADE)


class Deportista(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_nacimiento = models.CharField(max_length=255)
    delegacion = models.ForeignKey(Delegacion, on_delete=models.CASCADE)
    universidad = models.ForeignKey(Universidad, on_delete=models.CASCADE)


class Bodega(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    estado = models.BooleanField()
    bodeguero = models.ForeignKey(Bodeguero, on_delete=models.CASCADE)
    elementos = models.ManyToManyField(
        Elemento, through='Tiene', through_fields=('bodega', 'elemento'))


class Tiene(models.Model):
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)
    elemento = models.ForeignKey(Elemento, on_delete=models.CASCADE)
    delegacion = models.ForeignKey(Delegacion, on_delete=models.CASCADE)
