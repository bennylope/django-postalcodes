from django.db import models
from django.utils.translation import ugettext_lazy as _


class PostalCode(models.Model):
    """
    A model to represent postal codes and their location data.

    Originally based on the Census Bureau's zip code data
    http://www.census.gov/geo/www/gazetteer/gazetteer2010_layout.html#zcta
    """
    code = models.CharField(max_length=10)
    #country = models.CharField(max_length=2)
    latitude = models.DecimalField(decimal_places=6, max_digits=9)
    longitude = models.DecimalField(decimal_places=6, max_digits=9)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = _("Postal Code")
        verbose_name_plural = _("Postal Codes")

    def __unicode__(self):
        return u"%s" % self.code
