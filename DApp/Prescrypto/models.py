from django.db import models

# Create your models here.
class Users(models.Model):
    #campos: nombre, apellido, dui, wallet, pk, password
    firstname = models.CharField(max_length=50, verbose_name="Nombres")
    lastname = models.CharField(max_length=50, verbose_name="Apellidos")
    username = models.CharField(max_length=50, verbose_name="Username", unique=True)
    dui = models.CharField(max_length=50, verbose_name="DUI", unique=True, default="")
    wallet = models.CharField(max_length=500, verbose_name="Wallet", unique=True)
    private_key = models.CharField(max_length=500, verbose_name="Private key", unique=True)
    password = models.CharField(max_length=20, verbose_name="Contraseña")