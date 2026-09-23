from django.db import models
from django.db.models import Q
from apps.core.models import TimeStampedModel
from apps.clientes.models import Cliente
from apps.professores.models import Professor

class Aula(TimeStampedModel):
    class Status(models.TextChoices):
            AGENDADA = "AGENDADA", "Agendada"
            CONCLUIDA = "CONCLUIDA", "Concluída"
            CANCELADA = "CANCELADA", "Cancelada"
            REALIZADA = "REALIZADA", "Realizada"

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    duracao = models.PositiveSmallIntegerField(default=50)
    local = models.CharField(max_length=255)
    status = models.CharField(
        max_length=15,choices=Status.choices, default=Status.AGENDADA
    )
    observacoes = models.TextField(blank=True, null=True)

  
    class Meta:
        ordering = ["data_hora"]
        constraints = [
            models.UniqueConstraint(
                fields=["professor", "data_hora"],
                condition=~Q(status="CANCELADA"),
                name="professor_sem_conflito",
            ),
            models.UniqueConstraint(
                fields=["local", "data_hora"],
                condition=~Q(status="CANCELADA"),
                name="local_sem_conflito",
            ),
        ]

    def __str__(self):
        return f"Aula de {self.cliente.nome} com {self.professor.nome} às {self.data_hora} telefone {self.professor.telefone} no local {self.local} - Status: {self.status}"
