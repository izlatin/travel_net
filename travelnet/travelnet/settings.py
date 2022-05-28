import environ

from os.path import join
from pathlib import Path
from django.urls import reverse_lazy

env = environ.Env()
environ.Env.read_env(env_file='example.env')

BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(join(BASE_DIR.parent, '.env'))

ALLOWED_HOSTS = ["127.0.0.1"]
SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
MAPBOX_TOKEN = env('MAPBOX_TOKEN')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'users.apps.UsersConfig',
    'homepage.apps.HomepageConfig',
    'publications.apps.PublicationsConfig',
    'rating.apps.RatingConfig',
    'about.apps.AboutConfig',
    'core.apps.CoreConfig',

    'map',

    'sorl.thumbnail',
    'django_cleanup.apps.CleanupConfig',
    'debug_toolbar',
    'rest_framework',
    'rest_framework.authtoken',

    'mapbox_location_field',
    "bootstrap4",
]

AUTH_USER_MODEL = 'users.CustomUser'

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'travelnet.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(join(BASE_DIR, 'templates'))],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'travelnet.wsgi.application'

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = join(BASE_DIR, 'sent_emails')
# Internationalization

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_ROOT = 'static'
STATICFILES_DIRS = [
    BASE_DIR / 'static_dev'
]

# Default primary key field type
LOGIN_URL = reverse_lazy('users:login')
LOGIN_REDIRECT_URL = reverse_lazy('users:user_detail', kwargs={'user_id': 0})
LOGOUT_REDIRECT_URL = reverse_lazy('users:login')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

INTERNAL_IPS = [
    "127.0.0.1",
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
}

MAPBOX_KEY = MAPBOX_TOKEN

if DEBUG:
    # нужно для debug_toolbar
    import mimetypes

    mimetypes.add_type("application/javascript", ".js", True)
