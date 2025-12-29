#!/usr/bin/env python3
"""
Blockchain Node Health Checker - Blockchain Plugin
Monitors blockchain node health and sync status.
"""

import json
import time
import requests
from dataclasses import dataclass
from typing import Optional


@dataclass
class NodeHealth:
    """Node health status."""
    is_syncing: bool
    current_block: int
    highest_block: int
    peer_count: int
    chain_id: int
    client_version: str
    sync_percentage: float
    health_status: str
    issues: list


class BlockchainNodeChecker:
    """Check blockchain node health."""

    def __init__(self, rpc_url: str):
        self.rpc_url = rpc_url

    def check_health(self) -> NodeHealth:
        """Perform comprehensive health check."""
        issues = []

        # Get sync status
        sync_status = self._call_rpc("eth_syncing")
        is_syncing = sync_status is not False

        if is_syncing:
            current_block = int(sync_status.get("currentBlock", "0x0"), 16)
            highest_block = int(sync_status.get("highestBlock", "0x0"), 16)
        else:
            current_block = int(self._call_rpc("eth_blockNumber"), 16)
            highest_block = current_block

        sync_percentage = (current_block / highest_block * 100) if highest_block > 0 else 0

        # Get peer count
        peer_count = int(self._call_rpc("net_peerCount"), 16)
        if peer_count < 10:
            issues.append(f"Low peer count: {peer_count}")

        # Get chain ID
        chain_id = int(self._call_rpc("eth_chainId"), 16)

        # Get client version
        client_version = self._call_rpc("web3_clientVersion")

        # Determine health status
        if is_syncing and sync_percentage < 99:
            health_status = "syncing"
        elif peer_count < 5:
            health_status = "degraded"
            issues.append("Critical: Very low peer count")
        elif issues:
            health_status = "warning"
        else:
            health_status = "healthy"

        return NodeHealth(
            is_syncing=is_syncing,
            current_block=current_block,
            highest_block=highest_block,
            peer_count=peer_count,
            chain_id=chain_id,
            client_version=client_version,
            sync_percentage=round(sync_percentage, 2),
            health_status=health_status,
            issues=issues
        )

    def _call_rpc(self, method: str, params: list = None) -> any:
        """Make JSON-RPC call."""
        payload = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params or [],
            "id": 1
        }
        response = requests.post(self.rpc_url, json=payload, timeout=10)
        result = response.json()
        return result.get("result")

    def generate_report(self) -> dict:
        """Generate health report."""
        health = self.check_health()

        return {
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "rpc_url": self.rpc_url,
            "status": health.health_status,
            "node": {
                "client": health.client_version,
                "chain_id": health.chain_id,
                "peer_count": health.peer_count,
            },
            "sync": {
                "is_syncing": health.is_syncing,
                "current_block": health.current_block,
                "highest_block": health.highest_block,
                "percentage": health.sync_percentage,
            },
            "issues": health.issues,
        }


def main():
    import sys
    rpc_url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8545"

    checker = BlockchainNodeChecker(rpc_url)
    report = checker.generate_report()
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
