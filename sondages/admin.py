# -*- coding: utf-8 -*-
from django.contrib import admin
from sondages.models import Sondage, Choix


# choix v.1:
#admin.site.register(Choix)


# choix v.2:
#class InlineChoix(admin.StackedInline):
#    model = Choix
#    extra = 3


# choix v.3:
#class InlineChoix(admin.TabularInline):
#    model = Choix
#    extra = 3




# sondage v.1:
#admin.site.register(Sondage)


# sondage v.2:
#class AdminSondage(admin.ModelAdmin):
#    fields = ['date_pub', 'question']
#
#admin.site.register(Sondage, AdminSondage)


# sondage v.3:
#class AdminSondage(admin.ModelAdmin):
#    fieldsets = [
#        (None,        {'fields': ['question']}),
#        ('Info date', {'fields': ['date_pub']}),
#    ]
#
#admin.site.register(Sondage, AdminSondage)


# sondage v.4:
#class AdminSondage(admin.ModelAdmin):
#    fieldsets = [
#        (None,        {'fields': ['question']}),
#        ('Info date', {'fields': ['date_pub'], 'classes': ['collapse']}),
#    ]
#
#admin.site.register(Sondage, AdminSondage)


# sondage v.5:
#class AdminSondage(admin.ModelAdmin):
#    fieldsets = [
#        (None,        {'fields': ['question']}),
#        ('Info date', {'fields': ['date_pub'], 'classes': ['collapse']}),
#    ]
#    inlines = [InlineChoix]
#
#admin.site.register(Sondage, AdminSondage)


# sondage v.6:
#class AdminSondage(admin.ModelAdmin):
#    fieldsets = [
#        (None,        {'fields': ['question']}),
#        ('Info date', {'fields': ['date_pub'], 'classes': ['collapse']}),
#    ]
#    inlines = [InlineChoix]
#    list_display = ('question', 'date_pub')
#
#admin.site.register(Sondage, AdminSondage)


# sondage v.7:
#class AdminSondage(admin.ModelAdmin):
#    fieldsets = [
#        (None,        {'fields': ['question']}),
#        ('Info date', {'fields': ['date_pub'], 'classes': ['collapse']}),
#    ]
#    inlines = [InlineChoix]
#    list_display = ('question', 'date_pub', 'publie_recemment')
##    list_filter = ['date_pub']
##    search_fields = ['question']
##    date_hierarchy = 'date_pub'
#
#admin.site.register(Sondage, AdminSondage)


