from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from clube_saber.apps.web.models import Page


def home(request: HttpRequest) -> HttpResponse:
    return redirect('/admin')


def landing_page(request: HttpRequest, slug: str) -> HttpResponse:
    page = get_object_or_404(Page, slug=slug)

    return render(
        request=request, template_name='index.html', context={'page': page}
    )
