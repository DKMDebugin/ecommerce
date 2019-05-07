# Project view module
from django.views.generic import TemplateView
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm


def contact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        print(form.cleaned_data['email'])
        if request.is_ajax():
            json_data = {
                'message': 'Thank you for your submisssion',
            }
            return JsonResponse(json_data)
    if form.errors:
        errors = form.errors.as_json()
        if request.is_ajax():
            return HttpResponse(errors, status=400, content_type='application/json')

    template = 'contact/view.html'
    context = {
        'form': form,
    }
    return render(request, template, context)

class About(TemplateView):
    template_name = 'about.html'


def home(request):
    # print(request.session.get("first_name", 'Unknown')) # getter
    return render(request, 'home.html', {})

class Home(TemplateView):
    template_name = 'home.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        print(request.session.get('first_name'))
