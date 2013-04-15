from django.contrib import admin
from models import Page, WebsiteSettings

class PageAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title')


admin.site.register(Page, PageAdmin)
admin.site.register(WebsiteSettings)
