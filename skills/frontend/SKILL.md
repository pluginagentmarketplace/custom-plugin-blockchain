---
name: frontend-technologies
description: Master frontend development with HTML, CSS, JavaScript, TypeScript, and modern frameworks. Use when working on web UIs, styling, component development, or state management.
---

# Frontend Technologies Skill

Comprehensive guide to frontend development technologies and best practices.

## Quick Start

### HTML Basics
```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My Site</title>
</head>
<body>
  <header>
    <nav>
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/about">About</a></li>
      </ul>
    </nav>
  </header>
</body>
</html>
```

### CSS Flexbox
```css
.container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
}

.item {
  flex: 1;
  min-width: 0;
}
```

### JavaScript ES6+
```javascript
// Arrow functions
const greet = (name) => `Hello, ${name}!`;

// Template literals
const message = `Welcome ${greet("World")}`;

// Destructuring
const { name, age } = user;
const [first, ...rest] = array;

// Async/await
async function fetchData() {
  try {
    const response = await fetch('/api/data');
    return await response.json();
  } catch (error) {
    console.error('Error:', error);
  }
}
```

### React Component
```javascript
import { useState, useEffect } from 'react';

export function Counter() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    document.title = `Count: ${count}`;
  }, [count]);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>
        Increment
      </button>
    </div>
  );
}
```

## Key Concepts

### Responsive Design
- Mobile-first approach
- Media queries
- Flexible grids and flexbox
- Viewport meta tag
- Touch-friendly interfaces

### Component Architecture
- Reusable components
- Props and composition
- Single responsibility principle
- Component hierarchy
- Container vs. presentational components

### State Management
- Local component state
- Context API
- Redux/Zustand/Jotai
- MobX for reactive state
- State machines

### Performance Optimization
- Code splitting
- Lazy loading
- Image optimization
- Bundle analysis
- Memoization strategies
- Virtual scrolling for large lists

## Tools & Frameworks

### Build Tools
- **Vite**: Fast build tool with HMR
- **Webpack**: Powerful bundler
- **Parcel**: Zero-config bundler
- **esbuild**: Extremely fast bundler

### Package Managers
- npm: Default Node package manager
- yarn: Fast, reliable alternative
- pnpm: Efficient disk usage

### Testing
- **Jest**: Popular test runner
- **Vitest**: Vite-native test runner
- **React Testing Library**: Component testing
- **Cypress**: E2E testing

## Resources

- [MDN Web Docs](https://developer.mozilla.org/)
- [React Documentation](https://react.dev/)
- [CSS-Tricks](https://css-tricks.com/)
- [Can I Use](https://caniuse.com/) - Browser compatibility
