from django.db import models

# Create your models here.
class Palavra(models.Model):
    palavra = models.CharField(max_length=232)
    video_url = models.CharField(max_length=255)
    uri = models.CharField(max_length=255)
    votes = models.IntegerField()
    username = models.CharField(max_length=232)
    email = models.CharField(max_length=255)
    validacao = models.CharField(max_length=32)
    def __unicode__(self):
        return self.palavra

class Pagina(models.Model):
    path = models.CharField(max_length=232)
    title = models.CharField(max_length=232)
    content = models.TextField()
    def __unicode__(self):
        return self.title

class Configuracao(models.Model):
    codigo = models.CharField(max_length=232)
    conteudo = models.TextField()
    def __unicode__(self):
        return self.codigo
