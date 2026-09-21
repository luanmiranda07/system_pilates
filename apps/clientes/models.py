from django.db import models
from apps.core.validators import validar_cpf

from apps.core.models import TimeStampedModel



class Cliente(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    cpf = models.CharField(max_length=11, unique=True, validators=[validar_cpf])
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    endereco = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["nome"]


def __str__(self):
        return self.nome