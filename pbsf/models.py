from django.db import models

class Vacina(models.Model):
    NAO_ESPECIFICADO = 'NE'
    ADULTO = 'A'
    CRIANCA = 'C'
    
    PUBLICO_ALVO_CHOICES = [
        (NAO_ESPECIFICADO, 'Não Especificado'),
        (ADULTO, 'Adulto'),
        (CRIANCA, 'Criança'),
    ]
    
    nome = models.CharField(max_length=100)
    publico_alvo = models.CharField(max_length=2, choices=PUBLICO_ALVO_CHOICES, default=NAO_ESPECIFICADO)
    
    def __str__(self):
        return self.nome
