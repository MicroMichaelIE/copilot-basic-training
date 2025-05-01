import os
from typing import Any

from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.http import HttpRequest, HttpResponse
from django.urls import path
from django.views import View

# Configure Django settings with better security
settings.configure(
    DEBUG=os.getenv('DJANGO_DEBUG', 'False').lower() == 'true',
    SECRET_KEY=os.getenv('DJANGO_SECRET_KEY', os.urandom(32).hex()),
    ROOT_URLCONF=__name__,
    INSTALLED_APPS=[
        'django.contrib.contenttypes',
        'django.contrib.auth',
        'django.contrib.sessions',
    ],
    MIDDLEWARE=[
        'django.middleware.security.SecurityMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ],
    ALLOWED_HOSTS=['localhost', '127.0.0.1'],)

class HelloWorldView(View):
    """A simple class-based view that returns a greeting."""
    
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        """Handle GET requests with a friendly greeting."""
        try:
            return HttpResponse("Hello, World! Welcome to Django!")
        except Exception as e:
            return HttpResponse(f"An error occurred: {str(e)}", status=500)

# URL patterns using class-based views
urlpatterns = [
    path('', HelloWorldView.as_view(), name='hello_world'),
]

# WSGI application
application = get_wsgi_application()

if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(['manage.py', 'runserver', '8000'])