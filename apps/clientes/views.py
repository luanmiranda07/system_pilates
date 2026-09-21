from django.shortcuts import render
from rest_framework import viewsets
from apps.clientes.models import Cliente
from apps.clientes.serializers import ClienteSerializer
from django.db.models import Q

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        busca = self.request.query_params.get("busca")
        if busca:
            queryset = queryset.filter(Q(nome__icontains=busca)
                                       | Q(cpf__icontains=busca)
                                       | Q(telefone__icontains=busca))
        return queryset
