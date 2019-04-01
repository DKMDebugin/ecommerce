# Project view module
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from django.views.generic import TemplateView
from django.shortcuts import render, redirect

from .forms import ContactForm, LoginForm, RegisterForm


User = get_user_model()
def register_page(request):
    form        = RegisterForm(request.POST or None)
    context     = {
        'form': form,
    }
    if form.is_valid():
        print(form.cleaned_data)
        username    = form.cleaned_data.get('username')
        email       = form.cleaned_data.get('email')
        password    = form.cleaned_data.get('password')
        new_user    = User.objects.create_user(username, email, password)
        print(new_user)
    template = 'auth/register.html'
    return render(request, template, context)

def logout_view(request):
    logout(request)
    return redirect('home')

def login_page(request):
    form        = LoginForm(request.POST or None)
    context     = {
        'form': form,
    }
    print(request.user.is_authenticated)
    if form.is_valid():
        user = authenticate(request, username=form.cleaned_data.get('username'),
                                    password=form.cleaned_data.get('password'))
        if user is not None:
             login(request, user)
             context['form'] = LoginForm()
             return redirect('home')
        else:
            messages.success(request, 'Invalid Login. Incorrect Username/Password', 'alert alert-warning alert-dismissible')

    template    = 'auth/login.html'
    return render(request, template, context)

def contact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        print(form.clean_data)

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
