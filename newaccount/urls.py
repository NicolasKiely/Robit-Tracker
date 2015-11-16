from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.form, name='signup-form'),
    url(r'^validate/$', views.validate, name='signup-validate'),
    url(r'^submit/$', views.submit, name='signup-submit')
]
