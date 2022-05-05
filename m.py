import django
from django.conf import settings


INSTALLED_APPS = [
    'dataset',
]

DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.sqlite3',
        'NAME' : 'db.sqlite3',
    }
}

settings.configure(
    INSTALLED_APPS = INSTALLED_APPS,
    DATABASES = DATABASES,
)

django.setup()
