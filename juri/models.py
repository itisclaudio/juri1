from typing import TextIO
from django.db import models

class Area(models.Model):
    """ Areas del derecho """
    nombre	= models.CharField(max_length=50)
    activo	= models.BooleanField(default=True)

    class Meta:
        ordering = ['nombre']
        verbose_name_plural = 'Areas del Derecho'

    def __str__(self):
        return self.nombre


class Juez(models.Model):
    """ Lista de Jueces """
    apellidos   = models.CharField(max_length=50)
    nombres	    = models.CharField(max_length=50)
    activo	    = models.BooleanField(default=True)

    class Meta:
        ordering = ['apellidos', 'nombres']
        verbose_name_plural = 'Jueces'

    def __str__(self):
        return f'{self.apellidos}, {self.nombres}'


class Sala(models.Model):
    """ Salas de la Corte Suprema """
    nombre	= models.CharField(max_length=80)

    class Meta:
        ordering = ['nombre']
        verbose_name_plural = 'Salas de la Corte Suprema'

    def __str__(self):
        return self.nombre


class Casacion(models.Model):
    """ Lista de Jueces """
    DEMANDANTE  = 1
    DEMANDADO   = 2
    AMBOS       = 3
    PARTE_TIPO = (
        (DEMANDANTE, 'Demandante'),
        (DEMANDADO, 'Demandado'),
        (AMBOS, 'Ambos'),
    )

    IMPROCEDENTE        = 1
    INFUNDADO           = 2
    FUNDADO_EN_PARTE    = 3
    FUNDADO             = 4
    FALLO_TIPO = (
        (IMPROCEDENTE, 'Improcedente'),
        (INFUNDADO, 'Infundado'),
        (FUNDADO_EN_PARTE, 'Fundado en Parte'),
        (FUNDADO, 'Fundado'),
    )

    numero          = models.CharField(max_length=40, unique=True)
    materia	        = models.CharField(max_length=100)
    sumilla	        = models.TextField(blank=True, null=True)
    extracto        = models.TextField(blank=True, null=True)
    sala            = models.ForeignKey(Sala, on_delete=models.CASCADE)
    demandante      = models.CharField(max_length=130)
    demandado       = models.CharField(max_length=250)
    parte           = models.IntegerField(choices=PARTE_TIPO, default=1, blank=True, null=True)
    casante         = models.CharField(max_length=250)
    es_precedente   = models.BooleanField(default=False)
    fallo           = models.IntegerField(choices=FALLO_TIPO, default=1)
    juezponente_nombre = models.CharField(max_length=100)
    jueces_nombres  = models.CharField(max_length=150)
    juezdiscordia_nombre = models.CharField(max_length=50)
    area            = models.ManyToManyField(Area, blank=True)
    boletin        = models.CharField(max_length=60, blank=True, null=True)
    pagina          = models.CharField(max_length=17, blank=True, null=True)
    fecha_inicio    = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    fecha_sentencia = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    texto           = models.TextField(blank=True, null=True)
    activo	        = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Casaciones'

    def __str__(self):
        return f'{self.numero}, {self.materia}'