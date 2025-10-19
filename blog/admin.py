from django.contrib import admin
from .models import Blogs

class BlogsAdmin(admin.ModelAdmin):

    list_display = ["title", "show_on_list", "pub_date"]
    list_filter = ["show_on_list", "pub_date"]

admin.site.register(Blogs, BlogsAdmin)