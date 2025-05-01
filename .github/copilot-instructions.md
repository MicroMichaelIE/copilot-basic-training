# Copilot Alignment Instructions
## Frontend (React + TypeScript)

1. Use functional components with explicit TypeScript interfaces for props
2. Follow React hooks naming convention (use'Effect', use'State', etc.)
3. Implement proper error boundaries and loading states
4. Use typed event handlers (MouseEvent, FormEvent, etc.)
5. Maintain consistent component file structure (props interface -> component -> exports)

## Backend (Python Django)

1. Follow Django REST framework patterns for API endpoints
2. Use type hints for all Python functions and class methods
3. Implement proper exception handling with custom exception classes
4. Structure Django models with clear relationships and field types
5. Follow Django's class-based views pattern when applicable

VERY IMPORTANT: we use a virtual environment for Python development. This should usable via python and pip. python3 and pip3 are the system default and should be avoided. If pip doesn't exist, you can active the environment with `source venv/bin/activate.fish` and then use pip.