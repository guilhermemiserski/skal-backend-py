from django.db import models

class Evento(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    data = models.DateTimeField()
    localizacao = models.CharField(max_length=255)


class Ingresso(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nft_token_id = models.CharField(max_length=255)
    valido = models.BooleanField(default=True)
