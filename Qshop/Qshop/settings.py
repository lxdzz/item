"""
Django settings for Qshop project.

Generated by 'django-admin startproject' using Django 2.1.8.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ic%vpos-c_itv)#a9rf5be8%eto5j0%w#ho2xhjmdszr(&)#3x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Buyer',
    'Seller',
    'djcelery',
]

MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'Qshop.middleware.MiddleWareTest'
    'django.middleware.cache.FetchFromCacheMiddleware'
]

ROOT_URLCONF = 'Qshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True, #代表自动检索app下面的templates目录下的html文件
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

WSGI_APPLICATION = 'Qshop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=(
    os.path.join(BASE_DIR,'static'),
)

# STATIC_ROOT=os.path.join(BASE_DIR,'static') #静态文件的根目录,和STATICFILES_DIRS,MEDIA_URL,MEDIA_ROOT有冲突

MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'static')







alipay_public_key_string="""-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzWvn3wyy0o0QzsCHou2OtPpLzut/fkCZL7PNKte2hAVNtOPF5dyGgbMJPqxNtOnEWx+b4plDxadw1SdlKbjj2i4VuPwBIragp/p6yU9d8JKC+jJ3el1GBgQCiLYjMVTBD22Dvh9/O4rYkRv+sxN1i/v3bFXtRpqRBX9pnDsiDIo/GF5xdHSWAGX1jjdeswGQcRcCWtuKHwImPqOx8CZF7e8tlHPqp5rA8JfBIRvH28L3LwId/Fw5LykrUlCJ7TPYT7EuAYx0nVpPZ5c7u5cHOUqEq0hJEDq5WyizTba3gg7hEvC5GuGyXBHv5X4+75Kfnd6EzvMX48tofDzv/kvqpwIDAQAB
-----END PUBLIC KEY-----"""

alipay_private_key_string="""-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAzWvn3wyy0o0QzsCHou2OtPpLzut/fkCZL7PNKte2hAVNtOPF5dyGgbMJPqxNtOnEWx+b4plDxadw1SdlKbjj2i4VuPwBIragp/p6yU9d8JKC+jJ3el1GBgQCiLYjMVTBD22Dvh9/O4rYkRv+sxN1i/v3bFXtRpqRBX9pnDsiDIo/GF5xdHSWAGX1jjdeswGQcRcCWtuKHwImPqOx8CZF7e8tlHPqp5rA8JfBIRvH28L3LwId/Fw5LykrUlCJ7TPYT7EuAYx0nVpPZ5c7u5cHOUqEq0hJEDq5WyizTba3gg7hEvC5GuGyXBHv5X4+75Kfnd6EzvMX48tofDzv/kvqpwIDAQABAoIBAQDMgzSLFVpnUvg7zuR66iWcumCE9mKs8GVSX6DQmYhlcd5GTEp3KZFkSTnYArUue1n5GsQY2lvlyWkFXb5SxndafW01CPecdtQFyNM73t94pnTt4RagZYJUdOOM9kCdWXMICBEUVMlYH0izV3rBEIuDvWw8mGOtWi8tmQcs+pZQgfv5MIAhyeDt6cRhT2XBxxwbasvvOPUQuTfiuKt5+m4tLqDMbDGnwNe0nIKM7Z2y+lqSIhvttZMoC9ucfMyX2RkzacvXSqdcxcYMhjEQm+9Zb02tORb0Pf3SQXIW1mgWW/ZM0WAwJRTjUfno0QKgYAMaTgx1R/UX9Ss6VR4nFEaRAoGBAPtitqOr/cM7zWqfm+XdkH3G/N6cLE6c3/7neZ8SOk7z7yNgRPZOOoAHOY8g/ZFyf4NqR4Yk6DPoIl3lCJK6smBcT4AHvjJYAcLYs0sZqZDSbxMdz7004fyBMtqXLaTHhjTZGrg9B/XLRMm5Wt0jUc5WZ4nJ/ZkIf/GL+keTXasJAoGBANExM82B3RyGEUHqGZspBI5GHl0pe+hHfqwtLyBfhVz+jmDpBBrl8nJ94qRbx4XrbVeCVvdPaO/mRY+eKLvb3vl2Ezkm1Zjmt5YGR3ppqvNbjQbqj98C425cGn++0OzrFW54VuNcBOZCd9qnF0Os3L3TL4+hZa8h4OJvHIPfemQvAoGAeApwSoHzwInLEpI7AK4ntFgUIj0TT0rMD837HsG2hEMpu4vaAn/ioYZRrw5C53R0fY1/sAfptfewiYO371EloqwR7oJECYhK9v9Bxqfvd8906P0AWUpqa4hKf2VXj2sTpCLUBoxmQ7IYG/fd8uFNzCkocfy5k50ic3azQgCV5vkCgYA8wynk23+6NUb1+mWNqBBmsv9G2DHhekLVCBrUMGqwZFA+3fAPUBNoJiCa1P3TbFrKPFW+aBZ2+E/kM3BpgKf3ldBnnVwVmY5hyVkhuWeqYEFKbP91K4WcHKylxmsxJeeHuvSh/ax+pXfizv327lL/4EPEWIEMqa6ElvmVZGhMiQKBgC4q0PvH22mbWRYsAyIrcKabWrG4P/hW0m6q+TyUQV2KJ+G8x+sRbFTg/Ne8nJbWny38lhkrGBnNNJnoAwqYwDVSLZtRZIOMEGW5PLFaNnnrBWDGnmApMwa0Yb7ISHlrkGBvZTD5FV51AH/inV/1N/t+Gla9d5nkalvQMgJWMhHn
-----END RSA PRIVATE KEY-----"""

DING_URL="https://oapi.dingtalk.com/robot/send?access_token=d54a982dc3e7f3b80503b2969710e867c365dda2add289eb2be2f44f824f2092"

import djcelery #导入django-celery模块
djcelery.setup_loader() #进行模块加载
BROKER_URL='redis://127.0.0.1:6379/1' #任务容器地址,redis数据库地址
CELERY_IMPORTS=('CeleryTask.tasks') #具体的任务文件
CELERY_TIMEZONE='Asia/Shanghai' #celery时区
CELERYBEAT_SCHEDULER='djcelery.schedulers.DatabaseScheduler' #celery处理器,固定

from celery.schedules import crontab
from celery.schedules import timedelta

# CELERYBEAT_SCHEDULE={
#     u'测试任务1':{
#         "task":"CeleryTask.tasks.sendDing", #任务函数
#         "schedule":timedelta(seconds=1) #执行时间
#     }
# }

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION':[
            "127.0.0.1:11211" #本地memcached的地址端口
        ]
    }
}
CACHE_MIDDLEWARE_KEY_PREFIX = ''
CACHE_MIDDLEWARE_SECONDS = 600
CACHE_MIDDLEWARE_ALIAS = 'default'

# ERROR_PATH=os.path.join(BASE_DIR,"error.log")