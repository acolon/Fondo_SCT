from .base import *

ALLOWED_HOSTS.append('acolon.pythonanywhere.com')

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'sct_db',
		'USER': 'acolon',
		'PASSWORD': get_env_variable('SCT_DB_PWD'),
		'HOST': 'acolon.mysql.pythonanywhere-services.com',
		'PORT': '3306',
	}
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
