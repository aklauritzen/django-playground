from django.shortcuts import render
from ideas.models import Idea

# Create your views here.
def ideas_view(request, *args, **kwargs):
    return render (request, "ideas.html", {})