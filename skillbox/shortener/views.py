from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Link
from .forms import CreateLinkForm


def index(request):
    link_url = None
    if request.method == 'POST':
        form = CreateLinkForm(request.POST)
        if form.is_valid():
            link = form.save()
            link_url = request.build_absolute_uri(reverse('link-url', args=[link.id]))
        else:
            return render(request, 'index.html', {'form': form, 'link': link_url})
    form = CreateLinkForm()
    return render(request, 'index.html', {'form': form, 'link': link_url})

def activate(request, linkuid=''):
    link = get_object_or_404(Link, id=linkuid)
    link.inc_hits()
    return redirect(link.url)

def error_page(request, linkuid=''):
    return render(request, 'error.html')