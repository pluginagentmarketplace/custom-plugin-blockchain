# Crypto Wallet Development Guide

> Blockchain Plugin - Mobile Skill Reference
> Mobile Wallet & DApp Development

## Overview

Guide for building secure mobile crypto wallets and DApps.

## Security First

### Key Storage

```typescript
// ✅ Use Secure Storage
import * as SecureStore from 'expo-secure-store';

async function storePrivateKey(key: string) {
  await SecureStore.setItemAsync('privateKey', key, {
    keychainAccessible: SecureStore.WHEN_UNLOCKED,
  });
}

// ❌ Never use AsyncStorage for keys
// AsyncStorage.setItem('privateKey', key) // INSECURE!
```

### Biometric Authentication

```typescript
import * as LocalAuthentication from 'expo-local-authentication';

async function authenticateWithBiometrics(): Promise<boolean> {
  const hasHardware = await LocalAuthentication.hasHardwareAsync();
  const isEnrolled = await LocalAuthentication.isEnrolledAsync();

  if (!hasHardware || !isEnrolled) {
    return false;
  }

  const result = await LocalAuthentication.authenticateAsync({
    promptMessage: 'Authenticate to access wallet',
    fallbackLabel: 'Use passcode',
  });

  return result.success;
}
```

## Transaction Signing

```typescript
import { ethers } from 'ethers';

async function signTransaction(
  wallet: ethers.Wallet,
  tx: ethers.TransactionRequest
) {
  // Always show confirmation to user
  const confirmed = await showTransactionConfirmation(tx);
  if (!confirmed) {
    throw new Error('User rejected transaction');
  }

  // Sign and send
  const signedTx = await wallet.signTransaction(tx);
  return signedTx;
}
```

## WalletConnect Integration

```typescript
import { useWalletConnect } from '@walletconnect/react-native-compat';

function DAppConnector() {
  const { connect, session } = useWalletConnect();

  const handleConnect = async (uri: string) => {
    await connect({ uri });
  };

  return (
    <QRScanner onScan={handleConnect} />
  );
}
```

## Security Checklist

- [ ] Store keys in Secure Enclave/Keychain
- [ ] Implement biometric authentication
- [ ] Show transaction details before signing
- [ ] Encrypt seed phrase backups
- [ ] Implement session timeouts
- [ ] Log security events

---

*Blockchain Plugin - Mobile Skill*
