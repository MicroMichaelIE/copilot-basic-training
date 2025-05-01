# Testing Guidelines for Backend Components

## Core Testing Principles
1. Write tests for all models, views, and services
2. Follow Django's TestCase patterns and pytest best practices
3. Use meaningful test descriptions that follow the pattern: "test_[component]_should_[expected_behavior]"

## Test Structure Requirements
```python
from django.test import TestCase
from rest_framework.test import APITestCase

class ModelNameTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Setup test data that can be shared across all tests
        pass

    def setUp(self):
        # Setup that's specific to each test method
        pass

    def test_model_should_create_successfully(self):
        # Basic creation test
        pass

    def test_model_should_validate_fields(self):
        # Validation tests
        pass

class APIEndpointTests(APITestCase):
    def setUp(self):
        # Setup authentication and test data
        pass

    def test_endpoint_should_return_correct_data(self):
        # API response tests
        pass

    def test_endpoint_should_handle_invalid_input(self):
        # Error handling tests
        pass
```

## Testing Rules
1. Use `django.test.TestCase` for model tests
2. Use `rest_framework.test.APITestCase` for API endpoint tests
3. Implement proper test factories using `factory_boy`
4. Mock external services and API calls using `unittest.mock` or `pytest-mock`
5. Test permissions and authentication scenarios
6. Use proper test database setup and teardown

## Coverage Requirements
- Minimum 80% test coverage for all components
- 100% coverage for critical business logic including:
  - Model methods and properties
  - Serializer validation
  - View permissions and authentication
  - Custom middleware
  - Service layer functions

## Unit Test Categories

1. Model Tests
   - Creation and deletion
   - Field validation
   - Custom model methods
   - Model properties and computed fields
   - Model constraints and unique validations

2. Serializer Tests
   - Field serialization and deserialization
   - Validation rules
   - Custom field transformations
   - Nested serializer behavior
   - Read-only and write-only fields

3. Service Layer Tests
   - Business logic functions
   - Data transformations
   - Calculation methods
   - Utility functions
   - Helper methods

4. Form Tests
   - Field validation
   - Custom clean methods
   - Form saving behavior
   - Initial data handling

## Best Practices
1. Database Management
   - Use `TransactionTestCase` for tests requiring transaction rollback
   - Implement proper database cleanup in `tearDown`
   - Use test fixtures sparingly, prefer factories

2. Mocking and Factories
   - Use `factory_boy` for creating test data
   - Mock external services and APIs
   - Create realistic test data that reflects production scenarios

3. Error Testing
   - Test all error conditions
   - Verify error message content
   - Check status codes and response formats
   - Test validation error scenarios

4. Test Organization
   - Group related tests in test classes
   - Use descriptive test method names
   - Keep tests focused and atomic
   - Follow arrange-act-assert pattern

## Testing Tools
1. Required Packages
   ```
   pytest-django
   factory-boy
   coverage
   pytest-cov
   pytest-mock
   ```

2. Recommended Configuration
   ```python
   # pytest.ini
   [pytest]
   DJANGO_SETTINGS_MODULE = project.settings.test
   python_files = tests.py test_*.py *_tests.py
   addopts = --nomigrations --cov=. --cov-report=html
   ```

## Continuous Integration
- Run tests on every pull request
- Maintain test coverage reports
- Implement pre-commit hooks for test execution
- Configure test automation in CI/CD pipeline
