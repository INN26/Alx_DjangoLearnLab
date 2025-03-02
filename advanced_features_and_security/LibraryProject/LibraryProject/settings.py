"""
Django settings for LibraryProject project.

Generated by 'django-admin startproject' using Django 4.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i2&=dv_*eo!dya403!l5*gf7i2xk#fi)f$%5=bc**x0a8=mfk_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'relationship_app',
    'bookshelf',
    'csp',
]
AUTH_USER_MODEL = "bookshelf.CustomUser"

LOGIN_REDIRECT_URL = "/accounts/profile"
LOGOUT_REDIRECT_URL = "/accounts/profile"


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',
]
#CSP blocks unauthorized scripts from running.
CSP_DEFAULT_SRC = ["'self'"]  # Only allows content from the same origin
CSP_SCRIPT_SRC = ["'self'", "https://trusted-cdn.com"]  # Allow scripts from specific sources
CSP_STYLE_SRC = ["'self'", "'unsafe-inline'"]  # Allow styles from local sources
ROOT_URLCONF = 'LibraryProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,  # Ensures Django looks for templates in app directories
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

WSGI_APPLICATION = 'LibraryProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

#Scurity Configurations
DEBUG = False
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Ensure Django properly detects HTTPS behind a proxy (e.g., Nginx, AWS ELB)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Enforce HTTPS 
SECURE_SSL_REDIRECT = True # Redirect all HTTP traffic to HTTPS

# Enforce HTTPS settings prevent unauthorized access and session hijacking.
SECURE_HSTS_SECONDS = 31536000  # instruct browsers to only access the site via HTTPS for the specified time. (1 year)
SECURE_HSTS_PRELOAD = True # Allows preloading HSTS into browsers
SECURE_HSTS_INCLUDE_SUBDOMAINS = True # # Applies HSTS to all subdomains

#secure cookies
CSRF_COOKIE_SECURE = True #  to ensure CSRF cookies are only transmitted over HTTPS.
SESSION_COOKIE_SECURE = True #Ensures session cookies are only sent over HTTPS

#Secure HTTP Headers prevent XSS attacking
SECURE_BROWSER_XSS_FILTER = True  # Enable the browser’s XSS filtering and help prevent cross-site scripting attacks.
X_FRAME_OPTIONS = "DENY"  # prevent your site from being framed and protect against clickjacking.
SECURE_CONTENT_TYPE_NOSNIFF = True  # prevent browsers from MIME-sniffing a response away from the declared content-type.

 # Ensure secure referrer policy
SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"

# Use ALLOWED_HOSTS and Secure CSRF_TRUSTED_ORIGINS
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com', '127.0.0.1']  # Specify trusted domains

CSRF_TRUSTED_ORIGINS = ['https://yourdomain.com'] # Allows secure form submissions




