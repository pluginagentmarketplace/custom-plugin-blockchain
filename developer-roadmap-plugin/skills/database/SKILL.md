---
name: database-technologies
description: Master database design and management with SQL, NoSQL, and advanced querying techniques. Use when designing databases, optimizing queries, or choosing database solutions.
---

# Database Technologies Skill

Comprehensive guide to database design and optimization.

## Quick Start

### SQL Fundamentals
```sql
-- Create table
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert data
INSERT INTO users (name, email)
VALUES ('John Doe', 'john@example.com');

-- Query with WHERE and ORDER BY
SELECT * FROM users
WHERE created_at > NOW() - INTERVAL '7 days'
ORDER BY name ASC;

-- Join tables
SELECT u.name, COUNT(p.id) as post_count
FROM users u
LEFT JOIN posts p ON u.id = p.user_id
GROUP BY u.id
HAVING COUNT(p.id) > 5;

-- Update and Delete
UPDATE users SET name = 'Jane Doe' WHERE id = 1;
DELETE FROM users WHERE created_at < NOW() - INTERVAL '1 year';
```

### PostgreSQL Advanced Features
```sql
-- Window functions
SELECT
  name,
  salary,
  AVG(salary) OVER (PARTITION BY department) as avg_dept_salary
FROM employees
ORDER BY department, salary DESC;

-- Common Table Expressions (CTE)
WITH ranked_users AS (
  SELECT
    id,
    name,
    ROW_NUMBER() OVER (ORDER BY created_at) as rank
  FROM users
)
SELECT * FROM ranked_users
WHERE rank <= 10;

-- Indexing for performance
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_posts_user_created ON posts(user_id, created_at);
```

### MongoDB Document Operations
```javascript
// Create collection and insert
db.users.insertOne({
  name: "John Doe",
  email: "john@example.com",
  age: 30,
  tags: ["developer", "python"]
});

// Query with filters
db.users.find({
  age: { $gte: 25, $lte: 35 },
  tags: { $in: ["python", "javascript"] }
});

// Update operations
db.users.updateOne(
  { _id: ObjectId("...") },
  { $set: { status: "active" } }
);

// Aggregation pipeline
db.users.aggregate([
  { $match: { status: "active" } },
  { $group: { _id: "$department", count: { $sum: 1 } } },
  { $sort: { count: -1 } }
]);
```

### Redis for Caching
```javascript
// Redis with Node.js
const redis = require('redis');
const client = redis.createClient();

// Basic operations
await client.set('user:1:name', 'John Doe', { EX: 3600 });
const name = await client.get('user:1:name');

// List operations
await client.rPush('tasks:pending', 'task1', 'task2');
const tasks = await client.lRange('tasks:pending', 0, -1);

// Set operations
await client.sAdd('tags:1', 'javascript', 'python', 'golang');
const tags = await client.sMembers('tags:1');

// Sorted set for leaderboard
await client.zAdd('leaderboard', {
  score: 100,
  member: 'player1'
});
const topPlayers = await client.zRevRange('leaderboard', 0, 9);
```

## Key Concepts

### Database Design
- Normalization (1NF, 2NF, 3NF, BCNF)
- Entity-Relationship (ER) models
- Denormalization for performance
- Partitioning and sharding
- Primary and foreign keys
- Constraints and validation

### Query Optimization
- Query planning and EXPLAIN
- Index strategies
- Join optimization
- Avoiding N+1 queries
- Query caching
- Batch operations

### Transactions
- ACID properties
- Isolation levels
- Deadlock prevention
- Two-phase commit
- Optimistic locking
- Pessimistic locking

### NoSQL Considerations
- Flexible schemas
- Horizontal scalability
- Eventual consistency
- Document vs. key-value vs. column-family
- CAP theorem
- Replication strategies

### Backup and Recovery
- Backup strategies
- Point-in-time recovery
- Disaster recovery planning
- Replication
- Failover strategies

## Popular Databases

### SQL Databases
- PostgreSQL: Advanced, open-source
- MySQL: Widely used, reliable
- MariaDB: MySQL fork
- Oracle: Enterprise-grade

### NoSQL Databases
- MongoDB: Document database
- Redis: In-memory cache and database
- Elasticsearch: Search and analytics
- Cassandra: Distributed, high-scale
- DynamoDB: AWS managed service

## Tools for Database Management

- **pgAdmin**: PostgreSQL administration
- **MySQL Workbench**: MySQL tool
- **MongoDB Compass**: MongoDB GUI
- **DBeaver**: Universal database client
- **Liquibase**: Database version control
- **Flyway**: Database migrations

## Resources

- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [MongoDB Documentation](https://docs.mongodb.com/)
- [Redis Documentation](https://redis.io/documentation)
- [SQL Tutorial](https://sqlzoo.net/)
- [Database Design Course](https://www.udacity.com/course/database-optimization--ud451)
