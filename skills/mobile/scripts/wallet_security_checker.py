#!/usr/bin/env python3
"""
Wallet Security Checker - Blockchain Plugin
Analyzes mobile crypto wallet security implementation.
"""

import json
import re
from pathlib import Path
from dataclasses import dataclass, field


@dataclass
class WalletSecurityAnalysis:
    """Wallet security analysis results."""
    has_biometric: bool = False
    has_secure_storage: bool = False
    has_encrypted_backup: bool = False
    has_transaction_confirmation: bool = False
    exposed_private_keys: bool = False
    security_score: int = 0
    issues: list = field(default_factory=list)


class WalletSecurityChecker:
    """Check mobile wallet security implementation."""

    def __init__(self, project_path: str):
        self.project_path = Path(project_path)

    def analyze(self) -> dict:
        """Analyze wallet security."""
        analysis = WalletSecurityAnalysis()

        source_files = list(self.project_path.rglob("*.ts"))
        source_files += list(self.project_path.rglob("*.tsx"))
        source_files += list(self.project_path.rglob("*.js"))

        for file_path in source_files:
            if 'node_modules' in str(file_path):
                continue
            try:
                content = file_path.read_text()
                self._analyze_file(content, analysis, file_path)
            except:
                pass

        analysis.security_score = self._calculate_score(analysis)

        return self._generate_report(analysis)

    def _analyze_file(self, content: str, analysis: WalletSecurityAnalysis, path: Path):
        """Analyze a single file for security patterns."""
        # Biometric authentication
        if "TouchID" in content or "FaceID" in content or "BiometricAuth" in content:
            analysis.has_biometric = True

        # Secure storage
        if "SecureStore" in content or "Keychain" in content or "EncryptedStorage" in content:
            analysis.has_secure_storage = True

        # Encrypted backup
        if "encrypt" in content.lower() and "mnemonic" in content.lower():
            analysis.has_encrypted_backup = True

        # Transaction confirmation
        if "confirm" in content.lower() and "transaction" in content.lower():
            analysis.has_transaction_confirmation = True

        # Check for exposed private keys (security issue)
        if re.search(r'privateKey\s*=\s*["\'][a-fA-F0-9]{64}', content):
            analysis.exposed_private_keys = True
            analysis.issues.append(f"Possible hardcoded private key in {path.name}")

        # Check for insecure storage
        if "AsyncStorage" in content and ("privateKey" in content or "mnemonic" in content):
            analysis.issues.append(f"Sensitive data in AsyncStorage: {path.name}")

    def _calculate_score(self, analysis: WalletSecurityAnalysis) -> int:
        """Calculate security score."""
        score = 50

        if analysis.has_biometric:
            score += 15
        if analysis.has_secure_storage:
            score += 20
        if analysis.has_encrypted_backup:
            score += 10
        if analysis.has_transaction_confirmation:
            score += 5

        # Deductions
        if analysis.exposed_private_keys:
            score -= 50
        if analysis.issues:
            score -= len(analysis.issues) * 10

        return max(0, min(100, score))

    def _generate_report(self, analysis: WalletSecurityAnalysis) -> dict:
        """Generate security report."""
        return {
            "security_features": {
                "biometric_auth": analysis.has_biometric,
                "secure_storage": analysis.has_secure_storage,
                "encrypted_backup": analysis.has_encrypted_backup,
                "transaction_confirmation": analysis.has_transaction_confirmation,
            },
            "vulnerabilities": {
                "exposed_private_keys": analysis.exposed_private_keys,
            },
            "security_score": analysis.security_score,
            "issues": analysis.issues,
            "recommendations": self._get_recommendations(analysis),
        }

    def _get_recommendations(self, analysis: WalletSecurityAnalysis) -> list:
        """Get security recommendations."""
        recs = []

        if not analysis.has_biometric:
            recs.append("Implement biometric authentication")
        if not analysis.has_secure_storage:
            recs.append("Use Keychain/SecureStore for sensitive data")
        if analysis.exposed_private_keys:
            recs.append("CRITICAL: Remove hardcoded private keys")

        return recs


def main():
    import sys
    project_path = sys.argv[1] if len(sys.argv) > 1 else "."

    checker = WalletSecurityChecker(project_path)
    report = checker.analyze()
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
