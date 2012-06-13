from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Palavra(models.Model):
    palavra = models.CharField(max_length=232)
    video_url = models.CharField(max_length=255)
    uri = models.CharField(max_length=255)
    votes = models.IntegerField()
    username = models.CharField(max_length=232)
    email = models.CharField(max_length=255)
    validacao = models.CharField(max_length=32)
    def show_user(self):
        user = User.objects.filter(username__exact = self.username)
        if len(user) > 0:
            return user[0].first_name + ' ' + user[0].last_name
        return self.username 

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
