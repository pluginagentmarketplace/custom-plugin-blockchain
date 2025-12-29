# Blockchain Data Analysis Guide

> Blockchain Plugin - Data-AI Skill Reference
> On-Chain Analytics & ML

## Overview

Guide for analyzing blockchain data, detecting patterns, and building ML models for blockchain applications.

## Data Sources

### On-Chain Data

```python
from web3 import Web3

w3 = Web3(Web3.HTTPProvider(rpc_url))

# Get transaction
tx = w3.eth.get_transaction(tx_hash)

# Get block with transactions
block = w3.eth.get_block('latest', full_transactions=True)

# Get logs/events
logs = w3.eth.get_logs({
    'address': contract_address,
    'fromBlock': 'latest',
    'topics': [event_signature]
})
```

### Dune Analytics SQL

```sql
-- Daily active addresses
SELECT
    date_trunc('day', block_time) as day,
    COUNT(DISTINCT "from") as active_addresses,
    SUM(gas_used * gas_price) / 1e18 as total_eth_fees
FROM ethereum.transactions
WHERE block_time >= NOW() - INTERVAL '30 days'
GROUP BY 1
ORDER BY 1
```

## ML Applications

### Fraud Detection Features

```python
features = {
    'tx_count_24h': int,
    'unique_receivers': int,
    'avg_tx_value': float,
    'gas_usage_pattern': float,
    'contract_interaction_ratio': float,
    'mixer_interaction': bool,
    'known_scam_interaction': bool,
}
```

---

*Blockchain Plugin - Data-AI Skill*
