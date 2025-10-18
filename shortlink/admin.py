from django.contrib import admin
from .models import UrlInput,Domain

class UrlAdmin(admin.ModelAdmin):

    list_display = ["url_original", "url_new", "domain", "instant_forward"]
    list_filter = ["domain", "instant_forward"]

class DomainAdmin(admin.ModelAdmin):

    list_display = ["domain_custom"]

admin.site.register(UrlInput, UrlAdmin)
admin.site.register(Domain, DomainAdmin)