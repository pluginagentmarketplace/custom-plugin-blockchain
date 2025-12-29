# Blockchain DevOps Guide

> Blockchain Plugin - DevOps Skill Reference
> Node Operations & Infrastructure

## Overview

Guide for operating blockchain nodes, managing infrastructure, and ensuring high availability for blockchain systems.

## Node Operations

### Ethereum Node Setup (Docker)

```yaml
# docker-compose.yml
version: "3.8"

services:
  geth:
    image: ethereum/client-go:stable
    command:
      - --http
      - --http.addr=0.0.0.0
      - --http.api=eth,net,web3,txpool
      - --ws
      - --ws.addr=0.0.0.0
      - --syncmode=snap
      - --maxpeers=50
    ports:
      - "8545:8545"
      - "8546:8546"
      - "30303:30303"
    volumes:
      - geth-data:/root/.ethereum
    restart: unless-stopped

volumes:
  geth-data:
```

### Kubernetes Deployment

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: ethereum-node
spec:
  serviceName: ethereum
  replicas: 2
  template:
    spec:
      containers:
        - name: geth
          image: ethereum/client-go:stable
          resources:
            requests:
              cpu: "4"
              memory: "16Gi"
            limits:
              cpu: "8"
              memory: "32Gi"
          volumeMounts:
            - name: data
              mountPath: /root/.ethereum
  volumeClaimTemplates:
    - metadata:
        name: data
      spec:
        accessModes: ["ReadWriteOnce"]
        resources:
          requests:
            storage: 2Ti
```

## Monitoring

### Prometheus Metrics

```yaml
# prometheus.yml
scrape_configs:
  - job_name: 'geth'
    static_configs:
      - targets: ['geth:6060']
    metrics_path: /debug/metrics/prometheus
```

### Grafana Alerts

```yaml
- alert: NodeSyncLag
  expr: eth_block_number - eth_highest_block > 100
  for: 5m
  labels:
    severity: warning

- alert: LowPeerCount
  expr: eth_peer_count < 10
  for: 10m
  labels:
    severity: warning
```

---

*Blockchain Plugin - DevOps Skill*
