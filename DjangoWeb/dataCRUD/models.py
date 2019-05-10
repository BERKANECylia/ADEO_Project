from django.db import models

class PRG_STUDENT_SITE(models.Model):
    ID_ANO       =models.IntegerField()
    PRG          =models.CharField(max_length=120)
    ANNE_SCOLAIRE=models.CharField(max_length=120)
    SITE         =models.CharField(max_length=120)
    class Meta:
        db_table = 'PRG_STUDENT_SITE'

class ADR_STUDENTS(models.Model):
    ADR_CP      =models.IntegerField()
    ADR_VILLE   =models.CharField(max_length=120)
    ADR_PAYS    =models.CharField(max_length=2)
    ID_ANO      =models.IntegerField()
    class Meta:
        db_table='ADR_STUDENTS'

class STUDENT_INTERNSHIP(models.Model):
    ANNEE           =models.CharField(max_length=120)
    ANNEE_SCOLAIRE  =models.CharField(max_length=120)
    ENTERPRISE      =models.CharField(max_length=120)
    CODE_POSTAL     =models.CharField(max_length=120)
    VILLE           =models.CharField(max_length=120)
    PAYS            =models.CharField(max_length=120)
    SUJET           =models.CharField(max_length=120)
    REMUNERATION    =models.FloatField()
    ID_ANO          =models.IntegerField()
    class Meta:
        db_table='STUDENT_INTERNSHIP'


# Create your models here.
