# Blockchain Database Guide

> Blockchain Plugin - Database Skill Reference
> On-Chain Data Storage & Indexing

## Overview

Guide for storing and querying blockchain data efficiently.

## Schema Design

### Core Tables

```sql
-- Blocks table
CREATE TABLE blocks (
    number BIGINT PRIMARY KEY,
    hash CHAR(66) NOT NULL UNIQUE,
    parent_hash CHAR(66) NOT NULL,
    timestamp TIMESTAMPTZ NOT NULL,
    gas_used BIGINT NOT NULL,
    gas_limit BIGINT NOT NULL,
    base_fee_per_gas BIGINT,
    transaction_count INT NOT NULL
);

-- Transactions table
CREATE TABLE transactions (
    hash CHAR(66) PRIMARY KEY,
    block_number BIGINT REFERENCES blocks(number),
    "from" CHAR(42) NOT NULL,
    "to" CHAR(42),
    value NUMERIC(78, 0) NOT NULL,
    gas_used BIGINT NOT NULL,
    gas_price BIGINT NOT NULL,
    input BYTEA,
    status SMALLINT NOT NULL,
    tx_index INT NOT NULL
);

-- Indexes
CREATE INDEX idx_tx_from ON transactions("from");
CREATE INDEX idx_tx_to ON transactions("to");
CREATE INDEX idx_tx_block ON transactions(block_number);
```

### Event Logs

```sql
CREATE TABLE events (
    id BIGSERIAL PRIMARY KEY,
    block_number BIGINT NOT NULL,
    tx_hash CHAR(66) NOT NULL,
    log_index INT NOT NULL,
    contract CHAR(42) NOT NULL,
    topic0 CHAR(66) NOT NULL,
    topic1 CHAR(66),
    topic2 CHAR(66),
    topic3 CHAR(66),
    data BYTEA
);

CREATE INDEX idx_events_contract ON events(contract);
CREATE INDEX idx_events_topic0 ON events(topic0);
```

## Query Patterns

### Get Recent Transactions

```sql
SELECT *
FROM transactions
WHERE "from" = $1 OR "to" = $1
ORDER BY block_number DESC
LIMIT 100;
```

---

*Blockchain Plugin - Database Skill*
