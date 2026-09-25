from rest_framework import serializers
from apps.clientes.models import Cliente
from apps.professores.models import Professor
from apps.agenda.models import Aula

class AulaSerializer(serializers.ModelSerializer):
    cliente_nome = serializers.CharField(source="cliente.nome", read_only=True)
    professor_nome = serializers.CharField(source="professor.nome", read_only=True)
    telefone_professor = serializers.CharField(source="professor.telefone", read_only=True)

    class Meta:
        model = Aula
        fields = [
            "id",
            "cliente_nome",
            "cliente",
            "professor_nome",
            "professor",
            "telefone_professor",
            "data_hora",
            "duracao",
            "local",
            "status",
            "observacoes",
            "criado_em",
        ]
        # Conflitos de horário são checados em services.py (ignorando aulas canceladas).
        validators = []
        