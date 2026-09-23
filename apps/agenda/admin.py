from django.contrib import admin
from apps.agenda.models import Aula


@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = ["data_hora", "cliente", "professor", "telefone_professor", "local", "status"]
    list_filter = ["status", "professor", "local"]
    search_fields = ["cliente__nome", "professor__nome"]


    @admin.display(description="Telefone do professor")
    def telefone_professor(self, obj):
        return obj.professor.telefone