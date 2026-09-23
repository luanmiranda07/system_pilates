import re

from django.core.exceptions import ValidationError


def validar_cpf(valor):
    digitos = re.sub(r"\D", "", valor or "")

    if len(digitos) != 11:
        raise ValidationError("O CPF deve ter 11 dígitos.")

    if digitos == digitos[0] * 11:
        raise ValidationError("CPF inválido.")

    def calcular(quantidade):
        soma = sum(int(digitos[i]) * (quantidade + 1 - i) for i in range(quantidade))
        resto = (soma * 10) % 11
        return 0 if resto == 10 else resto

    if calcular(9) != int(digitos[9]) or calcular(10) != int(digitos[10]):
        raise ValidationError("CPF inválido.")




def nomes_sem_caracteres_especiais(valor):
    if not re.match(r"^[a-zA-ZÀ-ÿ\s]+$", valor):
        raise ValidationError("O nome não pode conter caracteres especiais ou números.") 
    return valor

def validar_telefone(valor):
    if not re.match(r"^\+?\d{10,15}$", valor):
        raise ValidationError("O telefone deve conter apenas números e pode incluir o código do país.")      
    return valor