from django.shortcuts import render
import common.render
from common.settings import get_page_config

# Site home page
def index(request):
    context = get_page_config(title='Home')
    return render(request, 'public/index.html', context)


# New user sign-up
def signup(request):
    context = get_page_config(title='New User Sign Up')
    context['form'] = [
        {'label': 'User Name', 'name': 'username'},
        {'label': 'Email Address', 'name': 'email'},
        {'label': 'Password', 'type': 'password', 'name':'password'},
        {'label': 'Re-enter Password', 'type': 'password', 'id':'repass'}
    ]
    context['validators'] = [ 'public/newaccount_validator.js' ]
    return common.render.singleform(request, context)
