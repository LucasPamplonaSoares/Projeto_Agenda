from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True) # Pode ser em branco e nulo
    data_evento = models.DateField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True) # Inserir a hora atual
    usuario : models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento' # Atualiza o nome da tabela

    def __str__(self):
        return self.titulo # Por o nome do evento que eu cadastrei

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y, %H:%M Hrs')

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-dT%H:%M')

    def get_evento_atrasado(self):
        if self.data_evento < datetime.now():
            return True
        else:
            return False
