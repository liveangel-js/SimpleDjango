# -*- coding: utf-8 -*-
"""
Django settings for SimpleDjango project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^@!45dr4n7kz&o(6lt$3i9(v@40mj#=e!7sy%_4#f7*_=4t0n^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

#memcache
#CACHE_BACKEND = 'memcache://127.0.0.1:12111'

# database cache; use commond manage.py createcachetable mycachename
CACHE_BACKEND = 'db://mycache'

# file cache
CACHE_BACKEND = 'file///usr/local/tmp'

# Application definition
#用户注册系统
INSTALLED_APPS = (
    'registration',
    'registration_email',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'book',
    'JsonPractice',
    'diyfield',
    'simpleform',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'book.myMiddleware.MyMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'SimpleDjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'SimpleDjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
#python 国际化
"""
生成需要翻译的文件
django-admin.py makemessages -l zh-cn
django-admin.py makemessages -l zh-tw
手工翻译 locale 中的文本后，我们需要编译一下，这样翻译才会生效
django-admin.py compilemessages
"""
LANGUAGES = (
    ('en', ('English')),
    ('zh-cn', ('中文简体')),
    ('zh-tw', ('中文繁體')),
)

#翻译文件所在目录，需要手工创建
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
TEMPLATE_CONTEXT_PROCESSORS = ("django.core.context_processors.i18n",)




# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')

# 其它 存放静态文件的文件夹，里面不能包含 STATIC_ROOT
# jquery.js 放在 common_static/js/ 下，这样就可以 在 /static/js/jquery.js 中访问到它！
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "common_static"),

)

# 这个是默认设置，默认会找 STATICFILES_DIRS 中所有文件夹和各app下的 static 文件夹
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder"
)


#用户注册的系统

ACCOUNT_ACTIVATION_DAYS = 7 # 激活期限

AUTHENTICATION_BACKENDS = (
    'registration_email.auth.EmailBackend',
)
# NOTICE:not work `lambda request, user: '/'`
LOGIN_REDIRECT_URL = '/'#登陆成功后跳转的网址

# NOTICE:not work only '/accounts/activate/complete/'
REGISTRATION_EMAIL_ACTIVATE_SUCCESS_URL = lambda request, user: '/accounts/activate/complete/'
REGISTRATION_EMAIL_REGISTER_SUCCESS_URL = lambda request, user: '/accounts/register/complete/'
