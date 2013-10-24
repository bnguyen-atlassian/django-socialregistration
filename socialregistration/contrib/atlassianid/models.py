from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.auth import authenticate

class AtlassianIDProfile(models.Model):
    user = models.ForeignKey(User)
    site = models.ForeignKey(Site, default=Site.objects.get_current)
    identity = models.TextField(unique=True)

    def __unicode__(self):
        try:
            return 'AtlassianID profile for %s, via provider %s' % (self.user, self.identity)
        except User.DoesNotExist:
            return 'AtlassianID profile for None, via provider None' 

    def authenticate(self):
        return authenticate(identity=self.identity)