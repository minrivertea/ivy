from django.db import models
from django.core.urlresolvers import reverse

from ckeditor.fields import RichTextField



class Page(models.Model):
    title = models.CharField(max_length=200)
    long_title = models.CharField(max_length=200, blank=True, null=True, help_text="Chinese and English allowed eg. ABOUT US ")
    slug = models.SlugField(max_length=80)
    content = RichTextField(blank=True, null=True)
    main_navigation = models.BooleanField(default=False)
    main_navigation_position = models.IntegerField(blank=True, null=True)
    promo_image = models.ImageField(blank=True, null=True, upload_to='promo-images')
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('page', args=[self.slug])


class WebsiteSettings(models.Model):
    website_name = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    telephone = models.CharField(max_length=200, blank=True, null=True)
    weibo_account = models.CharField(max_length=100, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        return self.id
    
    
