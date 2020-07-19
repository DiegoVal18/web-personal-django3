from django.db import models

# Create your models here.
class Proyect(models.Model):
    tittle = models.CharField(max_length=200, verbose_name="Titulo")
    
    description = models.TextField(verbose_name="Descripción")

    image= models.ImageField(verbose_name="Imagen", upload_to="projects")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")

    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")

    url = models.URLField(max_length=200, null=True, blank=True, verbose_name="Direccion Web" )


    class Meta:
        verbose_name= 'proyecto'
        verbose_name_plural= 'proyectos'
        ordering = ["-created"]
    def __str__(self):
        return self.tittle