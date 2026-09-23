
from django.core.exceptions import ValidationError

from apps.agenda.models import Aula


def verificar_conflitos(dados, ignorar_id=None):
    ativas = Aula.objects.exclude(status=Aula.Status.CANCELADA)
    if ignorar_id:
        ativas = ativas.exclude(id=ignorar_id)

    if ativas.filter(professor=dados["professor"], data_hora=dados["data_hora"]).exists():
        raise ValidationError({"professor": "Este professor já tem aula nesse horário."})

    if ativas.filter(local=dados["local"], data_hora=dados["data_hora"]).exists():
        raise ValidationError({"local": "Este local já está ocupado nesse horário."})


def marcar_aula(dados):
    verificar_conflitos(dados)

    aula = Aula.objects.create(
        cliente=dados["cliente"],
        professor=dados["professor"],
        data_hora=dados["data_hora"],
        local=dados["local"],
        duracao=dados.get("duracao",50),
        observacoes=dados.get("observacoes",""),
    )

    # aqui vai entrar a chamada do n8n depois
    return aula