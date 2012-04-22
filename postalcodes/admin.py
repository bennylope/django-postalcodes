from django.contrib import admin

from postalcodes.models import PostalCode


class PostalCodeAdmin(admin.ModelAdmin):
    """
    Admin for the postal code model
    """
    search_fields = ['code', 'city', 'state']
    list_filter = ['country']


admin.site.register(PostalCode, PostalCodeAdmin)
