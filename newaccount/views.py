from django.shortcuts import render
from django.http import JsonResponse
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
    return JsonResponse({"status": "error", "message": "Test Case"})


def submit(request):
    ''' Signup form submission handler '''
    return HttpResponse('')
