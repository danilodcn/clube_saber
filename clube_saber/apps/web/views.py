from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactForm
from .models.page import Page


def home(request: HttpRequest) -> HttpResponse:
    return redirect('/admin')


def landing_page(request: HttpRequest, slug: str) -> HttpResponse:
    page = get_object_or_404(Page, slug=slug)

    if request.method == 'POST':
        form = ContactForm({**request.POST, 'page': page.pk})
        if not form.is_valid():
            message = ''
        else:
            form.save()
            message = 'Em breve entraremos em contato'

        messages.error(request=request, message=message)

    return render(
        request=request, template_name='index.html', context={'page': page}
    )
