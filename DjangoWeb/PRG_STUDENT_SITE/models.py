from django.db import models

class PRG_STUDENT_SITE(models.Model):
    ID_ANO       =models.IntegerField()
    PRG          =models.CharField(max_length=120)
    ANNE_SCOLAIRE=models.CharField(max_length=120)
    SITE         =models.CharField(max_length=120)
# Create your models here.
