from django.http import Http404
from django.shortcuts import render

from projects.models import Project

# Create your views here.

def home_view(request, *args, **kwargs):
    context = {"name": "Anders"}
    return render(request, "home.html", context)

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def project_detail_view(request, pk):
    try:
        obj = Project.objects.get(pk=pk)
    except Project.DoesNotExists:
        raise Http404 # Renders html page, with HTTP status code 404

    return render(request, "projects/project_details.html", {"project": obj})

