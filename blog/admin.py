from django.contrib import admin
from .models import Blogs

class BlogsAdmin(admin.ModelAdmin):

    list_display = ["title", "content", "pub_date"]
    list_filter = ["pub_date"]

admin.site.register(Blogs, BlogsAdmin)