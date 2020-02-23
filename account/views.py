from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username = cd['username'],
                                password = cd['password']
                                )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Вход выполнен')
                else:
                    return HttpResponse('Аккаунт закрыт')
            else:
                return HttpResponse('Неверный логин или пароль')
    else:
        form = LoginForm()
    return render(request, 'account/templates/registration/login.html', {form: form})

# @login_required
def index(request):
    return render(request,
                  'account/index.html',
                  {'section': 'index'})



def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})