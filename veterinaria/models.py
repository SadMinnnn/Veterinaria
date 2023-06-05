from django.db import models


class registrar(models.Model):
    Usuario = models.CharField(max_length=50)
    Contra = models.CharField(max_length=50)
    Tipo = models.IntegerField()


class registrarmascota(models.Model):
    Nombre = models.CharField(primary_key=True, max_length=50)
    CedulaD = models.CharField(max_length=50)
    Edad = models.IntegerField()
    Especie = models.CharField(max_length=50)
    Raza = models.CharField(max_length=50)
    Color = models.CharField(max_length=50)
    Tamaño = models.IntegerField()
    Peso = models.IntegerField()



class historiaclinica(models.Model): 
    IdOrden = models.AutoField(primary_key=True)
    MedicoVQA=models.CharField(max_length=50)
    MotivoC=models.CharField(max_length=100)
    FechaH=models.DateField()
    Sintomatologia=models.CharField(max_length=100)
    Diagonostico=models.CharField(max_length=200)
    Medicamentov=models.CharField(max_length=50)
    DosisM=models.IntegerField()
    HistorialV=models.DateField()
    MedicamentoA=models.CharField(max_length=50)
    DetalleP=models.CharField(max_length=50)
    AnulaciónO=models.CharField(max_length=50)

class recetarmedicamentos(models.Model):
    IdMedico=models.AutoField(primary_key=True)
    CedulaD=models.IntegerField()
    FechaR=models.DateField()
    NombreMD=models.CharField(max_length=100)
    CedulaV=models.IntegerField()
    
class ventasmedicamentos(models.Model):
    IdFactura=models.CharField(primary_key=True, max_length=100)
    IdDueño=models.IntegerField()
    IdMascota=models.IntegerField()
    IdOrden=models.IntegerField()
    NombreP=models.CharField(max_length=100)
    FechaV=models.DateField()
    Valor=models.IntegerField()
    Cantidad=models.IntegerField()   
