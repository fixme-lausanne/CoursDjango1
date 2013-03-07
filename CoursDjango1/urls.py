from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
##    url(r'^sondages/', include('sondages.urls')),
###    url(r'^sondages/', include('sondages.urls', namespace="sondages")),    
#    url(r'^admin/', include(admin.site.urls)),
)
