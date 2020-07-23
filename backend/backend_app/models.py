from django.db import models

# Create your models here.

class Patient(models.Model):

    class Meta:

        db_table = 'patient'

    name = models.CharField(max_length=200)
    
    date_of_birth = models.DateField(
        auto_now=False,
        auto_now_add=False
    )
    RTPCR = 'RT'
    SOROLOGIA = 'SO'
    ANTIGENOS = 'AG'
    ANTICORPOS = 'AC'
    TEST_TYPE_CHOICES = [
        (RTPCR,'RT-PCR'),
        (SOROLOGIA,'Sorologia'),
        (ANTIGENOS, 'Teste Rápido - Antígenos'),
        (ANTICORPOS,'Teste Rápido - Anticorpos'),
    ] 
    test_type = models.CharField(
        max_length=2,
        choices=TEST_TYPE_CHOICES
    )

    POSITIVO = 'PO'
    NEGATIVO = 'NE'
    TEST_RESULT_CHOICES = [
        (POSITIVO,'Positvo'),
        (NEGATIVO,'Negativo'),
    ]
    test_result = models.CharField(
        max_length=2,
        choices=TEST_RESULT_CHOICES
    )
    
