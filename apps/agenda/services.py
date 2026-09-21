
from django.core.exceptions import ValidationError

from apps.agenda.models import Aula


def marcar_aula(dados):
    conflito_professor = Aula.objects.filter(
        professor=dados["professor"],
        data_hora=dados["data_hora"],
    ).exclude(status=Aula.Status.CANCELADA).exists()

    if conflito_professor:
        raise ValidationError({"professor": "Este professor já tem aula nesse horário."})

    conflito_local = Aula.objects.filter(
        local=dados["local"],
        data_hora=dados["data_hora"],
    ).exclude(status=Aula.Status.CANCELADA).exists()

    if conflito_local:
        raise ValidationError({"local": "Este local já está ocupado nesse horário."})

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