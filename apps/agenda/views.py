from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError

from apps.agenda.models import Aula
from apps.agenda.serializers import AulaSerializer
from apps.agenda.services import marcar_aula


class AulaViewSet(viewsets.ModelViewSet):
    queryset = Aula.objects.select_related("cliente", "professor")
    serializer_class = AulaSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        inicio = self.request.query_params.get("inicio")
        fim = self.request.query_params.get("fim")
        if inicio:
            qs = qs.filter(data_hora__date__gte=inicio)
        if fim:
            qs = qs.filter(data_hora__date__lte=fim)
        return qs

    def perform_create(self, serializer):
        try:
            aula = marcar_aula(serializer.validated_data)
        except DjangoValidationError as e:
            raise ValidationError(e.message_dict)
        serializer.instance = aula

    def perform_destroy(self, instance):
        instance.status = Aula.Status.CANCELADA
        instance.save()