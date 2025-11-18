---
name: backend-technologies
description: Master backend development with REST APIs, databases, authentication, and server frameworks. Use when building APIs, working with databases, or implementing backend logic.
---

# Backend Technologies Skill

Comprehensive guide to backend development and API design.

## Quick Start

### REST API with Express.js
```javascript
const express = require('express');
const app = express();

app.use(express.json());

// GET endpoint
app.get('/api/users/:id', (req, res) => {
  const { id } = req.params;
  res.json({ id, name: 'John Doe' });
});

// POST endpoint
app.post('/api/users', (req, res) => {
  const user = req.body;
  res.status(201).json(user);
});

// Error handling
app.use((err, req, res, next) => {
  res.status(500).json({ error: err.message });
});

app.listen(3000, () => {
  console.log('Server running on port 3000');
});
```

### Database Query (PostgreSQL)
```sql
-- Create table
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Query with joins
SELECT u.name, COUNT(p.id) as post_count
FROM users u
LEFT JOIN posts p ON u.id = p.user_id
GROUP BY u.id
ORDER BY post_count DESC;

-- Transactions
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### Authentication with JWT
```javascript
const jwt = require('jsonwebtoken');

// Generate token
function generateToken(userId) {
  return jwt.sign(
    { userId },
    process.env.JWT_SECRET,
    { expiresIn: '24h' }
  );
}

// Verify token middleware
function authMiddleware(req, res, next) {
  const token = req.headers.authorization?.split(' ')[1];

  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.userId = decoded.userId;
    next();
  } catch (error) {
    res.status(401).json({ error: 'Invalid token' });
  }
}
```

## Key Concepts

### API Design
- RESTful principles
- Resource-oriented URLs
- Proper HTTP methods and status codes
- Request/response format (JSON)
- Versioning strategies
- Rate limiting
- Error handling

### Database Design
- Normalization and relationships
- Indexes for performance
- Transactions and ACID properties
- Query optimization
- Connection pooling
- Migrations and schema versioning

### Security
- Input validation and sanitization
- SQL injection prevention
- CORS configuration
- Rate limiting
- Helmet middleware for headers
- Secure password hashing
- Environment variables for secrets

### Performance
- Caching strategies (Redis)
- Query optimization
- Database indexes
- Connection pooling
- Async/await patterns
- Load testing

## Popular Frameworks

### Node.js
- **Express**: Minimal web framework
- **Fastify**: High-performance alternative
- **NestJS**: Full-featured framework with TypeScript
- **Koa**: Lightweight successor to Express

### Python
- **Flask**: Lightweight microframework
- **Django**: Full-featured web framework
- **FastAPI**: Modern async framework
- **SQLAlchemy**: ORM library

### Java
- **Spring Boot**: Enterprise-grade framework
- **Quarkus**: Cloud-native alternative
- **Micronaut**: Lightweight framework

### Go
- **Gin**: Web framework
- **Echo**: High-performance framework
- **Fiber**: Express-inspired framework

## Tools & Libraries

### ORMs & Query Builders
- Prisma: Next-gen ORM
- Sequelize: Promise-based ORM
- TypeORM: ORM for TypeScript
- SQLAlchemy: Python ORM

### Testing
- Jest: Test framework
- Supertest: HTTP assertion library
- Mocha: Test runner
- Pytest: Python testing

### API Documentation
- Swagger/OpenAPI
- Postman
- Insomnia

## Resources

- [REST API Best Practices](https://restfulapi.net/)
- [Node.js Documentation](https://nodejs.org/docs/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [API Design Checklist](https://100.dataylane.com/api-design-best-practices/)
