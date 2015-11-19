from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from common.settings import get_page_config


login_redirect = '/'

@login_required(login_url=login_redirect)
def dashboard(request):
    ''' Shows user's dashboard '''
    context = get_page_config(request, title='Dashboard')
    return render(request, 'account/dashboard.html', context)


@login_required(login_url=login_redirect)
def settings(request):
    ''' Shows user account settings '''
    context = get_page_config(request, title='Settings')
    return render(request, 'account/settings.html', context)


@login_required(login_url=login_redirect)
def profile(request):
    ''' Shows user's public profile '''
    context = get_page_config(request, title='Profile')
    return render(request, 'account/profile.html', context)
