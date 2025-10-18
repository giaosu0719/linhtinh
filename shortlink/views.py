from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import UrlInput


def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())


def forwarding(request, short_url):
    forwarding_template = loader.get_template("forwarding.html")
    not_found_404_template = loader.get_template("404.html")

    try:
        url = get_object_or_404(UrlInput, url_new=short_url)
    except:
        return HttpResponse(not_found_404_template.render())

    if url.domain:
        expected_domain = url.domain.domain_custom.strip()
        current_domain = request.get_host().strip()

        if expected_domain != current_domain:
            return HttpResponse(not_found_404_template.render())

        short_full = f"{expected_domain}/{short_url}"
    else:
        short_full = f"{request.get_host()}/{short_url}"

    if url.instant_forward:
        return HttpResponseRedirect(url.url_original)

    context = {
        "url_original": url.url_original,
        "domain_custom": short_full,
    }
    return HttpResponse(forwarding_template.render(context, request))
