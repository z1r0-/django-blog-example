from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^single/(?P<post_id>\d+)/$', views.single, name='single'),
]