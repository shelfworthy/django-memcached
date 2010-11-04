from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'django_memcached.views.server_list', name="memcached_servers"),
    url(r'^(\d+)/$', 'django_memcached.views.server_status'),
)
