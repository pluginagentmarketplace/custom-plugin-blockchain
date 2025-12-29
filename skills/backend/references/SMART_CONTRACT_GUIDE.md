# Smart Contract Development Guide

> Blockchain Plugin - Backend Skill Reference
> Solidity & Smart Contract Development

## Overview

Guide for developing secure, gas-efficient smart contracts using Solidity and modern development frameworks.

## Table of Contents

1. [Contract Architecture](#contract-architecture)
2. [Security Patterns](#security-patterns)
3. [Gas Optimization](#gas-optimization)
4. [Testing Strategies](#testing-strategies)

---

## Contract Architecture

### Modern Solidity Pattern

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import {ERC20} from "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import {Ownable} from "@openzeppelin/contracts/access/Ownable.sol";
import {ReentrancyGuard} from "@openzeppelin/contracts/utils/ReentrancyGuard.sol";

contract MyToken is ERC20, Ownable, ReentrancyGuard {
    uint256 public constant MAX_SUPPLY = 1_000_000 * 10**18;

    mapping(address => bool) public blacklisted;

    event Blacklisted(address indexed account, bool status);

    error MaxSupplyExceeded();
    error AccountBlacklisted();

    constructor() ERC20("MyToken", "MTK") Ownable(msg.sender) {}

    function mint(address to, uint256 amount) external onlyOwner {
        if (totalSupply() + amount > MAX_SUPPLY) {
            revert MaxSupplyExceeded();
        }
        _mint(to, amount);
    }

    function _update(
        address from,
        address to,
        uint256 value
    ) internal override {
        if (blacklisted[from] || blacklisted[to]) {
            revert AccountBlacklisted();
        }
        super._update(from, to, value);
    }
}
```

---

## Security Patterns

### Reentrancy Protection

```solidity
// Using OpenZeppelin ReentrancyGuard
import {ReentrancyGuard} from "@openzeppelin/contracts/utils/ReentrancyGuard.sol";

contract Vault is ReentrancyGuard {
    mapping(address => uint256) public balances;

    function withdraw(uint256 amount) external nonReentrant {
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update state BEFORE external call (CEI pattern)
        balances[msg.sender] -= amount;

        // External call after state update
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");
    }
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
        _grantRole(ADMIN_ROLE, msg.sender);
    }

    function spend(address to, uint256 amount)
        external
        onlyRole(SPENDER_ROLE)
    {
        // spending logic
    }
}
```

---

## Gas Optimization

### Storage Optimization

```solidity
// ❌ Bad: Multiple storage reads
function badExample() external {
    uint256 a = storageVar;
    uint256 b = storageVar + 1;
    uint256 c = storageVar + 2;
}

// ✅ Good: Cache storage in memory
function goodExample() external {
    uint256 cached = storageVar;
    uint256 a = cached;
    uint256 b = cached + 1;
    uint256 c = cached + 2;
}

// ✅ Use immutable for constructor-set values
uint256 public immutable deploymentTime;

// ✅ Pack storage variables
struct UserData {
    uint128 balance;    // slot 0
    uint64 lastUpdate;  // slot 0
    uint64 nonce;       // slot 0
}
```

---

## Testing Strategies

### Foundry Test Pattern

```solidity
// test/MyToken.t.sol
pragma solidity ^0.8.20;

import {Test, console2} from "forge-std/Test.sol";
import {MyToken} from "../src/MyToken.sol";

contract MyTokenTest is Test {
    MyToken public token;
    address public owner = address(1);
    address public user = address(2);

    function setUp() public {
        vm.prank(owner);
        token = new MyToken();
    }

    function test_Mint() public {
        vm.prank(owner);
        token.mint(user, 1000 ether);
        assertEq(token.balanceOf(user), 1000 ether);
    }

    function testFuzz_Mint(uint256 amount) public {
        amount = bound(amount, 0, token.MAX_SUPPLY());
        vm.prank(owner);
        token.mint(user, amount);
        assertEq(token.balanceOf(user), amount);
    }

    function testFail_MintExceedsMaxSupply() public {
        vm.prank(owner);
        token.mint(user, token.MAX_SUPPLY() + 1);
    }
}
```

---

## Resources

- [Solidity Documentation](https://docs.soliditylang.org)
- [OpenZeppelin Contracts](https://docs.openzeppelin.com/contracts)
- [Foundry Book](https://book.getfoundry.sh)
- [Consensys Best Practices](https://consensys.github.io/smart-contract-best-practices)

---

*Blockchain Plugin - Backend Skill*
