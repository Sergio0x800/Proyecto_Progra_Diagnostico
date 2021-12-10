from django.db import models

class DetalleDiagnostico(models.Model):
  IdDetalle = models.BigAutoField(primary_key=True)
  Categoria = models.CharField(max_length=100)
  Opcion = models.CharField(max_length=100)
  Descripcion = models.CharField(max_length=100)
  NumeroParte = models.CharField(max_length=13)
  DetalleSolicitud = models.CharField(max_length=13)

class Diagnosticos(models.Model):
  IdDiagnostico = models.BigAutoField(primary_key=True)
  Placa = models.CharField(max_length=100)
  Cliente = models.CharField(max_length=100)
  Fecha = models.CharField(max_length=100)
  Tipo = models.CharField(max_length=13)
  Estado = models.CharField(max_length=100)
  Detalles=models.ForeignKey(DetalleDiagnostico,null=True, on_delete=models.CASCADE)

  
