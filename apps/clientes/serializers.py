from rest_framework import serializers
from apps.clientes.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
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

        read_only_fields = ["id","ativo","criado_em"]