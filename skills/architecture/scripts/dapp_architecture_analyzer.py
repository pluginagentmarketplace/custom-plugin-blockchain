#!/usr/bin/env python3
"""
DApp Architecture Analyzer - Blockchain Plugin
Analyzes decentralized application architecture patterns.
"""

import json
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ArchitectureAnalysis:
    """DApp architecture analysis results."""
    has_upgradeable_contracts: bool = False
    has_access_control: bool = False
    has_multisig: bool = False
    has_timelock: bool = False
    has_oracle_integration: bool = False
    has_layer2: bool = False
    contract_patterns: list = field(default_factory=list)
    security_score: int = 0
    issues: list = field(default_factory=list)


class DAppArchitectureAnalyzer:
    """Analyze DApp architecture patterns."""

    def __init__(self, project_path: str):
        self.project_path = Path(project_path)

    def analyze(self) -> dict:
        """Analyze the DApp architecture."""
        analysis = ArchitectureAnalysis()

        # Analyze smart contracts
        sol_files = list(self.project_path.rglob("*.sol"))
        for sol_file in sol_files:
            try:
                content = sol_file.read_text()
                self._analyze_contract(content, analysis)
            except:
                pass

        # Calculate security score
        analysis.security_score = self._calculate_security_score(analysis)

        return self._generate_report(analysis)

    def _analyze_contract(self, content: str, analysis: ArchitectureAnalysis):
        """Analyze contract patterns."""
        # Upgradability patterns
        if "UUPSUpgradeable" in content or "TransparentUpgradeableProxy" in content:
            analysis.has_upgradeable_contracts = True
            analysis.contract_patterns.append("upgradeable_proxy")

        if "Diamond" in content:
            analysis.contract_patterns.append("diamond_pattern")

        # Access control
        if "AccessControl" in content or "Ownable" in content:
            analysis.has_access_control = True

        # Security patterns
        if "TimelockController" in content:
            analysis.has_timelock = True

        if "Gnosis" in content or "multisig" in content.lower():
            analysis.has_multisig = True

        # Oracle integration
        if "AggregatorV3Interface" in content or "Chainlink" in content:
            analysis.has_oracle_integration = True

        # Layer 2
        if "arbitrum" in content.lower() or "optimism" in content.lower():
            analysis.has_layer2 = True

    def _calculate_security_score(self, analysis: ArchitectureAnalysis) -> int:
        """Calculate architecture security score."""
        score = 50  # Base score

        if analysis.has_access_control:
            score += 15
        if analysis.has_timelock:
            score += 15
        if analysis.has_multisig:
            score += 10
        if analysis.has_upgradeable_contracts:
            score += 5
        if not analysis.issues:
            score += 5

        return min(score, 100)

    def _generate_report(self, analysis: ArchitectureAnalysis) -> dict:
        """Generate architecture report."""
        return {
            "architecture": {
                "patterns": analysis.contract_patterns,
                "upgradeable": analysis.has_upgradeable_contracts,
                "access_control": analysis.has_access_control,
                "timelock": analysis.has_timelock,
                "multisig": analysis.has_multisig,
                "oracle": analysis.has_oracle_integration,
                "layer2": analysis.has_layer2,
            },
            "security_score": analysis.security_score,
            "issues": analysis.issues,
            "recommendations": self._get_recommendations(analysis),
        }

    def _get_recommendations(self, analysis: ArchitectureAnalysis) -> list:
        """Get architecture recommendations."""
        recs = []

        if not analysis.has_timelock:
            recs.append("Add timelock for governance actions")
        if not analysis.has_multisig:
            recs.append("Use multisig for admin operations")
        if not analysis.has_access_control:
            recs.append("Implement access control for sensitive functions")

        return recs


def main():
    import sys
    project_path = sys.argv[1] if len(sys.argv) > 1 else "."

    analyzer = DAppArchitectureAnalyzer(project_path)
    report = analyzer.analyze()
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
