from django.contrib.auth import authenticate, login, get_user_model
from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

from .forms import LoginForm, RegisterForm, GuestForm
from .models import GuestEmail

User = get_user_model()

def guest_register_view(request):
    form            = GuestForm(request.POST or None)
    context         = {
            'form': form,
        }
    next_           = request.GET.get('next')
    next_post       = request.POST.get('next')
    redirect_path   = next_ or next_post or None

    if form.is_valid():
        email = form.cleaned_data.get('email')
        new_guest_email = GuestEmail.objects.create(email=email)
        request.session['guest_email_id'] = new_guest_email.id
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect('/register/')
    return redirect('/register/')


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
    template = 'accounts/register.html'
    return render(request, template, context)


def login_page(request):
    form            = LoginForm(request.POST or None)
    context         = {
            'form': form,
        }
    next_           = request.GET.get('next')
    next_post       = request.POST.get('next')
    redirect_path   = next_ or next_post or None

    if form.is_valid():
        user = authenticate(request, username=form.cleaned_data.get('username'),
                                    password=form.cleaned_data.get('password'))
        if user is not None:
            login(request, user)
            try:
                del request.session['guest_email_id']
            except:
                pass
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect('/')
        else:
            messages.success(request, 'Invalid Login. Incorrect Username/Password', 'alert alert-warning alert-dismissible')

    template    = 'accounts/login.html'
    return render(request, template, context)