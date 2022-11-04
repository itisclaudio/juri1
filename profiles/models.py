# import email
from django.db import models

class Contact(models.Model):
    """ Emails generados por contactanos """
    nombres	    = models.CharField(max_length=50)
    email       = models.EmailField(max_length=254, blank=True, null=True)
    fechahora   = models.DateTimeField(auto_now_add=True)
    titulo	    = models.CharField(max_length=100, blank=True, null=True)
    contenido   = models.TextField()
    enviado	    = models.BooleanField(default=False)

    class Meta:
        ordering = ['-fechahora']
        verbose_name_plural = 'Contactanos'

    def __str__(self):
        return f"{self.fechahora} - {self.nombres}"