from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from openid.consumer.consumer import DiscoveryFailure

from socialregistration.contrib.openid.views import OpenIDRedirect, OpenIDCallback, OpenIDSetup
from socialregistration.contrib.atlassianid.client import AtlassianIDClient
from socialregistration.contrib.atlassianid.models import AtlassianIDProfile

class AtlassianIDRedirect(OpenIDRedirect):
    client = AtlassianIDClient
    
    def post(self, request):
        request.session['next'] = self.get_next(request)

        ax_attrs = request.POST.getlist('ax_attributes');
        sreg_attrs = request.POST.getlist('sreg_attributes');
        # We don't want to pass in the whole session object as this might not 
        # be pickleable depending on what session backend one is using. 
        # See issue #73
        client = self.get_client()(dict(request.session.items()),
            ax_attrs=ax_attrs, sreg_attrs=sreg_attrs)
        
        request.session[self.get_client().get_session_key()] = client

        try:
            return HttpResponseRedirect(client.get_redirect_url())
        except DiscoveryFailure, e:
            return self.error_to_response(request, {'error': e.message})
        
class AtlassianIDCallback(OpenIDCallback):
    client = AtlassianIDClient
    profile = AtlassianIDProfile
    
    def get(self, request, *args):
        result = super(AtlassianIDCallback, self).get(request, *args)
        
        client = request.session[self.get_client().get_session_key()]
        if not client.is_valid():
            return result
        
        return HttpResponseRedirect(reverse('socialregistration:atlassianid:setup'))
    
class AtlassianIDSetup(OpenIDSetup):
    client = AtlassianIDClient
    profile = AtlassianIDProfile
    