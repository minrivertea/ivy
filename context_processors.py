from django.conf import settings
from django.utils import translation
from django.contrib.sites.models import get_current_site

from website.models import Page, WebsiteSettings


def common(request):
    context = {}
    context['main_navigation'] = Page.objects.filter(main_navigation=True).order_by('main_navigation_position')
    context['base_template'] = settings.BASE_TEMPLATE
    context['site_name'] = settings.SITE_NAME
    
    
    try:
        context['sitesettings'] = WebsiteSettings.objects.all()[0]
    except:
        context['sitesettings'] = None
    
    return context

 