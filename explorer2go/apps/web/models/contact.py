from django.db import models

from .page import Page


class Contact(models.Model):
    class ReasonChoices(models.TextChoices):
        UNKNOWN = 'UNKNOWN', 'Desconhecido'
        DOUBT = 'DOUBT', 'Dúvida'
        SUGGESTION = 'SUGGESTION', 'Sugestão'
        CRITICIZE = 'CRITICIZE', 'Crítica'

    page = page = models.ForeignKey(
        Page, models.CASCADE, related_name='contacts', null=False, blank=False
    )
    email = models.CharField(
        'Email', max_length=250, null=True, blank=False, db_index=True
    )
    reason = models.CharField(
        'Rasão', choices=ReasonChoices.choices, max_length=20, db_index=True
    )
    message = models.TextField('Mensagem')

    created_at = models.DateTimeField('Data de Criação', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return f'{self.pk} - {self.email}'
