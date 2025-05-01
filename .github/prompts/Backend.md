# Backend Development Guidelines

## Django REST Framework Development

### Code Structure and Organization
- Organize views using class-based views with proper mixins
- Implement clear model relationships with appropriate field types
- Structure URLs in a RESTful pattern
- Keep business logic in services/utils separate from views

### Type Safety & Documentation
- Use Python type hints for all functions and methods
- Document APIs using Django REST swagger/OpenAPI
- Include docstrings for complex functions
- Annotate model fields with appropriate choices/validators

### API Development
- Follow REST conventions for endpoint naming
- Implement proper serializer validation
- Use viewsets for CRUD operations
- Include pagination for list endpoints

### Error Handling
- Create custom exception classes for business logic
- Implement proper exception handling middleware
- Return standardized error responses
- Log errors appropriately

### Security
- Implement proper authentication/authorization
- Validate all input data
- Use Django's security middleware
- Follow OWASP security guidelines

### Testing
- Write unit tests for models and services
- Include integration tests for APIs
- Test error scenarios and edge cases
- Maintain minimum 80% code coverage

### Performance
- Optimize database queries
- Implement caching where appropriate
- Use bulk operations for large datasets
- Profile and monitor API performance