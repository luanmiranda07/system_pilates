from django.contrib import admin
from apps.professores.models import Professor
# Register your models fromhere.

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ["nome", "cpf", "email", "telefone", "ativo"]
    search_fields = ["nome", "cpf", "email"]
    list_filter = ["ativo"]