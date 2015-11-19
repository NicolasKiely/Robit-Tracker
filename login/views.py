from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
import common.render
from common.settings import get_page_config


def login_form(request):
    ''' Show login page '''
    return __login_page(request)

def login_auth(request):
    ''' Authenticate login request '''
    uname = request.POST['username']
    passw = request.POST['password']
    user = authenticate(username=uname, password=passw)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/account/login-success/')
        else:
            return HttpResponseRedirect('/account/login-inactive/')
    else:
        return HttpResponseRedirect('/account/login-failed/')

def logout_auth(request):
    ''' Log user out '''
    logout(request)
    return HttpResponseRedirect('/')

def login_success(request):
    ''' Post-login success page '''
    context = get_page_config(request, title='Account Login')
    return render(request, 'account/login-success.html', context)

def login_failed(request):
    ''' Login failed page '''
    return __login_page(request, 'User name or password is wrong')

def login_inactive(request):
    ''' Login failed due to inactivated account '''
    return __login_page(request, 'User account has been deactived')


def __login_page(request, error=''):
    context=get_page_config(request, title='Account Login')
    context['action'] = '/account/auth/'
    context['title'] = 'Log In'
    context['form'] = [
        {'label': 'User Name', 'name': 'username'},
        {'label': 'Password', 'type': 'password', 'name': 'password'}
    ]
    if error != '': context['error'] = error
    return common.render.singleform(request, context)
