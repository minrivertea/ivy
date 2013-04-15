from django.db import models
from django.core.urlresolvers import reverse

from ckeditor.fields import RichTextField



class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=80)
    content = RichTextField(blank=True, null=True)
    main_navigation = models.BooleanField(default=False)
    main_navigation_position = models.IntegerField(blank=True, null=True)
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('page', args=[self.slug])

