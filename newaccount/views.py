from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.shortcuts import render
import urllib
import common.render
from common.settings import get_page_config


def form(request):
    ''' The signup form webpage '''
    context = get_page_config(title='New User Sign Up')
    context['form'] = [
        {'label': 'User Name', 'name': 'username'},
        {'label': 'Email Address', 'name': 'email'},
        {'label': 'Password', 'type': 'password', 'name':'password'},
        {'label': 'Re-enter Password', 'type': 'password', 'id':'repass'}
    ]
    context['validators'] = [ 'signup/newaccount_validator.js' ]
    return common.render.singleform(request, context)


def validate(request):
    ''' Signup form validation handler '''
    msg = ''
    if not('username' in request.GET):
        msg = 'Name not given!'
    elif not('email' in request.GET):
        msg = 'Email not given!'
    name = urllib.unquote(request.GET['username'])
    email = urllib.unquote(request.GET['email'])
    if not msg: msg = __validate_name__(name)
    if not msg: msg = __validate_email__(email)

    status = 'error' if msg else 'success'
    return JsonResponse({"status": status, "message": msg})


def submit(request):
    ''' Signup form submission handler '''
    return HttpResponse('')


def __validate_name__(name):
    ''' Internal validation function for username '''
    lname = len(name)
    if lname < 5:
        return 'User name must be at least 5 characters long'
    if lname > 64:
        return 'User name must not be longer than 64 characters'
    if len(User.objects.filter(username=name)):
        return 'User name already in use'
    return ''

def __validate_email__(email):
    ''' Internal validation function for email '''
    try:
        validate_email(email)
    except ValidationError:
        return 'Invalid email address: '+email
    return ''
