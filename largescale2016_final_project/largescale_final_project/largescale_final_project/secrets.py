# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5#=fje(zd&2%@-x*3s)5v5k6@ipi27_w7e76&y&mdpu76nm2i+'

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'renting_app',
    'USER' : 'appserver',
    'PASSWORD': 'foobarzoot',
    'HOST': '127.0.0.1',
    'PORT': '3306',
  },
}



