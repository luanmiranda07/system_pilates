from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError

from apps.agenda.models import Aula
from apps.agenda.serializers import AulaSerializer
from apps.agenda.services import marcar_aula, verificar_conflitos


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

    def perform_update(self, serializer):
        instancia = serializer.instance
        dados = {
            "professor": serializer.validated_data.get("professor", instancia.professor),
            "local": serializer.validated_data.get("local", instancia.local),
            "data_hora": serializer.validated_data.get("data_hora", instancia.data_hora),
        }
        status = serializer.validated_data.get("status", instancia.status)
        if status != Aula.Status.CANCELADA:
            try:
                verificar_conflitos(dados, ignorar_id=instancia.id)
            except DjangoValidationError as e:
                raise ValidationError(e.message_dict)
        serializer.save()

    def perform_destroy(self, instance):
        instance.status = Aula.Status.CANCELADA
        instance.save()