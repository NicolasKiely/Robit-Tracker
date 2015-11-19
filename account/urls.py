from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^settings/$', views.settings, name='settings'),
    url(r'^(?P<user_id>[0-9]+)/$', views.profile, name='profile')
]
