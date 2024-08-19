import os

AUTH_USER_MODEL = 'bookshelf.CustomUser'
SECURE_SSL_REDIRECT = True

# HTTP Strict Transport Security (HSTS) settings
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'your-secret-key')