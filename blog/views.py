from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Blogs


def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())

def blog_view(request, blog_title):
    blog_template = loader.get_template("blog.html")
    not_found_404_template = loader.get_template("404.html")

    try:
        blog = get_object_or_404(Blogs, title = blog_title)
    except:
        return HttpResponse(not_found_404_template.render())

    context = {
        "content_blog": blog.content,
        "title_blog": blog.title,
    }
    return HttpResponse(blog_template.render(context, request))
