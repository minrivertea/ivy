# Django settings for IVY project.

import os
PROJECT_PATH = os.path.normpath(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


DEBUG = False
TEMPLATE_DEBUG = DEBUG
THUMBNAIL_DEBUG = False
GA_IS_ON = True
ADMINS = (('Chris West', 'chris@minrivertea.com'),)
MANAGERS = ADMINS
TIME_ZONE = 'Asia/Shanghai'
SITE_ID = 1
SECRET_KEY = ''



# STATIC / MEDIA FILES
# ----------------------------------------------------------
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')
MEDIA_URL = '/media/'

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)



TEMPLATE_LOADERS = (
#    'ab.loaders.load_template_source',
#    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.media',
    'django.core.context_processors.debug',
    'django.core.context_processors.request',
    'context_processors.common',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware', 
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
#    'ab.middleware.ABMiddleware',
#    'django_mobile.middleware.MobileDetectionMiddleware',
#    'django_mobile.middleware.SetFlavourMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
#    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
)


ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, "templates/"), 
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.sitemaps',
    'django.contrib.comments',
    'django.contrib.redirects',
    'django.contrib.staticfiles',
    'website',
    'sorl.thumbnail',
    'ckeditor',
)


SESSION_EXPIRE_AT_BROWSER_CLOSE = True

BASE_TEMPLATE = "base.html"
SITE_NAME = 'ivy-ad.com'




# CKEDITOR SETTINGS
# -----------------------------------------------
CKEDITOR_UPLOAD_PATH = os.path.join(MEDIA_ROOT, 'ckuploads')
CKEDITOR_UPLOAD_PREFIX = "/media/ckuploads/"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            [      'Undo', 'Redo',
              '-', 'Bold', 'Italic', 'Underline', 'BulletedList', 'NumberedList', 'Image',
              '-', 'Link', 'Unlink', 'Anchor',
              '-', 'Format',
              '-', 'PasteFromWord',
              '-', 'Maximize', 'Source', 
            ],
        ],
        'width': 840,
        'height': 300,
        'toolbarCanCollapse': False,
    }
}

# LANGUAGE SETTINGS
# ------------------------------------------
USE_I18N = True
gettext = lambda s: s
LANGUAGES = (
    ('zh', gettext('Chinese')),
)


LANGUAGE_CODE = 'zh'

LOG_FILENAME = "/var/log/django/ivy.log"

try:
    from local_settings import *
except ImportError:
    pass
