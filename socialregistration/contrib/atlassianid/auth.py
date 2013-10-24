from django.contrib.auth.backends import ModelBackend
from django.contrib.sites.models import Site
from socialregistration.contrib.atlassianid.models import AtlassianIDProfile


class AtlassianIDAuth(ModelBackend):
    def authenticate(self, identity=None):
        try:
            return AtlassianIDProfile.objects.get(
                identity=identity,
                site=Site.objects.get_current()
            ).user
        except AtlassianIDProfile.DoesNotExist:
            return None
