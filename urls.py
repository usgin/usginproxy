from django.conf.urls.defaults import patterns

urlpatterns = patterns('',
    (r'.+', 'usginproxy.views.proxy'),
)