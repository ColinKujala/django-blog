import os

import dj_database_url

from .settings import *


DATABASES = {
    "default": dj_database_url.config(
        default="sqlite:///" + os.path.join(BASE_DIR, "db.sqlite3")
    )
}

DEBUG = False  # Because debug off, we need to set ALLOWED_HOSTS
TEMPLATE_DEBUG = False
STATIC_ROOT = os.path.join(BASE_DIR, "static")
SECRET_KEY = os.environ.get("SECRET_KEY")
ALLOWED_HOSTS = ["*"]  # Heroku will auto check requests for correct hostname

# Whitenoise middleware helps serve up site through Heroku
MIDDLEWARE = ("whitenoise.middleware.WhiteNoiseMiddleware", *MIDDLEWARE)
