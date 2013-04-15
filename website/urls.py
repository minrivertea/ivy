from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
import views


urlpatterns = patterns('',

    url(r'^$', views.index, name="home"),
    url(r'^(?P<slug>[\w-]+)/$', views.page, name="page"),
    #url(r'^photo/(?P<slug>[\w-]+)/$', views.photo, name="photo"),
    #url(r'^cv/$', direct_to_template, {'template': 'cv.html'}, name="cv"),
)
