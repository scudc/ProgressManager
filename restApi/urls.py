from django.conf.urls.defaults import patterns, url,include
from djangorestframework.views import ListOrCreateModelView, InstanceModelView
from resources import MyModelResource
from django.contrib import admin
from views import getProgress
from views import getProgressBarData
from django.conf import settings

admin.autodiscover()
my_model_list = ListOrCreateModelView.as_view(resource=MyModelResource)
my_model_instance = InstanceModelView.as_view(resource=MyModelResource)

urlpatterns = patterns('',
    url(r'^restframework', include('djangorestframework.urls', namespace='djangorestframework')),
    url(r'^$', my_model_list, name='model-resource-root'),
    url(r'^(?P<id>[0-9]+)/$', my_model_instance, name='model-resource-instance'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^getProgress/',getProgress),
    url(r'^getProgressBarData$',getProgressBarData),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT,})
)
