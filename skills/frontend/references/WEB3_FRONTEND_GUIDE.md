# Web3 Frontend Development Guide

> Blockchain Plugin - Frontend Skill Reference
> DApp & Web3 Frontend Development

## Overview

Guide for building decentralized application (DApp) frontends with Web3 integration, wallet connections, and smart contract interactions.

## Table of Contents

1. [Wallet Connection](#wallet-connection)
2. [Contract Interaction](#contract-interaction)
3. [Transaction Handling](#transaction-handling)
4. [Best Practices](#best-practices)

---

## Wallet Connection

### Using wagmi + RainbowKit

```tsx
// providers/Web3Provider.tsx
import { WagmiConfig, createConfig, configureChains } from 'wagmi';
import { mainnet, polygon, sepolia } from 'wagmi/chains';
import { RainbowKitProvider, getDefaultWallets } from '@rainbow-me/rainbowkit';
import { alchemyProvider } from 'wagmi/providers/alchemy';
import { publicProvider } from 'wagmi/providers/public';

const { chains, publicClient } = configureChains(
  [mainnet, polygon, sepolia],
  [
    alchemyProvider({ apiKey: process.env.VITE_ALCHEMY_API_KEY! }),
    publicProvider(),
  ]
);

const { connectors } = getDefaultWallets({
  appName: 'My DApp',
  projectId: process.env.VITE_WALLET_CONNECT_PROJECT_ID!,
  chains,
});

const config = createConfig({
  autoConnect: true,
  connectors,
  publicClient,
});

export function Web3Provider({ children }: { children: React.ReactNode }) {
  return (
    <WagmiConfig config={config}>
      <RainbowKitProvider chains={chains}>
        {children}
      </RainbowKitProvider>
    </WagmiConfig>
  );
}
```

### Connect Button Component

```tsx
// components/ConnectButton.tsx
import { useAccount, useConnect, useDisconnect } from 'wagmi';

export function WalletButton() {
  const { address, isConnected } = useAccount();
  const { connect, connectors, isPending } = useConnect();
  const { disconnect } = useDisconnect();

  if (isConnected) {
    return (
      <div>
        <span>{address?.slice(0, 6)}...{address?.slice(-4)}</span>
        <button onClick={() => disconnect()}>Disconnect</button>
      </div>
    );
  }

  return (
    <div>
      {connectors.map((connector) => (
        <button
          key={connector.id}
          onClick={() => connect({ connector })}
          disabled={isPending}
        >
          Connect {connector.name}
        </button>
      ))}
    </div>
  );
}
```

---

## Contract Interaction

### Reading Contract Data

```tsx
import { useContractRead } from 'wagmi';
import { erc20ABI } from 'wagmi';

function TokenBalance({ tokenAddress, userAddress }) {
  const { data: balance, isLoading, isError } = useContractRead({
    address: tokenAddress,
    abi: erc20ABI,
    functionName: 'balanceOf',
    args: [userAddress],
    watch: true,
  });

  if (isLoading) return <span>Loading...</span>;
  if (isError) return <span>Error fetching balance</span>;

  return <span>{formatUnits(balance, 18)} tokens</span>;
}
```

### Writing to Contracts

```tsx
import { usePrepareContractWrite, useContractWrite, useWaitForTransaction } from 'wagmi';
import { parseEther } from 'viem';

function TransferToken({ tokenAddress }) {
  const [to, setTo] = useState('');
  const [amount, setAmount] = useState('');

  const { config, error: prepareError } = usePrepareContractWrite({
    address: tokenAddress,
    abi: erc20ABI,
    functionName: 'transfer',
    args: [to, parseEther(amount || '0')],
    enabled: Boolean(to && amount),
  });

  const { write, data, isLoading: isWriting } = useContractWrite(config);

  const { isLoading: isConfirming, isSuccess } = useWaitForTransaction({
    hash: data?.hash,
  });

  return (
    <form onSubmit={(e) => { e.preventDefault(); write?.(); }}>
      <input
        placeholder="Recipient address"
        value={to}
        onChange={(e) => setTo(e.target.value)}
      />
      <input
        placeholder="Amount"
        value={amount}
        onChange={(e) => setAmount(e.target.value)}
      />
      <button disabled={!write || isWriting || isConfirming}>
        {isWriting ? 'Signing...' : isConfirming ? 'Confirming...' : 'Transfer'}
      </button>
      {isSuccess && <p>Transaction confirmed!</p>}
      {prepareError && <p>Error: {prepareError.message}</p>}
    </form>
  );
}
```

---

## Transaction Handling

### Transaction Status Component

```tsx
function TransactionStatus({ hash }: { hash: `0x${string}` }) {
  const { data, isError, isLoading } = useWaitForTransaction({
    hash,
    confirmations: 2,
  });

  if (isLoading) {
    return (
      <div className="pending">
        <Spinner />
        <span>Waiting for confirmation...</span>
        <a href={`https://etherscan.io/tx/${hash}`} target="_blank">
          View on Etherscan
        </a>
      </div>
    );
  }

  if (isError) {
    return <div className="error">Transaction failed</div>;
  }

  return (
    <div className="success">
      Transaction confirmed in block {data?.blockNumber}
    </div>
  );
}
```

---

## Best Practices

### Security Checklist

- [ ] Never store private keys in frontend code
- [ ] Validate addresses before transactions
- [ ] Show transaction details before signing
- [ ] Handle network switching gracefully
- [ ] Display gas estimates to users
- [ ] Implement proper error messages

### UX Patterns

```tsx
// Good: Show pending state and allow cancellation
<button disabled={isPending}>
  {isPending ? (
    <>
      <Spinner /> Check wallet...
    </>
  ) : (
    'Approve'
  )}
</button>

// Good: Display formatted addresses
<span title={fullAddress}>
  {address.slice(0, 6)}...{address.slice(-4)}
</span>

// Good: Link to block explorer
<a href={`${explorerUrl}/tx/${hash}`} target="_blank">
  View transaction ↗
</a>
```

---

## Resources

- [wagmi Documentation](https://wagmi.sh)
- [RainbowKit](https://rainbowkit.com)
- [viem](https://viem.sh)
- [Ethers.js](https://docs.ethers.org)

---

*Blockchain Plugin - Frontend Skill*
