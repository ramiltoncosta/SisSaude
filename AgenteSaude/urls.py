from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'AgenteSaude.familia.views.home', name='home'),
    url(r'^familia/(?P<ende>[\w ]+)/endereco/$','AgenteSaude.familia.views.endereco', name='endereco'),
   # url(r'^familia/endereco/$','AgenteSaude.familia.views.endereco'),
    # url(r'^blog/', include('blog.urls')),

   	url(r'^admin/', include(admin.site.urls)),
)
