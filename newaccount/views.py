from django.http import JsonResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.shortcuts import render
import re
import urllib
import common.render
from common.settings import get_page_config

# Form fiels for creating new account
new_account_form_fields = [
    {'label': 'User Name', 'name': 'username'},
    {'label': 'Email Address', 'name': 'email'},
    {'label': 'Password', 'type': 'password', 'name':'password'},
    {'label': 'Re-enter Password', 'type': 'password', 'id':'repass'}
]

# Validator js file for creating new account
new_account_validators = [ 'signup/newaccount_validator.js' ]

# Form action
new_account_action = '/signup/submit/'

# Username regular expression
username_expression = re.compile('^[0-9A-Za-z_]+$')


def form(request):
    ''' The signup form webpage '''
    context = get_page_config(request, title='New User Sign Up')
    context['form'] = new_account_form_fields
    context['action'] = new_account_action
    context['validators'] = new_account_validators
    return common.render.singleform(request, context)


def validate(request):
    ''' Signup form validation handler '''
    msg = __validate_name__(request.GET)
    if not msg: msg = __validate_email__(request.GET)

    status = 'error' if msg else 'success'
    return JsonResponse({"status": status, "message": msg})


def submit(request):
    ''' Signup form submission handler '''
    context = get_page_config(request, title='New User Sign Up')
    req = request.POST
    msg = __validate_name__(req)
    if not msg: msg = __validate_email__(req)
    newuser = User.objects.create_user(
        req['username'],
        req['email'],
        req['password']
    )
    user = authenticate(username=req['username'], password=req['password'])
    login(request, user)
    context['user'] = user
    if msg:
        # Return back to account signup page with error
        context['form'] = new_account_form_fields
        context['action'] = new_account_action
        context['validators'] = new_account_validators
        context['error'] = msg
        return common.render.singleform(request, context)
    return render(request, 'signup/finished.html', context)


def __validate_name__(hpars):
    ''' Internal validation function for username '''
    if not('username' in hpars):
        return 'Name not given'
    name = urllib.unquote(hpars['username'])
    lname = len(name)
    if lname < 5:
        return 'User name must be at least 5 characters long'
    if lname > 64:
        return 'User name must not be longer than 64 characters'
    if not username_expression.search(name):
        return 'User name must contain only letters, numbers, or underscore'
    if len(User.objects.filter(username=name)):
        return 'User name already in use'
    return ''

def __validate_email__(hpars):
    ''' Internal validation function for email '''
    if not('email' in hpars):
        return 'Email address not given'
    email = urllib.unquote(hpars['email'])
    try:
        validate_email(email)
    except ValidationError:
        return 'Invalid email address: '+email
    return ''
