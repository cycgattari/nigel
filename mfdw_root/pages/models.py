from django.db import models
# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=60)
    permalink = models.CharField(max_length=12, unique=True)
    update_date = models.DateTimeField('Last Updated')
    bodytext = models.TextField('Page Content', blank=True)

    def __str__(self):
        return self.title

class Unidades(models.Model):
    unidad = models.IntegerField()
    depto = models.CharField(max_length=10, help_text='Por Ej PBK o 2A')
    nro_medidor = models.CharField(max_length=15, help_text='Numero completo de Medidor')
    propietario = models.CharField(max_length=50)

    def __str__(self):
        return self.depto

class Mediciones(models.Model):
    unidades = models.ForeignKey(Unidades, on_delete=models.CASCADE)
    valor_medidor = models.IntegerField()
    mes_medicion = models.DateTimeField(blank=True, null=True)
