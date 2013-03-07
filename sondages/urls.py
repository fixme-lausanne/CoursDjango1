# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from sondages import views

from django.views.generic import DetailView, ListView
from sondages.models import Sondage


urlpatterns = patterns('',

#	 # Urls classiques
#
#	 # ex: /sondages/
#    url(r'^$', views.index, name='index'),
#    # ex: /sondages/5/
#    url(r'^(?P<sondage_id>\d+)/$', views.detail, name='detail'),
#    # ex: /sondages/5/resultats/
#    url(r'^(?P<sondage_id>\d+)/resultats/$', views.resultats, name='resultats'),
#    # ex: /sondages/5/vote/
#    url(r'^(?P<sondage_id>\d+)/vote/$', views.vote, name='vote'),
#    
#    #url(r'^derniers_sondages\.html$', views.index),
    
    
    
#     # Urls génériques
#    url(r'^$',
#        ListView.as_view(
#            queryset=Sondage.objects.order_by('-date_pub')[:5],
#            context_object_name='liste_derniers_sondages',
#            template_name='sondages/index.html'),
#        name='index'),
#    url(r'^(?P<pk>\d+)/$',
#        DetailView.as_view(
#            model=Sondage,
#            template_name='sondages/detail.html'),
#        name='detail'),
#    url(r'^(?P<pk>\d+)/resultats/$',
#        DetailView.as_view(
#            model=Sondage,
#            template_name='sondages/resultats.html'),
#        name='resultats'),
#    url(r'^(?P<sondage_id>\d+)/vote/$', views.vote, name='vote'),
)
