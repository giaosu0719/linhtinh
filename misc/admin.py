from django.contrib import admin
from .models import File

class FileAdmin(admin.ModelAdmin):

    list_display = ["name_file", "upload_date"]
    list_filter = ["upload_date"]

admin.site.register(File, FileAdmin)
