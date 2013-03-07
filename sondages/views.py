# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect
from django.template import Context, loader
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

from sondages.models import Sondage, Choix

# index v.1:
#def index(request):
#    return HttpResponse(u"Hello Fixme. Vous êtes sur l'index des sondages.")

# index v.2:
#def index(request):
#    liste_derniers_sondages = Sondage.objects.order_by('-date_pub')[:5]
#    retour = ', '.join([s.question for s in liste_derniers_sondages])
#    return HttpResponse(retour)
#    liste_derniers_sondages = Sondage.objects.order_by('-date_pub')[:5]
#    contexte = Context({
#        'liste_derniers_sondages': liste_derniers_sondages,
#    })
#    return render(request, 'sondages/index.html', contexte)

# index v.3:
#def index(request):
#    liste_derniers_sondages = Sondage.objects.order_by('-date_pub')[:5]
#    template = loader.get_template('sondages/index.html')
#    contexte = Context({
#        'liste_derniers_sondages': liste_derniers_sondages,
#    })
#    return HttpResponse(template.render(contexte))
    
# index v.4:
#def index(request):
#    liste_derniers_sondages = Sondage.objects.order_by('-date_pub')[:5]
#    contexte = Context({
#        'liste_derniers_sondages': liste_derniers_sondages,
#    })
#    return render(request, 'sondages/index.html', contexte)
    


        
# detail v.1:    
#def detail(request, sondage_id):
#    return HttpResponse("Vous regardez le sondage n° %s." % sondage_id)
        
# detail v.2:
#def detail(request, sondage_id):
#    try:
#        sondage = Sondage.objects.get(pk=sondage_id)
#    except Sondage.DoesNotExist:
#        raise Http404
#    return render(request, 'sondages/detail.html', {'sondage': sondage})
        
# detail v.3:
#def detail(request, sondage_id):
#    sondage = get_object_or_404(Sondage, pk=sondage_id)
#    return render(request, 'sondages/detail.html', {'sondage': sondage})




# resultats v.1:
#def resultats(request, sondage_id):
#    return HttpResponse(u"Vous regardez les résultats du sondage n° %s." % sondage_id)

# resultats v.2:
#def resultats(request, sondage_id):
#    sondage = get_object_or_404(Sondage, pk=sondage_id)
#    return render(request, 'sondages/resultats.html', {'sondage': sondage})




# vote v.1:
#def vote(request, sondage_id):
#    return HttpResponse(u"Vous votez pour le sondage n° %s." % sondage_id)

# vote v.2:
#def vote(request, sondage_id):
#    s = get_object_or_404(Sondage, pk=sondage_id)
#    try:
#        choix_selectionne = s.choix_set.get(pk=request.POST['choix'])
#    except (KeyError, Choix.DoesNotExist):
#        # On réaffiche le formulaire du sondage.
#        return render(request, 'sondages/detail.html', {
#            'sondage': s,
#            'error_message': u"Vous n'avez sélectionné aucun choix.",
#        })
#    else:
#        choix_selectionne.votes += 1
#        choix_selectionne.save()
#        # Toujours utiliser HttpResponseRedirect après le traitement de 
#        # données POST. Cela évite aux données d'être envoyées deux fois si
#        # l'utilisateur utilise le bouton Page précedente.
#        return HttpResponseRedirect(reverse('sondages:resultats', args=(s.id,)))
    
