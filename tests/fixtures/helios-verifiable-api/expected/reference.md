# Reference
<details><summary><code>client.<a href="src/fern/client.py">get_chain_id</a>() -> ChainIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the chain id of the network of the underlying RPC node.
### Why is this useful?
Replaces the `eth_chainId` RPC method.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.get_chain_id()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_block_information</a>(...) -> Block</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns information about a block.
### Why is this useful?
Replaces the `eth_getBlockByNumber` and `eth_getBlockByHash` RPC methods.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.get_block_information(
    block_id="earliest",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**block_id:** `BlockNumberOrTagOrHash` 
    
</dd>
</dl>

<dl>
<dd>

**transaction_detail_flag:** `typing.Optional[bool]` — A flag indicating whether to include full transaction details or just the hashes.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_block_receipts</a>(...) -> BlockReceiptsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all transaction receipts for a given block.
### Why is this useful?
Replaces the `eth_getBlockReceipts` RPC method.
### How to verify response?
- RLP encode each receipt and keccak-256 hash these encoded receipts.
- Construct a Merkle Patricia Trie (MPT) from these hashes.
- Verify the root of the constructed MPT against the trusted block's receipt root.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.get_block_receipts(
    block_id="earliest",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**block_id:** `BlockNumberOrTagOrHash` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">send_raw_transaction</a>(...) -> SendRawTxResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new message call transaction or a contract creation for signed transactions.
### Why is this useful?
Replaces the `eth_sendRawTransaction` RPC method.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.send_raw_transaction()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**bytes:** `typing.Optional[Bytes]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">create_new_filter</a>(...) -> NewFilterResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a filter in the node, to notify when the state changes.

State changes can be of three types: logs, new blocks and pending transactions.

To check if the state has changed, query `/filterChanges/{filterId}`.
### Why is this useful?
Replaces the `eth_newFilter`, `eth_newBlockFilter` and `eth_newPendingTransactionFilter` RPC methods.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.create_new_filter()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**kind:** `typing.Optional[NewFilterRequestKind]` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[Filter]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">uninstall_a_filter</a>(...) -> UninstallFilterResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Uninstalls a filter with given id.
### Why is this useful?
Replaces the `eth_uninstallFilter` RPC method.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.uninstall_a_filter(
    filter_id="filterId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**filter_id:** `Uint` — Filter identifier
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Verifiable
<details><summary><code>client.verifiable.<a href="src/fern/verifiable/client.py">get_account_information</a>(...) -> AccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns information about an address along with its EIP-1186 account proof.
### Why is this useful?
Replaces the `eth_getProof`, `eth_getTransactionCount`, `eth_getBalance`, `eth_getCode`, and `eth_getStorageAt` RPC methods.
### How to verify response?
- RLP encode the `TrieAccount` struct and keccak-256 hash it.
- Verify the given `accountProof` against the trusted block's state root using the address as the key (path) and the hashed account as the value (leaf).
- For each item in `storageProof`, verify the given leaf’s Merkle Proof against the `storageHash`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.verifiable.get_account_information(
    address="address",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**address:** `Address` — The address of the account.
    
</dd>
</dl>

<dl>
<dd>

**include_code:** `typing.Optional[bool]` — A flag indicating whether to include the account's code.
    
</dd>
</dl>

<dl>
<dd>

**storage_slots:** `typing.Optional[typing.Union[BytesMax32, typing.Sequence[BytesMax32]]]` — A list of storage positions (in hex) to include in the proof.
    
</dd>
</dl>

<dl>
<dd>

**block:** `typing.Optional[BlockNumberOrTagOrHash]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.verifiable.<a href="src/fern/verifiable/client.py">get_transaction_receipt</a>(...) -> TransactionReceiptResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the receipt of a transaction along with a Merkle Proof of its inclusion.
### Why is this useful?
Replaces the `eth_getTransactionReceipt` RPC method.
### How to verify response?
- RLP encode the given receipt and keccak-256 hash it.
- Verify the given `receiptProof` against the trusted block's receipt root with the given receipt's hash as the leaf.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.verifiable.get_transaction_receipt(
    tx_hash="txHash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tx_hash:** `Hash32` — The hash of the transaction.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.verifiable.<a href="src/fern/verifiable/client.py">get_logs</a>(...) -> LogsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an array of all logs matching the given filter object.
Corresponding to each log, it also returns the transaction receipt and a Merkle Proof of its inclusion.
### Why is this useful?
Replaces the `eth_getLogs` RPC method.
### How to verify response?
For each log:
- Find the corresponding transaction receipt for the log from the `receiptProofs` field. Let’s call this `receipt`.
- Ensure that this log entry is included in the `receipt.logs` array.
- RLP encode the `receipt` and keccak-256 hash it.
- Verify the given `receiptProof` against the trusted block's receipt root with the given receipt's hash as the leaf.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.verifiable.get_logs()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**from_block:** `typing.Optional[Uint]` — Starting block number or tag.
    
</dd>
</dl>

<dl>
<dd>

**to_block:** `typing.Optional[Uint]` — Ending block number or tag.
    
</dd>
</dl>

<dl>
<dd>

**block_hash:** `typing.Optional[Hash32]` — Block hash. If present, fromBlock and toBlock are not allowed.
    
</dd>
</dl>

<dl>
<dd>

**address:** `typing.Optional[GetEthV1ProofLogsRequestAddress]` — Contract address or a list of addresses from which logs should originate.
    
</dd>
</dl>

<dl>
<dd>

**topic0:** `typing.Optional[FilterTopic]` — 32 Bytes DATA topic(s).
    
</dd>
</dl>

<dl>
<dd>

**topic1:** `typing.Optional[FilterTopic]` — 32 Bytes DATA topic(s).
    
</dd>
</dl>

<dl>
<dd>

**topic2:** `typing.Optional[FilterTopic]` — 32 Bytes DATA topic(s).
    
</dd>
</dl>

<dl>
<dd>

**topic3:** `typing.Optional[FilterTopic]` — 32 Bytes DATA topic(s).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.verifiable.<a href="src/fern/verifiable/client.py">get_filter_logs</a>(...) -> FilterLogsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an array of all logs matching the filter with given id.
Corresponding to each log, it also returns the transaction receipt and a Merkle Proof of its inclusion.
### Why is this useful?
Replaces the `eth_getFilterLogs` RPC method.
### How to verify response?
For each log:
- Find the corresponding transaction receipt for the log from the `receiptProofs` field. Let’s call this `receipt`.
- Ensure that this log entry is included in the `receipt.logs` array.
- RLP encode the `receipt` and keccak-256 hash it.
- Verify the given `receiptProof` against the trusted block's receipt root with the given receipt's hash as the leaf.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.verifiable.get_filter_logs(
    filter_id="filterId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**filter_id:** `Uint` — Filter identifier
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.verifiable.<a href="src/fern/verifiable/client.py">get_filter_changes</a>(...) -> FilterChangesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the changes since the last poll for a given filter id. If filter is of logs type, then corresponding to each log, it also returns the transaction receipt and a Merkle Proof of its inclusion.
### Why is this useful?
Replaces the `eth_getFilterChanges` RPC method.
### How to verify response?
> Note: Only applicable for filters of logs type.

For each log:
- Find the corresponding transaction receipt for the log from the `receiptProofs` field. Let’s call this `receipt`.
- Ensure that this log entry is included in the `receipt.logs` array.
- RLP encode the `receipt` and keccak-256 hash it.
- Verify the given `receiptProof` against the trusted block's receipt root with the given receipt's hash as the leaf
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.verifiable.get_filter_changes(
    filter_id="filterId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**filter_id:** `Uint` — Filter identifier
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.verifiable.<a href="src/fern/verifiable/client.py">create_extended_access_list</a>(...) -> ExtendedAccessListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all addresses and storage keys (along with their EIP-1186 proofs) that are accessed by a given transaction.

It's an extended list because it includes the `from`, `to` and `block.beneficiary` addresses as well.
### Why is this useful?
Replaces the `eth_createAccessList` RPC method.
### How to verify response?
For each account:
- RLP encode the `TrieAccount` struct and keccak-256 hash it.
- Verify the given `accountProof` against the trusted block's state root using the address as the key (path) and the hashed account as the value (leaf).
- For each item in `storageProof`: verify the given leaf’s Merkle Proof against the `storageHash`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.verifiable.create_extended_access_list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tx:** `typing.Optional[GenericTransaction]` 
    
</dd>
</dl>

<dl>
<dd>

**validate_tx:** `typing.Optional[bool]` — A flag indicating whether to validate the transaction (such as enforcing gas limit).
    
</dd>
</dl>

<dl>
<dd>

**block:** `typing.Optional[BlockNumberOrTagOrHash]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

