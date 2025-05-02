"""Core app views."""
import json
from typing import Any, Dict, List
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import Cat


class HelloWorldView(View):
    """A simple class-based view that returns a greeting."""
    
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        """Handle GET requests with a friendly greeting."""
        try:
            return HttpResponse("Hello, World! Welcome to Django!")
        except Exception as e:
            return HttpResponse(f"An error occurred: {str(e)}", status=500)


@method_decorator(csrf_exempt, name='dispatch') # Exempt from CSRF for simplicity in API usage
class CatListView(View):
    """View for listing all cats (GET) and adding a new cat (POST)."""

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> JsonResponse:
        """Handle GET requests to return all cats."""
        try:
            cats: List[Dict[str, Any]] = list(
                Cat.objects.values('id', 'name', 'breed', 'age')
            )
            return JsonResponse({'cats': cats}, safe=False)
        except Exception as e:
            return JsonResponse(
                {'error': f'An error occurred: {str(e)}'}, 
                status=500
            )

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> JsonResponse:
        """Handle POST requests to add a new cat."""
        try:
            data: Dict[str, Any] = json.loads(request.body)
            name = data.get('name')
            breed = data.get('breed')
            age = data.get('age')

            if not name or not breed or age is None:
                return JsonResponse({'error': 'Missing required fields (name, breed, age)'}, status=400)

            # Basic type validation for age
            try:
                age_int = int(age)
            except (ValueError, TypeError):
                 return JsonResponse({'error': 'Age must be a valid integer'}, status=400)

            cat = Cat.objects.create(name=name, breed=breed, age=age_int)
            return JsonResponse(
                {'message': 'Cat added successfully', 'cat': {'id': cat.id, 'name': cat.name, 'breed': cat.breed, 'age': cat.age}},
                status=201 # HTTP 201 Created
            )
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format in request body'}, status=400)
        except Exception as e:
            # It's good practice to log the exception e here
            return JsonResponse(
                {'error': f'An internal server error occurred'}, # Avoid exposing internal error details like str(e)
                status=500
            )
