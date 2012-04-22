from django.db import models
from django.utils.translation import ugettext_lazy as _


class PostalCode(models.Model):
    """
    A model to represent postal codes and their location data.

    Originally based on the Census Bureau's zip code data
    http://www.census.gov/geo/www/gazetteer/gazetteer2010_layout.html#zcta
    """
    code = models.CharField(_("postal code"), max_length=20)
    country = models.CharField(_("country"), max_length=2)
    city = models.CharField(_("city"), max_length=200, blank=True, null=True)
    state = models.CharField(_("state"), max_length=100, blank=True, null=True)
    latitude = models.DecimalField(_("latitude"), decimal_places=6, max_digits=9, blank=True,
            null=True)
    longitude = models.DecimalField(_("longitude"), decimal_places=6, max_digits=9, blank=True,
            null=True)

    class Meta:
        verbose_name = _("Postal code")
        verbose_name_plural = _("Postal codes")

    def __unicode__(self):
        return u"%s" % self.code
