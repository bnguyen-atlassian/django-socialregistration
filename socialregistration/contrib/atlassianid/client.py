from django.conf import settings
from django.core.urlresolvers import reverse
import urlparse

from socialregistration.contrib.openid.client import OpenIDClient

class AtlassianIDClient(OpenIDClient):
    def __init__(self, session_data, **kwargs):
        endpoint_url = settings.SOCIAL_REGISTRATION_ATLASSIANID_URL
        super(AtlassianIDClient, self).__init__(session_data, endpoint_url, **kwargs)
    
    def get_callback_url(self, **kwargs):
        return urlparse.urljoin(self.get_realm(),
            reverse('socialregistration:atlassianid:callback'))    
        
    @classmethod
    def allow_signups(cls):
        return True
    