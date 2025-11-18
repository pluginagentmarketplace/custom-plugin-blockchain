---
name: architecture-design-patterns
description: Master software architecture, design patterns, and system design. Use when designing systems, understanding architecture patterns, or preparing for system design interviews.
---

# Architecture & Design Patterns Skill

Comprehensive guide to software architecture and design patterns.

## Quick Start

### Design Patterns - Creational

#### Singleton Pattern
```javascript
class Logger {
  constructor() {
    if (Logger.instance) {
      return Logger.instance;
    }
    this.logs = [];
    Logger.instance = this;
  }

  log(message) {
    this.logs.push(message);
    console.log(message);
  }
}

const logger1 = new Logger();
const logger2 = new Logger();
console.log(logger1 === logger2); // true
```

#### Factory Pattern
```javascript
class Animal {}
class Dog extends Animal {
  bark() { console.log('Woof!'); }
}
class Cat extends Animal {
  meow() { console.log('Meow!'); }
}

class AnimalFactory {
  static createAnimal(type) {
    switch(type) {
      case 'dog': return new Dog();
      case 'cat': return new Cat();
      default: throw new Error('Unknown animal');
    }
  }
}

const dog = AnimalFactory.createAnimal('dog');
dog.bark();
```

### Design Patterns - Structural

#### Adapter Pattern
```javascript
// Legacy interface
class OldLogger {
  writeLog(msg) {
    console.log('[OLD] ' + msg);
  }
}

// New interface
class NewLogger {
  info(msg) { console.log('[INFO] ' + msg); }
  error(msg) { console.log('[ERROR] ' + msg); }
}

// Adapter
class LoggerAdapter extends NewLogger {
  constructor(oldLogger) {
    super();
    this.oldLogger = oldLogger;
  }

  info(msg) {
    this.oldLogger.writeLog(msg);
  }
}
```

### Design Patterns - Behavioral

#### Observer Pattern
```javascript
class EventEmitter {
  constructor() {
    this.events = {};
  }

  on(event, callback) {
    if (!this.events[event]) {
      this.events[event] = [];
    }
    this.events[event].push(callback);
  }

  emit(event, data) {
    if (this.events[event]) {
      this.events[event].forEach(cb => cb(data));
    }
  }
}

const emitter = new EventEmitter();
emitter.on('user:login', (user) => {
  console.log(`${user} logged in`);
});
emitter.emit('user:login', 'John');
```

### Architectural Patterns

#### MVC Pattern
```javascript
// Model
class User {
  constructor(id, name, email) {
    this.id = id;
    this.name = name;
    this.email = email;
  }
}

// View
class UserView {
  displayUser(user) {
    console.log(`User: ${user.name} (${user.email})`);
  }
}

// Controller
class UserController {
  constructor(model, view) {
    this.model = model;
    this.view = view;
  }

  loadUser(id) {
    const user = this.model.find(id);
    this.view.displayUser(user);
  }
}
```

## Key Concepts

### Software Architecture
- Layered (N-tier) architecture
- Microservices architecture
- Event-driven architecture
- CQRS (Command Query Responsibility Segregation)
- Hexagonal architecture (Ports and Adapters)
- Service-oriented architecture (SOA)

### SOLID Principles
- **S**ingle Responsibility: One reason to change
- **O**pen/Closed: Open for extension, closed for modification
- **L**iskov Substitution: Subtypes must be substitutable
- **I**nterface Segregation: Many small interfaces
- **D**ependency Inversion: Depend on abstractions

### Design Patterns by Category

#### Creational Patterns
- Singleton
- Factory Method
- Abstract Factory
- Builder
- Prototype

#### Structural Patterns
- Adapter
- Bridge
- Composite
- Decorator
- Facade
- Flyweight
- Proxy

#### Behavioral Patterns
- Chain of Responsibility
- Command
- Iterator
- Mediator
- Memento
- Observer
- State
- Strategy
- Template Method
- Visitor

### Scalability Patterns
- Database sharding
- Caching layers
- Load balancing
- Circuit breaker
- Retry logic
- Bulkhead isolation
- Rate limiting
- API throttling

### Reliability Patterns
- Health checks
- Graceful degradation
- Bulkhead pattern
- Circuit breaker
- Timeout handling
- Fallback mechanisms

## System Design Concepts

### Capacity Planning
- Traffic estimation
- Storage requirements
- Bandwidth calculation
- Resource estimation

### Availability & Reliability
- Single points of failure
- Redundancy
- Replication
- Failover mechanisms
- SLA and SLO definition

### Performance Optimization
- Caching strategies
- Database optimization
- Network optimization
- Asynchronous processing
- Load balancing

### Security Architecture
- Authentication and authorization
- Encryption
- Data privacy
- Network security
- Compliance requirements

## Real-World Examples

### Design a URL Shortener
- Requirements analysis
- Capacity estimation
- Data model design
- Encoding scheme
- Cache strategy
- Redundancy and failover

### Design a Chat Application
- Real-time communication
- Message persistence
- Notification system
- Scalability considerations
- Group messaging

### Design a Video Streaming Platform
- Content delivery
- Adaptive bitrate streaming
- Caching strategy
- Database design
- Live streaming architecture

## Resources

- [Refactoring Guru Design Patterns](https://refactoring.guru/design-patterns/)
- [System Design Primer](https://github.com/donnemartin/system-design-primer/)
- [SOLID Principles](https://en.wikipedia.org/wiki/SOLID)
- [Microservices Architecture](https://martinfowler.com/microservices/)
- [Enterprise Integration Patterns](https://www.enterpriseintegrationpatterns.com/)
