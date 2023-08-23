from django.db import models

from .page import Page


class Contact(models.Model):
    class ReasonChoices(models.IntegerChoices):
        UNKNOWN = 1, 'Desconhecido'
        DOUBT = 2, 'Dúvida'
        SUGGESTION = 3, 'Sugestão'
        CRITICIZE = 4, 'Crítica'

    page = page = models.ForeignKey(
        Page, models.CASCADE, related_name='contacts', null=False, blank=False
    )
    email = models.CharField(
        'Email', max_length=250, null=True, blank=False, db_index=True
    )
    reason = models.PositiveSmallIntegerField(
        'Rasão', choices=ReasonChoices.choices, db_index=True
    )
    message = models.TextField('Mensagem')

    created_at = models.DateTimeField('Data de Criação', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return f'{self.pk} - {self.email}'
