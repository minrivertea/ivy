from django.conf.urls.defaults import *
from django.conf import settings
import django.views.static
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from django.views.generic.simple import direct_to_template
from django.utils.translation import ugettext_lazy as _
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



# admin urls
from django.contrib import admin
admin.autodiscover()

# main URL patterns
urlpatterns = patterns('',
    (r'^', include('website.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^ckeditor/', include('ckeditor.urls')),
    
    # SITEMAPS, FEEDS AND STATICS
    (r'^robots\.txt$', direct_to_template, {'template': 'robots.txt', 'mimetype': 'text/plain'}),
    (r'^humans\.txt$', direct_to_template, {'template': 'humans.txt', 'mimetype': 'text/plain'}),
    


    
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

