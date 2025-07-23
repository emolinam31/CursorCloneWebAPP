from django.db import models
from django.utils import timezone

# Create your models here.

class Feature(models.Model):
    """
    Modelo para las características destacadas de Cursor
    """
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    icon = models.CharField(max_length=100, default="code", verbose_name="Icono")
    is_active = models.BooleanField(default=True, verbose_name="Activo")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Creado en")
    
    class Meta:
        verbose_name = "Característica"
        verbose_name_plural = "Características"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title


class Testimonial(models.Model):
    """
    Modelo para testimonios de usuarios
    """
    author = models.CharField(max_length=100, verbose_name="Autor")
    position = models.CharField(max_length=100, verbose_name="Cargo")
    content = models.TextField(verbose_name="Contenido")
    avatar = models.URLField(blank=True, null=True, verbose_name="Avatar URL")
    is_active = models.BooleanField(default=True, verbose_name="Activo")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Creado en")
    
    class Meta:
        verbose_name = "Testimonio"
        verbose_name_plural = "Testimonios"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.author} - {self.position}"


class NewsletterSubscription(models.Model):
    """
    Modelo para suscripciones al newsletter
    """
    email = models.EmailField(unique=True, verbose_name="Email")
    is_active = models.BooleanField(default=True, verbose_name="Activo")
    subscribed_at = models.DateTimeField(default=timezone.now, verbose_name="Suscrito en")
    
    class Meta:
        verbose_name = "Suscripción Newsletter"
        verbose_name_plural = "Suscripciones Newsletter"
        ordering = ['-subscribed_at']
    
    def __str__(self):
        return self.email 