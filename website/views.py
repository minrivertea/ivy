from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from models import Page

#render shortcut
def render(request, template, context_dict=None, **kwargs):
    
    return render_to_response(
        template, context_dict or {}, context_instance=RequestContext(request),
                              **kwargs
    )


def index(request):
    return render(request, "website/home.html", locals())
    
      
def page(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request, "page.html", locals())
    