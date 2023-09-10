from pathlib import Path
from decouple import config
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False 

ALLOWED_HOSTS = ['*']



INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
]
# apps
INSTALLED_APPS+=[
    'plnnusantarapower.apps.PlnNusantaraPowerConfig',
    'user.apps.UserConfig',
    'intro.apps.IntroConfig',
    'about.apps.AboutConfig',
    'services.apps.ServicesConfig',
    'gallery.apps.GalleryConfig',
    'news.apps.NewsConfig',
    'contact.apps.ContactConfig',
    'topbar.apps.TopbarConfig',
    'lihatberita.apps.LihatberitaConfig'
]

AUTH_USER_MODEL ='user.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    
]


ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'topbar.context_processors.topbar'
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'my_db',
        'USER': 'root',
        'PASSWORD': '1*Mysqladmin',
        'HOST': 'localhost',
        'PORT': '3307',
        "OPTION": {
            "init_command": "SET default_storage_engine=INNODB",
            'charset': 'utf8mb4',
            "autocommit": True,
        }
    },
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/
LANGUAGE_CODE = 'id'

LANGUAGES = [
    ('en', _('English')),
    ('id', _('Indonesian')),
    # Add other languages as needed
]

LOCALE_PATHS = [
    BASE_DIR/'locale'
]

TIME_ZONE = 'Asia/Makassar'

USE_I18N = True
USE_L10N =True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=[BASE_DIR / 'static']
STATIC_ROOT= BASE_DIR / 'staticfiles'

MEDIA_URL=''
MEDIA_ROOT=''
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

JAZZMIN_SETTINGS = {
    "site_title": "Dashboard",
    "site_header": "Admin",
    "site_brand": "Dashboard ",
    "login_logo": None,
    "login_logo_dark": None,
    "site_logo_classes": "img-circle",
    "site_icon": None,
    "welcome_sign": "LOGIN ADMIN",
    "copyright": "PLN NUSANTARA POWER",
    "search_model": ["user.User","intro.Intro",],
    "user_avatar": None,
    "topmenu_links": [
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},
        {"model": "user.User"},
    ],
    "usermenu_links": [
        {"model": "user.User"}
    ],
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "icons": {
        "auth": "fas fa-users-cog",
        "user.User": "fas fa-user",
        
        "auth.Group": "fas fa-users",
        "auth.Permission":"fa fa-key",
        
        "about.About":"fa fa-info-circle",
        
        "contact.Contact":"fa fa-address-book",
        
        "gallery.GalleryImage":"fa fa-image",
        "gallery.Gallery":"fa fa-th",
        
        "intro.Intro":"fa fa-quote-left",
        "intro.BackgroundImageIntro":"fa fa-image",
        
        "news.News":"fa fa-list-alt",
        
        "services.MenuServices":"fa fa-th",
        "services.Services":"fa fa-cogs",
        
        "topbar.TopBar":"fa fa-bars",
        "topbar.Social":"fa fa-comments",
        
        "lihatberita.LihatBerita":"fa fa-list-alt",
        
        "user.User":"fa fa-user",

    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    "related_modal_active": False,
    "custom_css": None,
    "custom_js": None,
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {"auth.user": "horizontal_tabs", "auth.group": "horizontal_tabs"},
    "language_chooser": True,
}
