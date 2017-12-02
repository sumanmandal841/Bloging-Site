from django.apps import AppConfig


class DjangoSocialAppConfig(AppConfig):
    name = 'django_social_app'
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'social_django',  # <--

    'mysite.core',
]