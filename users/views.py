from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import views as auth_views
import datetime

time = datetime.datetime.now()

def get_base_context(context):
    context['time'] = time
    return context

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in!')
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
    }
    get_base_context(context)
    return render(request, 'users/register.html', context=context)

class login(auth_views.LoginView):
    template_name = 'users/login.html'

class logout(auth_views.LogoutView):
    template_name = 'users/logout.html'

