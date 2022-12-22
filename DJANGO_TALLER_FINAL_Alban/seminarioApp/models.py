from django.db import models
from django.utils import timezone
opciones_estado = [    
    ("Reservado", "Reservado"),    
    ("Completada", "Completada"),    
    ("Anulada", "Anulada"),    
    ("No asisten", "No asisten")]

instituciones = [      
    ("UFRO", "UFRO"),
    ("U Autonoma", "U Autonoma"),     
    ("Santo Tomas", "Santo Tomas"), 
    ("AIEP", "AIEP"),   
    ("U.Catolica", "U.Catolica"),    
    ("Inacap", "Inacap")]

# Create your models here.
class Inscrito(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    fechaInscripcion = models.DateField()
    institucion = models.CharField(max_length=50, choices=instituciones)
    horaInscripcion = models.TimeField()
    estado = models.CharField(max_length=50, choices=opciones_estado)
    observacion = models.CharField(max_length=50)


    def save(self, *args, **kwargs):
        if not self.id:
            self.fechaInscripcion = timezone.now().date()
            self.horaInscripcion = timezone.now().time()
        super(Inscrito, self).save(*args, **kwargs)

class Institucion(models.Model):
    id = models.AutoField(primary_key=True)
    institucion = models.CharField(max_length=50)