# Testing Guidelines for Frontend Components

## Core Testing Principles
1. Write tests for every new component and feature
2. Follow the React Testing Library philosophy: test behavior, not implementation
3. Use meaningful test descriptions that follow the pattern: "it should [expected behavior]"

## Test Structure Requirements
```typescript
describe('ComponentName', () => {
    beforeEach(() => {
        // Setup test environment
    });

    it('should render successfully', () => {
        // Basic render test
    });

    it('should handle user interactions', () => {
        // Interaction tests
    });
});
```

## Testing Rules
1. Use `@testing-library/react` and `@testing-library/jest-dom` as primary testing tools
2. Mock external dependencies and API calls
3. Test loading, error, and success states
4. Verify component accessibility using `jest-axe`

## Coverage Requirements
- Minimum 80% test coverage for all components
- 100% coverage for critical business logic
- Test all user interactions and state changes
- Include edge cases and error scenarios

