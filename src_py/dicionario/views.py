from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from dicionario.models import Palavra, Pagina, Configuracao
import smtplib
import random
import string


def home(request):
    return palavra(request, 'Amar')

def palavra(request, palavra):
    palavra_list = Palavra.objects.filter(uri__exact = palavra).order_by('votes')
    mais_votada = palavra_list[0]
    letra = mais_votada.palavra[0]
    palavra_side_list = Palavra.objects.filter(palavra__istartswith = letra).filter(validacao__exact = 'ok').values('palavra', 'uri').distinct().order_by('palavra')
    return render_to_response('dicionario/palavra.html', {'palavra_side_list': palavra_side_list, 'palavra_list': palavra_list, 'mais_votada': mais_votada, 'letra': letra})

def palavraid(request, palavra, palavra_id):
    palavra_list = Palavra.objects.filter(uri__exact = palavra).order_by('votes')
    mais_votada = Palavra.objects.get(id = palavra_id)
    letra = mais_votada.palavra[0]
    palavra_side_list = Palavra.objects.filter(palavra__istartswith = letra).filter(validacao__exact = 'ok').values('palavra', 'uri').distinct().order_by('palavra')
    return render_to_response('dicionario/palavra.html', {'palavra_side_list': palavra_side_list, 'palavra_list': palavra_list, 'mais_votada': mais_votada, 'letra': letra})

def letra(request, letra):
    palavra_side_list = Palavra.objects.filter(palavra__istartswith = letra).filter(validacao__exact = 'ok').values('palavra', 'uri').distinct().order_by('palavra')
    return render_to_response('dicionario/letra.html', {'palavra_side_list': palavra_side_list, 'letra': letra})

def search(request):
    crit = request.GET.get('q')
    palavra_list = Palavra.objects.filter(palavra__istartswith = crit).filter(validacao__exact = 'ok').order_by('palavra')
    letra = crit[0]
    palavra_side_list = Palavra.objects.filter(palavra__istartswith = letra).filter(validacao__exact = 'ok').values('palavra', 'uri').distinct().order_by('palavra')    
    return render_to_response('dicionario/search.html', {'palavra_list': palavra_list, 'letra': letra, 'palavra_side_list': palavra_side_list}) 

def pagina(request, path):
    pagina = Pagina.objects.get(path = path) 
    return render_to_response('dicionario/pagina.html', {'pagina': pagina})

@csrf_protect
def colaborar(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('dicionario/colaborar.html', c)

def codegen(size, id):
    chars=string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for x in range(size)) + `id`

def confirmar(request, validacao):
    try:
        palavra = Palavra.objects.get(validacao=validacao)
        palavra.validacao = 'ok'
        palavra.save()
        msg = 'Confirmado, valeu!'
    except: 
        msg = 'Obrigado'
    return render_to_response('dicionario/obrigado.html', {'msg': msg})
    
@csrf_protect
def obrigado(request):
    config = Configuracao.objects.get(codigo='email')
    sys_email = config.conteudo.split(':')
    post = request.POST
    palavra = Palavra.objects.create(palavra=post.get('palavra'), username=post.get('username'), votes=0, video_url=post.get('video_url'), email=post.get('email'))
    palavra.uri = palavra.palavra.replace('/', '-').replace(' ', '-').replace('?', '')
    palavra.save()
    palavra.validacao = codegen(20, palavra.id)
    palavra.save()
    to = post.get('email')
    gmail_user = sys_email[0]
    gmail_pwd = sys_email[1]
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(gmail_user, gmail_pwd)
    header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:Libras obrigado a vc\n'
    msg = header + '\n Obrigado, confirme acessando o link http://libras.w3ca.com.br/confirmar/' + palavra.validacao + ' . \n\n'
    smtpserver.sendmail(gmail_user, to, msg)
    smtpserver.close()
    msg = 'Mandamos um e-mail para confirmar. Muito obrigado!'
    return render_to_response('dicionario/obrigado.html', {'msg': msg})
