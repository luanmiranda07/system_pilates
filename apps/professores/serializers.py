from rest_framework import serializers
from apps.professores.models import Professor

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = [
            "id",
            "nome",
            "email",    
            "telefone",
            "cpf",
            "data_nascimento",
            "endereco",
            "ativo",
            "criado_em"
        ]

        read_only_fields = ["id", "criado_em"]