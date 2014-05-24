from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','copa.views.listaJogo'),
    url(r'^salvar/$','copa.views.salvar'),
)
