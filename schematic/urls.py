from django.conf.urls import url
from . import views

urlpatterns = [
    url('^editor/$', views.editor_new, name='new'),
    url('^editor/(?P<schema_id>[0-9]+)/$', views.editor, name='editor')
]
