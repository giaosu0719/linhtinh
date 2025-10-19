from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Blogs

def index(request):
    list_blogs = Blogs.objects.order_by("-pub_date")
    date = [b.pub_date for b in list_blogs]

    list_date_and_blogs = list(zip(list_blogs,date))

    template = loader.get_template("blogs_list.html")


    context = {
        "list_date_and_blogs": list_date_and_blogs,
    }
    
    return HttpResponse(template.render(context, request))

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
        "pub_date_blog": blog.pub_date,
    }
    return HttpResponse(blog_template.render(context, request))