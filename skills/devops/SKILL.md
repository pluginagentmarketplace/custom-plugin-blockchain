---
name: devops-infrastructure
description: Master DevOps practices including containerization, orchestration, CI/CD, and infrastructure automation. Use when deploying applications, setting up CI/CD, or managing infrastructure.
---

# DevOps & Infrastructure Skill

Comprehensive guide to DevOps practices and tools.

## Quick Start

### Docker Basics
```dockerfile
# Dockerfile for Node.js app
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm ci --only=production

COPY . .

EXPOSE 3000

CMD ["node", "index.js"]
```

### Docker Compose
```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      - DATABASE_URL=postgres://user:pass@db:5432/mydb
    depends_on:
      - db

  db:
    image: postgres:15
    environment:
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=mydb
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

### Kubernetes Deployment
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: app
        image: my-registry/my-app:1.0.0
        ports:
        - containerPort: 3000
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: app-secrets
              key: db-url
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
```

### GitHub Actions CI/CD
```yaml
name: CI/CD

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2

    - name: Setup Node.js
      uses: actions/setup-node@v2
      with:
        node-version: '18'

    - name: Install dependencies
      run: npm ci

    - name: Run tests
      run: npm test

    - name: Build
      run: npm run build

    - name: Deploy to production
      if: github.ref == 'refs/heads/main'
      run: npm run deploy
```

### Terraform Infrastructure
```hcl
provider "aws" {
  region = "us-east-1"
}

resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "main" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "us-east-1a"
}

resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.main.id

  tags = {
    Name = "web-server"
  }
}
```

## Key Concepts

### Containerization
- Image layers and optimization
- Registry management
- Container security scanning
- Resource limits
- Health checks
- Logging and monitoring

### Kubernetes
- Pods and containers
- Deployments and StatefulSets
- Services and networking
- ConfigMaps and Secrets
- Persistent volumes
- RBAC and security policies
- Helm charts for package management

### CI/CD Practices
- Automated testing
- Build automation
- Deployment pipelines
- Blue-green deployments
- Canary releases
- Rollback strategies
- Artifact management

### Infrastructure as Code
- Code-based infrastructure
- Version control for infrastructure
- State management
- Modularity and reusability
- Testing infrastructure code

### Monitoring & Observability
- Metrics collection
- Log aggregation
- Distributed tracing
- Alerting and on-call
- SLOs and SLIs
- Dashboard creation

## Popular Tools

### Containerization
- Docker: Container platform
- Podman: Docker alternative
- containerd: Container runtime

### Orchestration
- Kubernetes: Container orchestration
- Docker Swarm: Docker's native orchestration
- Nomad: Multi-workload orchestrator

### CI/CD
- GitHub Actions: GitHub's native CI/CD
- GitLab CI/CD: GitLab's solution
- Jenkins: Open-source automation
- CircleCI: Cloud CI/CD

### IaC
- Terraform: Multi-cloud IaC
- CloudFormation: AWS-specific
- Ansible: Configuration management
- Pulumi: Programmatic IaC

### Monitoring
- Prometheus: Metrics collection
- Grafana: Visualization
- ELK Stack: Logging
- Datadog: Comprehensive monitoring

## Resources

- [Docker Documentation](https://docs.docker.com/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Terraform Registry](https://registry.terraform.io/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
