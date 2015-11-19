''' Render preprocessor for common pages '''
from django.shortcuts import render

def singleform(request, context):
    ''' Sets defaults for individual form inputs '''
    context.setdefault('form', [])
    context.setdefault('error', '')
    context.setdefault('action', '')
    context.setdefault('validators', [])
    if ('page' in context) and ('title' in context['page']):
        context.setdefault('title', context['page']['title'])
    for form in context['form']:
        form.setdefault('label', '')
        form.setdefault('type', 'text')
        if 'name' in form:
            form.setdefault('id', form['name'])
        else:
            form.setdefault('id', form['label'].replace(' ', '-').lower())

    return render(request, 'common/singleform.html', context)
