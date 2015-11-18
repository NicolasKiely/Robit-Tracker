from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/', views.login_form, name='login-form'),
    url(r'^login-success/', views.login_success, name='login-success'),
    url(r'^login-failed/', views.login_failed, name='login-failed'),
    url(r'^login-inactive/', views.login_inactive, name='login-inactive'),
    url(r'^auth/', views.login_auth, name='login-auth'),
    url(r'^logout/', views.logout_auth, name='logout')
]
