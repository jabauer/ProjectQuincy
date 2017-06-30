# This file is exec'd from settings.py, so it has access to and can
# modify all the variables in settings.py.

# If this file is changed in development, the development server will
# have to be manually restarted because changes will not be noticed
# immediately.

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # Django needs to make databases in the test mysql server
        'NAME': 'travispq',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'OPTIONS': {
            # In each case, we want strict mode on to catch truncation issues
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            # Load the socket info from .my.cnf in the travis user
            'read_default_file': '~travis/.my.cnf'
        },
        'PORT': '',
        'TEST': {
                # We also want the test databse to for utf8 and the general
                # collation to keep case sensitive unicode searches working
                # as we would expect on production
                'CHARSET': 'utf8',
                'COLLATION': 'utf8_general_ci',
                'OPTIONS': {
                    'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
                },
            },
    },
}

# secret key added as a travis build step

STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = [
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/home/vagrant/ProjectQuincy/static',
]

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ProjectQuincy.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'ProjectQuincy.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS' : [
            os.path.join(BASE_DIR, "templates")
        ],
        'OPTIONS': {
            'context_processors': [
                "django.contrib.auth.context_processors.auth",
            ],
        }
    }
]

TIME_ZONE = 'America/New_York'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    #this next app provides basic searching of multiple fields in a table
    'simplesearch',
    #these apps are part of the main Project Quincy code base
    'activities',
    'citations',
    'communication',
    'people',
    'places',
    'search',
    'static',
    'templates'
)