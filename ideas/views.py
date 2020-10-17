from django.shortcuts import render
from ideas.models import Idea
from .forms import IdeaModelForm


# Create your views here.
def ideas_view(request, *args, **kwargs):
    return render(request, "ideas.html", {})


def idea_create_view(request, *args, **kwargs):
    form = IdeaModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = IdeaModelForm()

    qs = Idea.objects.all()
    # Passes form AND query set with same conext variable
    context = {"form": form, "object_list": qs}
    return render(request, "ideas.html", context)
