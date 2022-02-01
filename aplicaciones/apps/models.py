from django.db import models

class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    proveedor = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    n_articulos = models.CharField(max_length=4)
    
    def __str__(self):
        return self.proveedor
