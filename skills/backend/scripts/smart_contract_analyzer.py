#!/usr/bin/env python3
"""
Smart Contract Analyzer - Blockchain Plugin
Analyzes Solidity smart contracts for patterns and vulnerabilities.
"""

import os
import re
import json
from pathlib import Path
from dataclasses import dataclass, field


@dataclass
class ContractMetrics:
    """Metrics for a smart contract."""
    name: str
    file_path: str
    solidity_version: str = ""
    lines_of_code: int = 0
    functions: int = 0
    modifiers: int = 0
    events: int = 0
    has_reentrancy_guard: bool = False
    has_access_control: bool = False
    uses_safe_math: bool = False
    vulnerabilities: list = field(default_factory=list)
    gas_patterns: list = field(default_factory=list)


class SmartContractAnalyzer:
    """Analyze Solidity smart contracts."""

    VULNERABILITY_PATTERNS = {
        'reentrancy': r'\.call\{value:.*\}\(|\.send\(|\.transfer\(',
        'tx_origin': r'tx\.origin',
        'timestamp_dependency': r'block\.timestamp|now',
        'unchecked_return': r'\.call\(.*\);(?!\s*require)',
        'floating_pragma': r'pragma solidity \^',
    }

    GAS_OPTIMIZATION_PATTERNS = {
        'use_immutable': r'(public|private|internal)\s+\w+\s+\w+;(?!.*immutable)',
        'multiple_sstore': r'storage\[.*\]\s*=.*;\s*storage\[.*\]\s*=',
        'loop_length': r'for\s*\(.*\.length',
    }

    def __init__(self, project_path: str):
        self.project_path = Path(project_path)
        self.contracts: list[ContractMetrics] = []

    def analyze_project(self) -> dict:
        """Analyze all Solidity contracts."""
        sol_files = list(self.project_path.rglob("*.sol"))

        for file_path in sol_files:
            if 'node_modules' in str(file_path) or 'lib' in str(file_path):
                continue
            metrics = self._analyze_contract(file_path)
            if metrics:
                self.contracts.append(metrics)

        return self._generate_report()

    def _analyze_contract(self, file_path: Path) -> ContractMetrics:
        """Analyze a single Solidity file."""
        try:
            content = file_path.read_text()
        except:
            return None

        # Extract contract name
        contract_match = re.search(r'contract\s+(\w+)', content)
        name = contract_match.group(1) if contract_match else file_path.stem

        metrics = ContractMetrics(name=name, file_path=str(file_path))

        # Solidity version
        version_match = re.search(r'pragma solidity\s+([^;]+);', content)
        metrics.solidity_version = version_match.group(1) if version_match else "unknown"

        # Count elements
        metrics.lines_of_code = len([l for l in content.split('\n') if l.strip()])
        metrics.functions = len(re.findall(r'function\s+\w+', content))
        metrics.modifiers = len(re.findall(r'modifier\s+\w+', content))
        metrics.events = len(re.findall(r'event\s+\w+', content))

        # Security patterns
        metrics.has_reentrancy_guard = 'ReentrancyGuard' in content or 'nonReentrant' in content
        metrics.has_access_control = 'Ownable' in content or 'AccessControl' in content
        metrics.uses_safe_math = 'SafeMath' in content or metrics.solidity_version >= '0.8'

        # Check vulnerabilities
        for vuln_name, pattern in self.VULNERABILITY_PATTERNS.items():
            if re.search(pattern, content):
                metrics.vulnerabilities.append(vuln_name)

        # Gas optimization issues
        for pattern_name, pattern in self.GAS_OPTIMIZATION_PATTERNS.items():
            if re.search(pattern, content):
                metrics.gas_patterns.append(pattern_name)

        return metrics

    def _generate_report(self) -> dict:
        """Generate analysis report."""
        if not self.contracts:
            return {"message": "No Solidity contracts found"}

        total_vulns = sum(len(c.vulnerabilities) for c in self.contracts)
        with_reentrancy = sum(1 for c in self.contracts if c.has_reentrancy_guard)
        with_access = sum(1 for c in self.contracts if c.has_access_control)

        return {
            "summary": {
                "total_contracts": len(self.contracts),
                "total_functions": sum(c.functions for c in self.contracts),
                "total_vulnerabilities": total_vulns,
                "contracts_with_reentrancy_guard": with_reentrancy,
                "contracts_with_access_control": with_access,
            },
            "contracts": [
                {
                    "name": c.name,
                    "path": c.file_path,
                    "version": c.solidity_version,
                    "loc": c.lines_of_code,
                    "functions": c.functions,
                    "events": c.events,
                    "security": {
                        "reentrancy_guard": c.has_reentrancy_guard,
                        "access_control": c.has_access_control,
                    },
                    "vulnerabilities": c.vulnerabilities,
                    "gas_issues": c.gas_patterns,
                }
                for c in self.contracts
            ],
            "recommendations": self._generate_recommendations(),
        }

    def _generate_recommendations(self) -> list:
        """Generate security recommendations."""
        recommendations = []

        vuln_contracts = [c for c in self.contracts if c.vulnerabilities]
        if vuln_contracts:
            recommendations.append(
                f"Review {len(vuln_contracts)} contracts with potential vulnerabilities"
            )

        no_access = [c for c in self.contracts if not c.has_access_control and c.functions > 3]
        if no_access:
            recommendations.append(
                f"Add access control to {len(no_access)} contracts"
            )

        return recommendations


def main():
    import sys
    project_path = sys.argv[1] if len(sys.argv) > 1 else "."
    analyzer = SmartContractAnalyzer(project_path)
    report = analyzer.analyze_project()
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
