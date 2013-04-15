from django.db import models
from django.core.urlresolvers import reverse



class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=80)
    content = models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('page', args=[self.slug])

