#!/usr/bin/env python3
"""
Web3 Component Analyzer - Blockchain Plugin
Analyzes DApp frontend components and Web3 integration patterns.
"""

import os
import re
import json
from pathlib import Path
from dataclasses import dataclass, field


@dataclass
class Web3ComponentMetrics:
    """Metrics for Web3 frontend components."""
    name: str
    file_path: str
    has_wallet_connection: bool = False
    has_contract_interaction: bool = False
    has_transaction_handling: bool = False
    web3_hooks_used: list = field(default_factory=list)
    chains_supported: list = field(default_factory=list)
    issues: list = field(default_factory=list)


class Web3ComponentAnalyzer:
    """Analyze Web3 DApp frontend components."""

    WEB3_HOOKS = [
        'useAccount', 'useConnect', 'useDisconnect', 'useNetwork',
        'useContractRead', 'useContractWrite', 'usePrepareContractWrite',
        'useBalance', 'useToken', 'useEnsName', 'useEnsAddress',
        'useSendTransaction', 'useWaitForTransaction', 'useSignMessage',
        'useProvider', 'useSigner', 'useContract'
    ]

    def __init__(self, project_path: str):
        self.project_path = Path(project_path)
        self.components: list[Web3ComponentMetrics] = []

    def analyze_project(self) -> dict:
        """Analyze all Web3 components."""
        tsx_files = list(self.project_path.rglob("*.tsx"))
        tsx_files += list(self.project_path.rglob("*.jsx"))

        for file_path in tsx_files:
            if 'node_modules' in str(file_path):
                continue
            metrics = self._analyze_component(file_path)
            if metrics and (metrics.has_wallet_connection or metrics.has_contract_interaction):
                self.components.append(metrics)

        return self._generate_report()

    def _analyze_component(self, file_path: Path) -> Web3ComponentMetrics:
        """Analyze a single component for Web3 patterns."""
        try:
            content = file_path.read_text()
        except:
            return None

        metrics = Web3ComponentMetrics(
            name=file_path.stem,
            file_path=str(file_path)
        )

        # Check for wallet connection patterns
        wallet_patterns = ['useConnect', 'useAccount', 'ConnectButton', 'WalletConnect']
        metrics.has_wallet_connection = any(p in content for p in wallet_patterns)

        # Check for contract interaction
        contract_patterns = ['useContractRead', 'useContractWrite', 'contract.']
        metrics.has_contract_interaction = any(p in content for p in contract_patterns)

        # Check for transaction handling
        tx_patterns = ['useSendTransaction', 'useWaitForTransaction', 'sendTransaction']
        metrics.has_transaction_handling = any(p in content for p in tx_patterns)

        # Find Web3 hooks used
        for hook in self.WEB3_HOOKS:
            if hook in content:
                metrics.web3_hooks_used.append(hook)

        # Find supported chains
        chain_patterns = {
            'mainnet': r'chainId.*?1[,\s\)]',
            'polygon': r'chainId.*?137',
            'arbitrum': r'chainId.*?42161',
            'optimism': r'chainId.*?10[,\s\)]',
            'sepolia': r'chainId.*?11155111',
        }
        for chain, pattern in chain_patterns.items():
            if re.search(pattern, content):
                metrics.chains_supported.append(chain)

        # Detect issues
        metrics.issues = self._detect_issues(content, metrics)

        return metrics

    def _detect_issues(self, content: str, metrics: Web3ComponentMetrics) -> list:
        """Detect common Web3 frontend issues."""
        issues = []

        # No error handling for transactions
        if metrics.has_transaction_handling:
            if 'onError' not in content and 'catch' not in content:
                issues.append("Transaction without error handling")

        # No loading state for async operations
        if metrics.has_contract_interaction:
            if 'isLoading' not in content and 'isPending' not in content:
                issues.append("Contract interaction without loading state")

        # Hardcoded addresses
        if re.search(r'0x[a-fA-F0-9]{40}', content):
            if 'import' not in content.split('0x')[0][-100:]:
                issues.append("Possible hardcoded contract address")

        # No network check
        if metrics.has_contract_interaction and 'useNetwork' not in content:
            issues.append("Contract interaction without network verification")

        return issues

    def _generate_report(self) -> dict:
        """Generate analysis report."""
        if not self.components:
            return {"message": "No Web3 components found"}

        total_wallet = sum(1 for c in self.components if c.has_wallet_connection)
        total_contract = sum(1 for c in self.components if c.has_contract_interaction)
        total_issues = sum(len(c.issues) for c in self.components)

        return {
            "summary": {
                "total_web3_components": len(self.components),
                "wallet_connected_components": total_wallet,
                "contract_interaction_components": total_contract,
                "total_issues": total_issues,
            },
            "components": [
                {
                    "name": c.name,
                    "path": c.file_path,
                    "wallet_connection": c.has_wallet_connection,
                    "contract_interaction": c.has_contract_interaction,
                    "hooks_used": c.web3_hooks_used,
                    "chains": c.chains_supported,
                    "issues": c.issues,
                }
                for c in self.components
            ],
            "recommendations": self._generate_recommendations(),
        }

    def _generate_recommendations(self) -> list:
        """Generate Web3 frontend recommendations."""
        recommendations = []

        no_error_handling = [c for c in self.components if "Transaction without error handling" in c.issues]
        if no_error_handling:
            recommendations.append(
                f"Add error handling to {len(no_error_handling)} components with transactions"
            )

        no_network_check = [c for c in self.components if "Contract interaction without network verification" in c.issues]
        if no_network_check:
            recommendations.append(
                "Add network verification before contract interactions"
            )

        return recommendations


def main():
    import sys
    project_path = sys.argv[1] if len(sys.argv) > 1 else "."
    analyzer = Web3ComponentAnalyzer(project_path)
    report = analyzer.analyze_project()
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
