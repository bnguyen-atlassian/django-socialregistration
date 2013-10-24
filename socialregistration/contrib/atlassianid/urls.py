from django.conf import settings
from django.conf.urls.defaults import *

from socialregistration.contrib.atlassianid.views import AtlassianIDRedirect, AtlassianIDCallback, AtlassianIDSetup

urlpatterns = patterns('',
    url('^redirect/$', AtlassianIDRedirect.as_view(), name='redirect'),
    url('^callback/$', AtlassianIDCallback.as_view(), name='callback'),
    url('^setup/$', AtlassianIDSetup.as_view(), name='setup'),
)
