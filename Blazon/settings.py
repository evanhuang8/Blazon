"""
Django settings for Blazon project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cwkhep$k0mgw+$5i^hio6jmut%f!(2yox=8*rr+4@)5okv@jef'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'sponsorship',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Blazon.urls'

WSGI_APPLICATION = 'Blazon.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'Blazon', 
        'USER': 'root', 
        'PASSWORD': 'L33che$', 
        'HOST': '', 
        'PORT': '', 
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

# Media files

MEDIA_ROOT = os.path.join(BASE_DIR, 'sponsorship/static/media/')

# Blazon

AUTH_USER_MODEL = 'sponsorship.User'
AUTHENTICATION_BACKENDS = ('sponsorship.models.UserAuthBackend',)
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)
LOGIN_URL = '/login/'

MASTERCARD_PUBLIC = os.environ.get('MASTERCARD_PUBLIC', 'sbpb_NjIxZjhlYTktNTQxMS00NzI1LWFhMGQtOGY1YjJiMDZlMGFh')
MASTERCARD_PRIVATE = os.environ.get('MASTERCARD_PRIVATE', '/6XxzS5TE28m7PD4E2Ykk4ImRgqstQzJhwfQ+/sxtOp5YFFQL0ODSXAOkNtXTToq')
MANDRILL_API_KEY = os.environ.get('MANDRILL_API_KEY', 'EJmj_TdbdCy6Xda_9hREKA')
MANDRILL_FROM_EMAIL = os.environ.get('MANDRILL_FROM_EMAIL', 'team@carbon.com')
MANDRILL_FROM_NAME = os.environ.get('MANDRILL_FROM_EMAIL', 'Carbon')

# Django REST framework

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication', 
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated', 
    ),
}
