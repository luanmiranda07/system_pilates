from django.shortcuts import render
from rest_framework import viewsets
from apps.professores.models import Professor
from apps.professores.serializers import ProfessorSerializer

class ProfessoresViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        busca = self.request.query_params.get("busca")
        if busca:
            queryset = queryset.filter(nome__icontains=busca)
        return queryset
