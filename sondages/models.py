# -*- coding: utf-8 -*-
from django.db import models
import datetime
from django.utils import timezone



# sondage v.1:
#class Sondage(models.Model):
#    question = models.CharField(max_length=200)
#    date_pub = models.DateTimeField('date de publication')


# sondage v.2:
#class Sondage(models.Model):
#    question = models.CharField(max_length=200)
#    date_pub = models.DateTimeField('date de publication')
#    
#    def __unicode__(self):
#    	return self.question


# sondage v.3:
#class Sondage(models.Model):
#    question = models.CharField(max_length=200)
#    date_pub = models.DateTimeField('date de publication')
#    
#    def __unicode__(self):
#    	return self.question
#    	
#    def publie_recemment(self):
#        return self.date_pub >= timezone.now() - datetime.timedelta(days=1)


# sondage v.4:
#class Sondage(models.Model):
#    question = models.CharField(max_length=200)
#    date_pub = models.DateTimeField('date de publication')
#    
#    def __unicode__(self):
#    	return self.question
#    	
#    def publie_recemment(self):
#        return self.date_pub >= timezone.now() - datetime.timedelta(days=1)
#    publie_recemment.admin_order_field = 'date_pub'
#    publie_recemment.boolean = True
#    publie_recemment.short_description = 'Publié récemment?'
        


# choix v.1:
#class Choix(models.Model):
#    sondage = models.ForeignKey(Sondage)
#    texte_choix = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)


# choix v.2:
#class Choix(models.Model):
#    sondage = models.ForeignKey(Sondage)
#    texte_choix = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)
#    
#    def __unicode__(self):
#    	return self.texte_choix
