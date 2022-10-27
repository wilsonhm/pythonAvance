from django.db import models

# Create your models here.
class Asesor(models.Model):
    nombres=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=50)
    dni=models.CharField(max_length=8)
    especialidad=models.CharField(max_length=8)
    celular=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = ("Asesor")
        verbose_name_plural = ("Asesores")

    def __str__(self):
        return self.nombres

 