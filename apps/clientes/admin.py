from django.contrib import admin
from apps.clientes.models import Cliente
# Register your models fromhere.

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ["nome", "cpf", "email", "telefone", "ativo"]
    search_fields = ["nome", "cpf", "email"]
    list_filter = ["ativo"]