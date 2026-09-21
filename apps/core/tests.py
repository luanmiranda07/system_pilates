from django.test import TestCase
from django.core.exceptions import ValidationError
from validators import validar_cpf
# Create your tests here

cpf = input("Digite um CPF para validar: ")
try:
    validar_cpf(cpf)
    print("CPF válido.")
except ValidationError as e:
    print(f"CPF inválido: {e}")