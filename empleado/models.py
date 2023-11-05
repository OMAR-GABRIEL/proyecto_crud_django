from django.db import models

# Create your models her
class Empleado(models.Model):
    codigo=models.CharField(primary_key=True,max_length=10)
    nombre=models.CharField(max_length=45)


    def __str__(self):
        text="{0}({1})"
        return text.format(self.nombre,self.codigo)
        