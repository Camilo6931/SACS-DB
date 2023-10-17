from django.db import models

class PolicitcasBCK (models.Model):
    id_politica = models.AutoField(primary_key=True)
    id_db = models.ForeignKey('BasesDatos', models.DO_NOTHING, db_column='id_db')
    id_instancia = models.ForeignKey('instancias', models.DO_NOTHING, db_column='id_instancia')
    id_tipobck = models.ForeignKey('tipoBckls', models.DO_NOTHING, db_column='id_tipobck')
    id_frecuencia_bck = models.ForeignKey('periodicidad',models.DO_NOTHING, db_column='id_frecuencia_bck')

    class Meta:
        managed = False
        db_table = 'politicas_bck'
        unique_together = ('id_db', 'id_instancia', 'id_frecuencia_bck')
        verbose_name = 'politicas de backup'
        verbose_name_plural = 'politica bck'
        ordering = ['id_instancia']

    def __str__(self):
        return self.id_instancia.nombre_instancia + ' ' + self.id_db.nombre_db + ' ' + 'backup' + self.id_tipobck.nombre_tipo_bck + ' ' + self.id_frecuencia_bck.frecuencia_bck


    class Peridiocidad(models.Model):
        id_peridiocidad = models.AutoField(primary_key=True)
        frecuencia_bck = models.CharField(max_length=10)

        class Meta:
            managed = False
            db_table = 'peridiocidad'
            verbose_name = 'frecuencia'
            verbose_name_plural = 'frecuencias'
            orderin = ['id_periodicidad']

        def __str__(self):
            return self.frecuencia_bck
        
    
    class BasesDato(models.Model):
        id_db = models.AutoField(primary_key=True)
        nombre_db = models.CharField(unique=True, max_length=100, blank=True, null=True)

        class Meta:
            managed = False
            db_table = 'bases_datos'
            verbose_name = 'Base de datos'
            verbose_name_plural = 'Bases de datos'
            ordering = ['nombre_db']
        
        def __str__(self):
            return self.nombre_db
        
    
    class Tipobckls(models.Model):
        id_tipo_bck = models.IntegerField(primary_key=True)
        nombre_tipo_bck = models.CharField(max_length=20)

        class Meta:
            managed = False
            db_table = 'tipo_bckls'
            verbose_name = 'Tipo de bck'
            verbose_name_plural = 'Tipos de bck'
        
        def __str__(self):
            return self.nombre_tipo_bck

    class Instancia(models.Model):
        id_instancia = models.IntegerField(primary_key=True)
        nombre_instancia = models.CharField(max_length=50)

        class Meta:
            manged = False
            db_table = 'instancias'
            verbose_name = 'Instancia'
            verbose_name_plural = 'Instancias'
        
        def __str__(self):
            return self.nombre_instancia
    
    class Programacionbck(models.Model):
        IP_No_modificar = models.CharField(db_column='IP', max_length=50, blank=True, null=True, editable=False) # Field name made lowercase
        ver_Name_No_Modificar = models.CharField(db_column= 'SERVER_NAME', max_length=50, blank=True,null=True, editable=False) #Field name made lowercase
        Lunes_a_Sábado = models.IntegerField(db_column='CANT_L_S', blank=True, null=True) # Field name made lowercase
        Domingo = models.IntegerField(db_column='CANT_DMG', blank=True, null=True) # Field name made lowercase
        Mensual = models.IntegerField('CANT_MENSUAL', blank=True, null=True)# Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'programacionBck'
        verbose_name = 'programación'
        verbose_name_plural = 'Programación copias diarias por instancia'
        ordering =['Server_Name_No_modificar']

    def __str__(self) -> str:
        return self.IP_No_modificar + ' / ' + self.Server_Name_No_modificar
     
