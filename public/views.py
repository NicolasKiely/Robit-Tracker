from django.shortcuts import render
import common.render
from common.settings import get_page_config

# Site home page
def index(request):
    context = get_page_config(request, title='Home')
    return render(request, 'public/index.html', context)
