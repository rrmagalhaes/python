from datetime import datetime, timedelta

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# python manage.py makemigrations core (cria arquivo com migrações)
# python manage.py sqlmigrate core (mostra sql que será aplicado)
# python manage.py migrate core XXXX (aplica alterações no banco)
class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True,verbose_name='Data de Criação')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    local = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'events'

    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y - %Hh%M')

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

    def get_evento_atrasado(self):
        if self.data_evento < datetime.now():
            return True
        else:
            return False

    def get_evento_proximo(self):
        if datetime.now() <= self.data_evento < datetime.now() + timedelta(hours=1):
            return True
        else:
            return False