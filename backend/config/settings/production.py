from .base import *

DEBUG = False

if not SECRET_KEY:
    raise ValueError("SECRET_KEY must be configured in production.")

if not ALLOWED_HOSTS:
    raise ValueError("ALLOWED_HOSTS must be configured in production.")

SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True