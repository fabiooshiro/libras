from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'dicionario.views.home', name='home'),
    # url(r'^libras/', include('libras.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^search/$', 'dicionario.views.search'),
    url(r'^letra/(?P<letra>\w+)/$', 'dicionario.views.letra'),
    url(r'^dicionario/(?P<palavra>[^/]+)/$', 'dicionario.views.palavra'),
    url(r'^dicionario/(?P<palavra>[^/]+)/(?P<palavra_id>\d+)/$', 'dicionario.views.palavraid'),
    url(r'^amin/', include(admin.site.urls)),
    url(r'^pg/(?P<path>.*)', 'dicionario.views.pagina'),
    url(r'^colaborar.*', 'dicionario.views.colaborar'),
    url(r'^obrigado.*', 'dicionario.views.obrigado'),
    url(r'^confirmar/(?P<validacao>.*)', 'dicionario.views.confirmar'),
)
