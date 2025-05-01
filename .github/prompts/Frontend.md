# Frontend Development Guidelines

## Core Principles
- Write strictly typed components using TypeScript
- Maintain consistent React functional component patterns
- Ensure accessibility (WCAG) compliance in all components
- Optimize performance with proper hooks usage and memoization

## Component Structure
```typescript
// Standard component structure
interface ComponentProps {
    title: string;
}

export const Component = ({ title }: ComponentProps) => {
    // Component logic
}
```
It's important to keep the props interface at the top for better readability and maintainability. Further, export the component at the end to keep the structure clean.
It is better to avoid React.FC as it can lead to implicit children prop types and other issues - let's define our own prop types explicitly.

## State Management
- Use appropriate hooks (`useState`, `useReducer`, `useContext`)
- Implement proper data fetching patterns with `useEffect`
- Handle loading, error, and success states explicitly

## Type Safety
- Define interfaces for all props and state
- Use strict TypeScript compiler options
- Implement proper event handling types
- Utilize discriminated unions for complex state

## Performance Guidelines
- Memoize callbacks with `useCallback`
- Cache computed values with `useMemo`
- Implement proper React.Suspense boundaries
- Lazy load components when appropriate

## Testing Considerations
- Write unit tests for all components
- Implement integration tests for complex flows
- Use proper testing libraries (Jest, React Testing Library)
- Test accessibility with appropriate tools

## Code Style
- Follow consistent naming conventions
- Implement proper error boundaries
- Document complex logic with JSDoc
- Maintain clean component hierarchy