from django.contrib import admin
from .models import File, Shortener, Domain

class FileAdmin(admin.ModelAdmin):

    list_display = ["name_file", "upload_date"]
    list_filter = ["upload_date"]


class ShortenerAdmin(admin.ModelAdmin):

    list_display = ["url_original", "url_new", "domain", "instant_forward"]
    list_filter = ["domain", "instant_forward"]

class DomainAdmin(admin.ModelAdmin):

    list_display = ["domain_custom"]

admin.site.register(Shortener, ShortenerAdmin)
admin.site.register(Domain, DomainAdmin)
admin.site.register(File, FileAdmin)
