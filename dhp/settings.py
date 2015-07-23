import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PROJECT_NAME = 'DHP'
PROJECT_VARIABLE_PATTERN = '_'.join((PROJECT_NAME, '{}'))

SECRET_KEY = os.getenv(PROJECT_VARIABLE_PATTERN.format('SECRET_KEY'))

DEBUG = False # os.getenv(PROJECT_VARIABLE_PATTERN.format('DEBUG'), False) == 'TRUE'
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Dane Hillard', 'github@danehillard.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv(PROJECT_VARIABLE_PATTERN.format('DATABASE_NAME')),
        'USER': os.getenv(PROJECT_VARIABLE_PATTERN.format('DATABASE_USER')),
        'PASSWORD': os.getenv(PROJECT_VARIABLE_PATTERN.format('DATABASE_PASSWORD')),
        'HOST': os.getenv(PROJECT_VARIABLE_PATTERN.format('DATABASE_HOST'), 'localhost'),
        'PORT': os.getenv(PROJECT_VARIABLE_PATTERN.format('DATABASE_PORT'), 3306),
    }
}

SOCIAL_MEDIA = {
    'facebook': 'danehillard',
    'instagram': 'danehillard',
    'pinterest': 'danehillard',
    'twitter': 'danehillard',
    'youtube': 'danehillard',
    'linkedin': 'danehillard',
}

LOGIN_REDIRECT_URL = '/'
ALLOWED_HOSTS = os.getenv(PROJECT_VARIABLE_PATTERN.format('ALLOWED_HOSTS'), '*').split(',')

TIME_ZONE = 'America/Detroit'
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
USE_TZ = False

STATIC_ROOT = os.path.join(BASE_DIR, os.getenv(PROJECT_VARIABLE_PATTERN.format('STATIC_ROOT'), 'static'))
STATIC_URL = os.getenv(PROJECT_VARIABLE_PATTERN.format('STATIC_URL'), '/static/')
MEDIA_ROOT = os.path.join(BASE_DIR, os.getenv(PROJECT_VARIABLE_PATTERN.format('MEDIA_ROOT'), 'media'))
MEDIA_URL = os.getenv(PROJECT_VARIABLE_PATTERN.format('MEDIA_URL'), '/media/')

IMAGE_UPLOAD_PATH = os.path.join('images', 'uncropped')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
    os.path.join(BASE_DIR, 'bower_components'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'context_processors.template_visible_settings',
            ],
        },
    },
]

TEMPLATE_VISIBLE_SETTINGS = (
    'SOCIAL_MEDIA',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'dhp.urls'
WSGI_APPLICATION = 'dhp.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.admin',
    'compressor',
    'blog',
    'photography',
    'home',
    'about',
    'contact',
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache' if not DEBUG else 'django.core.cache.backends.dummy.DummyCache',
        'LOCATION': os.getenv(PROJECT_VARIABLE_PATTERN.format('MEMCACHED_ENDPOINT'), '127.0.0.1:11211'),
    }
}

CACHE_MIDDLEWARE_SECONDS = 3600
CACHE_MIDDLEWARE_KEY_PREFIX = PROJECT_NAME.lower()

ADMIN_URL = os.getenv(PROJECT_VARIABLE_PATTERN.format('ADMIN_URL'), r'^admin/')

COMPRESS_CSS_FILTERS = (
    'compressor.filters.cssmin.CSSMinFilter',
)

COMPRESS_PRECOMPILERS = (
    ('text/x-sass', 'sass {infile} {outfile}'),
)

COMPRESS_OFFLINE = True
COMPRESS_OUTPUT_DIR = ''

AWS_ACCESS_KEY_ID = os.getenv(PROJECT_VARIABLE_PATTERN.format('AWS_ACCESS_KEY_ID'))
AWS_SECRET_ACCESS_KEY = os.getenv(PROJECT_VARIABLE_PATTERN.format('AWS_SECRET_ACCESS_KEY'))
