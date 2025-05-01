"""Core app views."""
from typing import Any
from django.http import HttpRequest, HttpResponse
from django.views import View


class HelloWorldView(View):
    """A simple class-based view that returns a greeting."""
    
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        """Handle GET requests with a friendly greeting."""
        try:
            return HttpResponse("Hello, World! Welcome to Django!")
        except Exception as e:
            return HttpResponse(f"An error occurred: {str(e)}", status=500)
