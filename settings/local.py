# settings/local.py

from .base import *

DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'sct_db',
		'USER': 'sct_user',
		'PASSWORD': get_env_variable('SCT_DB_PWD'),
		'HOST': 'localhost',
		'PORT': '3306',
	}
}

STATICFILES_DIRS = (
	os.path.join(BASE_DIR, 'static'),
)
