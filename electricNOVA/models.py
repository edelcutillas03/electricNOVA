from django.db import models
from django.utils import timezone

class TipoCargador(models.Model):
    descripcion = models.CharField(max_length=25)


    def __str__(self):
        return self.descripcion


        
class Estado(models.Model):
    descripcion = models.CharField(max_length=25)
    

    def __str__(self):
        return self.descripcion


class Electrocasero(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    cp = models.CharField(max_length=5)
    direccion = models.CharField(max_length=100)
    poblacion = models.CharField(max_length=100)
    provincia = models.CharField(max_length=50)
    preciodecarga = models.DecimalField(max_digits=5, decimal_places=2)
    horasdisponibles = models.TextField()
    tiposCargador = models.ManyToManyField(TipoCargador)

    def __str__(self):
        return self.nombre



class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    direccion = models.CharField(max_length=100)
    poblacion = models.CharField(max_length=100)
    provincia = models.CharField(max_length=50)
    reservas = models.ManyToManyField(
        Electrocasero,
        through='Reserva')


    def __str__(self):
        return self.nombre



class Reserva(models.Model):
    cliente = models.ForeignKey(
                        'Cliente'
                        ,on_delete=models.CASCADE,)
    electrocasero = models.ForeignKey(
                        'Electrocasero'
                        ,on_delete=models.CASCADE,)
    estado = models.ForeignKey(
                        'Estado'
                        ,on_delete=models.CASCADE,)
    fecha = models.DateField()
    

    def __str__(self):
        return str(self.fecha) + " - " + self.cliente.nombre + " - " + self.electrocasero.nombre + " - " + self.estado.descripcion





















