from django.db import models

# Create your models here.
class servicios(models.Model):
    pk_servicios = models.AutoField(primary_key=True, null=False, blank=False)
    tipo = models.CharField(max_length=50, null=False, blank=False)
    precio = models.IntegerField(null=False, blank=False)
    descuento = models.IntegerField(null=False, blank=False)
    imagenes= models.URLField(max_length=8000, blank=False, null=False,default='https://ca-times.brightspotcdn.com/dims4/default/87be6da/2147483647/strip/true/crop/1970x1108+39+0/resize/1200x675!/quality/90/?url=https%3A%2F%2Fcalifornia-times-brightspot.s3.amazonaws.com%2F12%2Fa5%2F79e097ccf62312d18a025f22ce48%2Fhoyla-recuento-11-cosas-aman-gatos-top-001')
    class Meta:
        verbose_name= 'servicios'
        verbose_name_plural = 'servicioss'
        ordering = ['tipo']

    def __str__(self):
        return "{0}".format(self.tipo)


class barberia(models.Model):
    pk_barberia = models.AutoField(primary_key=True, null=False, blank=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    direccion = models.CharField(max_length=60, null=False, blank=False)
    telefono = models.IntegerField(null=False, blank=False)

    class Meta:
        verbose_name= 'barberia'
        verbose_name_plural = 'barberias'
        ordering = ['nombre']

    def __str__(self):
        return "{0}".format(self.nombre)

class empleados(models.Model):
    pk_empleados = models.AutoField(primary_key=True, null=False, blank=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellidos = models.CharField(max_length=60, null=False, blank=False)
    direccion = models.CharField(max_length=60, null=False, blank=False)
    telefono = models.IntegerField(null=False, blank=False)
    Sexo = models.CharField(max_length=15, null=False, blank=False)
    fk_barberia = models.ForeignKey(barberia, on_delete=models.CASCADE)

    class Meta:
        verbose_name= 'empleados'
        verbose_name_plural = 'empleadoss'
        ordering = ['nombre']

    def __str__(self):
        return "{0}".format(self.nombre)

class cliente(models.Model):
    pk_cliente = models.AutoField(primary_key=True, null=False, blank=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellidos = models.CharField(max_length=60, null=False, blank=False)
    c_cita = models.CharField(max_length=70, null=False, blank=False)
    fk_barberia = models.ForeignKey(barberia, on_delete=models.CASCADE)
    fk_servicios = models.ForeignKey(servicios, on_delete=models.CASCADE)

    class Meta:
        verbose_name= 'cliente'
        verbose_name_plural = 'clientes'
        ordering = ['nombre']

    def __str__(self):
        return "{0}".format(self.nombre)

class cita(models.Model):
    pk_cita = models.AutoField(primary_key=True, null=False, blank=False)
    fecha = models.CharField(max_length=50, null=False, blank=False)
    horario = models.CharField(max_length=20, null=False, blank=False)
    fk_barberia = models.ForeignKey(barberia, on_delete=models.CASCADE)
    fk_cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)

    class Meta:
        verbose_name= 'cita'
        verbose_name_plural = 'citas'
        ordering = ['fecha']

    def __str__(self):
        return "{0}".format(self.fecha)

