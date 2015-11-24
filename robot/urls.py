from django.conf.urls import url
from . import views

urlpatterns = [
   url('^manage/$', views.manage_new, name='new'),
   url('^manage/(?P<bot_id>[0-9]+)/$', views.manage, name='manage')
]
