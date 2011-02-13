from django.conf.urls.defaults import *
from core.views import *
from django.conf import settings

urlpatterns = patterns('django.views.generic.simple',
    (r'^$', 'direct_to_template', {'template' : 'index.html'}),
    #(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT}),
    )