import os


# Django settings for project.
DEBUG = False
TEMPLATE_DEBUG = False

ADMINS = (
    ('Your Name', 'your_email@domain.com'),
)
MANAGERS = ADMINS

SERVER_EMAIL = 'angular@localhost.com'

APPLICATION_DIR = os.path.dirname(globals()['__file__'])

DATABASES = {
    'default': {
        # 'postgresql_psycopg2','postgresql','sqlite3','oracle', 'django.db.backends.mysql'
        'ENGINE': 'django.db.backends.sqlite3',
        # Database name or path to database file if using sqlite3.
        'NAME': APPLICATION_DIR + '/database/angular.db',
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Not used with sqlite3.
        'PORT': '',                      # Not used with sqlite3.
        # 'OPTIONS': {
        #    'init_command': 'SET storage_engine=INNODB',
        # }
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = False

DATETIME_FORMAT = 'Y-m-d H:i:s'

DATE_FORMAT = 'Y-m-d'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'usermedia')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/mediafiles/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    # os.path.join(APPLICATION_DIR, "resources"),
    ("angular", os.path.join(APPLICATION_DIR, "resources")),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
    #'dajaxice.finders.DajaxiceFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ujau$^uei_ak=@-v8va(&@q_sc0^1nn*qpwyc-776n&qoam@+v'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    #'raven.contrib.django.middleware.SentryResponseErrorIdMiddleware',
    #'raven.contrib.django.middleware.Sentry404CatchMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'pagination.middleware.PaginationMiddleware',
    #'linaro_django_pagination.middleware.PaginationMiddleware',
    #'common.filter_persist_middleware.FilterPersistMiddleware',
    #'audiofield.middleware.threadlocals.ThreadLocals',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.csrf",
    "django.contrib.messages.context_processors.messages",
    #"context_processors.newfies_version",
    #needed by Sentry
    #"django.core.context_processors.request",
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or
    # "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(APPLICATION_DIR, 'templates'),
)

INTERNAL_IPS = ('127.0.0.1',)

#ALLOWED_HOSTS
ALLOWED_HOSTS = ['127.0.0.1']

#DAJAXICE_MEDIA_PREFIX = "dajaxice"
#DAJAXICE_MEDIA_PREFIX = "dajax"  # http://domain.com/dajax/
#DAJAXICE_CACHE_CONTROL = 10 * 24 * 60 * 60

INSTALLED_APPS = (
    #admin tool apps
    #'admin_tools',
    #'admin_tools.theming',
    #'admin_tools.menu',
    #'admin_tools.dashboard',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    'django.contrib.markup',

)



#No of records per page
#=======================
PAGE_SIZE = 10

# AUTH MODULE SETTINGS
AUTH_PROFILE_MODULE = 'user_profile.UserProfile'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/pleaselog/'


#REDIS-CACHE
#===========
CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': '127.0.0.1:6379',
        #'OPTIONS': {
        #    'DB': 1,
        #    'PASSWORD': 'yadayada',
        #    'PARSER_CLASS': 'redis.connection.HiredisParser'
        #},
    },
}


#LANGUAGES
#===========
gettext = lambda s: s
LANGUAGES = (
    ('en', gettext('English')),
    ('fr', gettext('French')),
    ('es', gettext('Spanish')),
    ('pt', gettext('Portuguese')),
    ('zh', gettext('Chinese')),
    ('tr', gettext('Turkish')),
    ('ja', gettext('Japanese')),
)

LOCALE_PATHS = (
    os.path.join(APPLICATION_DIR, 'locale'),
)

LANGUAGE_COOKIE_NAME = 'angular_language'

ADMIN_MEDIA_PREFIX = '/static/admin/'

#EMAIL BACKEND
#=============
# Use only in Debug mode. Not in production
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

#TASTYPIE API
#============
API_ALLOWED_IP = ['127.0.0.1', 'localhost']


#IMPORT LOCAL SETTINGS
#=====================
try:
    from settings_local import *
except ImportError:
    pass
