# DApp Architecture Guide

> Blockchain Plugin - Architecture Skill Reference
> Decentralized Application Design

## Overview

Guide for designing secure, scalable decentralized applications.

## Architecture Layers

```
┌────────────────────────────────────────────┐
│           Presentation Layer               │
│  (Web3 Frontend, Mobile, Extensions)       │
├────────────────────────────────────────────┤
│           Application Layer                │
│  (API Gateway, Indexer, Notifications)     │
├────────────────────────────────────────────┤
│           Blockchain Layer                 │
│  (Smart Contracts, Oracles, Bridges)       │
├────────────────────────────────────────────┤
│             Data Layer                     │
│  (PostgreSQL, Redis, IPFS)                 │
└────────────────────────────────────────────┘
```

## Smart Contract Patterns

### Upgradeable Proxy (UUPS)

```solidity
import {UUPSUpgradeable} from "@openzeppelin/contracts-upgradeable/proxy/utils/UUPSUpgradeable.sol";

contract MyContract is UUPSUpgradeable, OwnableUpgradeable {
    function initialize() public initializer {
        __Ownable_init(msg.sender);
        __UUPSUpgradeable_init();
    }

    function _authorizeUpgrade(address) internal override onlyOwner {}
}
```

### Access Control

```solidity
import {AccessControl} from "@openzeppelin/contracts/access/AccessControl.sol";

contract Treasury is AccessControl {
    bytes32 public constant ADMIN_ROLE = keccak256("ADMIN_ROLE");
    bytes32 public constant SPENDER_ROLE = keccak256("SPENDER_ROLE");

    constructor() {
        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
    }
}
```

## Security Checklist

- [ ] Implement access control
- [ ] Add timelock for governance
- [ ] Use multisig for admin operations
- [ ] Conduct security audit
- [ ] Set up monitoring

---

*Blockchain Plugin - Architecture Skill*
