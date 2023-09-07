from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactForm
from .models.page import Page


def home(request: HttpRequest) -> HttpResponse:
    return redirect('/admin')


def landing_page(request: HttpRequest, slug: str) -> HttpResponse:
    page = get_object_or_404(Page, slug=slug, enabled=True)

    if request.method == 'POST':
        data = request.POST.copy()
        data['page'] = page.pk
        form = ContactForm(data)
        if not form.is_valid():
            message = 'Houve um erro ao salvar o contato'
        else:
            form.save()
            message = 'Em breve entraremos em contato'

        messages.error(request=request, message=message)

    return render(
        request=request, template_name='index.html', context={'page': page}
    )
