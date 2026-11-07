# Reference
## Accounts
<details><summary><code>client.accounts.<a href="src/fern/accounts/client.py">list</a>(...) -> AccountsListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List every appearance of an address anywhere on the chain. Corresponds to the <a href="/chifra/accounts/#chifra-list">chifra list</a> command line.
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.accounts.list(
    addrs=[
        "addrs"
    ],
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

**addrs:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — one or more addresses (0x...) to list
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[bool]` — display only the count of records for each monitor
    
</dd>
</dl>

<dl>
<dd>

**no_zero:** `typing.Optional[bool]` — for the --count option only, suppress the display of zero appearance accounts
    
</dd>
</dl>

<dl>
<dd>

**bounds:** `typing.Optional[bool]` — report first and last block this address appears
    
</dd>
</dl>

<dl>
<dd>

**unripe:** `typing.Optional[bool]` — list transactions labeled unripe (i.e. less than 28 blocks old)
    
</dd>
</dl>

<dl>
<dd>

**silent:** `typing.Optional[bool]` — freshen the monitor only (no reporting)
    
</dd>
</dl>

<dl>
<dd>

**first_record:** `typing.Optional[int]` — the first record to process
    
</dd>
</dl>

<dl>
<dd>

**max_records:** `typing.Optional[int]` — the maximum number of records to process
    
</dd>
</dl>

<dl>
<dd>

**reversed:** `typing.Optional[bool]` — produce results in reverse chronological order
    
</dd>
</dl>

<dl>
<dd>

**first_block:** `typing.Optional[float]` — first block to export (inclusive, ignored when freshening)
    
</dd>
</dl>

<dl>
<dd>

**last_block:** `typing.Optional[float]` — last block to export (inclusive, ignored when freshening)
    
</dd>
</dl>

<dl>
<dd>

**chain:** `typing.Optional[str]` — the chain to use
    
</dd>
</dl>

<dl>
<dd>

**no_header:** `typing.Optional[bool]` — suppress the header in the output
    
</dd>
</dl>

<dl>
<dd>

**fmt:** `typing.Optional[str]` — export format, one of [ txt | csv | json ]
    
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

<details><summary><code>client.accounts.<a href="src/fern/accounts/client.py">export</a>(...) -> AccountsExportResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Export full details of transactions for one or more addresses. Corresponds to the <a href="/chifra/accounts/#chifra-export">chifra export</a> command line.
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.accounts.export(
    addrs=[
        "addrs"
    ],
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

**addrs:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — one or more addresses (0x...) to export
    
</dd>
</dl>

<dl>
<dd>

**topics:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — filter by one or more log topics (only for --logs option)
    
</dd>
</dl>

<dl>
<dd>

**fourbytes:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — filter by one or more fourbytes (only for transactions and trace options)
    
</dd>
</dl>

<dl>
<dd>

**appearances:** `typing.Optional[bool]` — export a list of appearances
    
</dd>
</dl>

<dl>
<dd>

**receipts:** `typing.Optional[bool]` — export receipts instead of transactional data
    
</dd>
</dl>

<dl>
<dd>

**logs:** `typing.Optional[bool]` — export logs instead of transactional data
    
</dd>
</dl>

<dl>
<dd>

**approvals:** `typing.Optional[bool]` — export all token approval transactions for the given address
    
</dd>
</dl>

<dl>
<dd>

**traces:** `typing.Optional[bool]` — export traces instead of transactional data
    
</dd>
</dl>

<dl>
<dd>

**neighbors:** `typing.Optional[bool]` — export the neighbors of the given address
    
</dd>
</dl>

<dl>
<dd>

**statements:** `typing.Optional[bool]` — export only statements
    
</dd>
</dl>

<dl>
<dd>

**transfers:** `typing.Optional[bool]` — export only eth or token transfers
    
</dd>
</dl>

<dl>
<dd>

**assets:** `typing.Optional[bool]` — list all assets (with names) that appear in any transfer
    
</dd>
</dl>

<dl>
<dd>

**balances:** `typing.Optional[bool]` — traverse the transaction history and show each change in ETH balances
    
</dd>
</dl>

<dl>
<dd>

**withdrawals:** `typing.Optional[bool]` — export withdrawals for the given address
    
</dd>
</dl>

<dl>
<dd>

**articulate:** `typing.Optional[bool]` — articulate transactions, traces, logs, and outputs
    
</dd>
</dl>

<dl>
<dd>

**cache_traces:** `typing.Optional[bool]` — force the transaction's traces into the cache
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[bool]` — for --appearances mode only, display only the count of records
    
</dd>
</dl>

<dl>
<dd>

**first_record:** `typing.Optional[int]` — the first record to process
    
</dd>
</dl>

<dl>
<dd>

**max_records:** `typing.Optional[int]` — the maximum number of records to process
    
</dd>
</dl>

<dl>
<dd>

**relevant:** `typing.Optional[bool]` — for log and accounting export only, export only logs relevant to one of the given export addresses
    
</dd>
</dl>

<dl>
<dd>

**emitter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — for the --logs option only, filter logs to show only those logs emitted by the given address(es)
    
</dd>
</dl>

<dl>
<dd>

**topic:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — for the --logs option only, filter logs to show only those with this topic(s)
    
</dd>
</dl>

<dl>
<dd>

**nfts:** `typing.Optional[bool]` — for the --logs option only, filter logs to show only nft transfers
    
</dd>
</dl>

<dl>
<dd>

**reverted:** `typing.Optional[bool]` — export only transactions that were reverted
    
</dd>
</dl>

<dl>
<dd>

**asset:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — export transfers, balances, or statements only for this asset
    
</dd>
</dl>

<dl>
<dd>

**flow:** `typing.Optional[AccountsExportRequestFlow]` — export transfers, balances, or statements with incoming, outgoing, or zero value
    
</dd>
</dl>

<dl>
<dd>

**factory:** `typing.Optional[bool]` — for --traces only, report addresses created by (or self-destructed by) the given address(es)
    
</dd>
</dl>

<dl>
<dd>

**unripe:** `typing.Optional[bool]` — export transactions labeled unripe (i.e. less than 28 blocks old)
    
</dd>
</dl>

<dl>
<dd>

**reversed:** `typing.Optional[bool]` — produce results in reverse chronological order
    
</dd>
</dl>

<dl>
<dd>

**no_zero:** `typing.Optional[bool]` — for the --count option only, suppress the display of zero appearance accounts
    
</dd>
</dl>

<dl>
<dd>

**first_block:** `typing.Optional[float]` — first block to process (inclusive)
    
</dd>
</dl>

<dl>
<dd>

**last_block:** `typing.Optional[float]` — last block to process (inclusive)
    
</dd>
</dl>

<dl>
<dd>

**accounting:** `typing.Optional[bool]` — deprecated option, you may simply remove it
    
</dd>
</dl>

<dl>
<dd>

**chain:** `typing.Optional[str]` — the chain to use
    
</dd>
</dl>

<dl>
<dd>

**no_header:** `typing.Optional[bool]` — suppress the header in the output
    
</dd>
</dl>

<dl>
<dd>

**cache:** `typing.Optional[bool]` — force the results of the query into the cache
    
</dd>
</dl>

<dl>
<dd>

**decache:** `typing.Optional[bool]` — removes related items from the cache
    
</dd>
</dl>

<dl>
<dd>

**ether:** `typing.Optional[bool]` — export values in ether
    
</dd>
</dl>

<dl>
<dd>

**fmt:** `typing.Optional[str]` — export format, one of [ txt | csv | json ]
    
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

<details><summary><code>client.accounts.<a href="src/fern/accounts/client.py">monitors</a>(...) -> AccountsMonitorsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add, remove, clean, and list address monitors. Corresponds to the <a href="/chifra/accounts/#chifra-monitors">chifra monitors</a> command line.
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.accounts.monitors()

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

**addrs:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — one or more addresses (0x...) to process
    
</dd>
</dl>

<dl>
<dd>

**delete:** `typing.Optional[bool]` — delete a monitor, but do not remove it
    
</dd>
</dl>

<dl>
<dd>

**undelete:** `typing.Optional[bool]` — undelete a previously deleted monitor
    
</dd>
</dl>

<dl>
<dd>

**remove:** `typing.Optional[bool]` — remove a previously deleted monitor
    
</dd>
</dl>

<dl>
<dd>

**clean:** `typing.Optional[bool]` — clean (i.e. remove duplicate appearances) from monitors, optionally clear stage
    
</dd>
</dl>

<dl>
<dd>

**list:** `typing.Optional[bool]` — list monitors in the cache (--verbose for more detail)
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[bool]` — show the number of active monitors (included deleted but not removed monitors)
    
</dd>
</dl>

<dl>
<dd>

**staged:** `typing.Optional[bool]` — for --clean, --list, and --count options only, include staged monitors
    
</dd>
</dl>

<dl>
<dd>

**chain:** `typing.Optional[str]` — the chain to use
    
</dd>
</dl>

<dl>
<dd>

**no_header:** `typing.Optional[bool]` — suppress the header in the output
    
</dd>
</dl>

<dl>
<dd>

**cache:** `typing.Optional[bool]` — force the results of the query into the cache
    
</dd>
</dl>

<dl>
<dd>

**decache:** `typing.Optional[bool]` — removes related items from the cache
    
</dd>
</dl>

<dl>
<dd>

**fmt:** `typing.Optional[str]` — export format, one of [ txt | csv | json ]
    
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

<details><summary><code>client.accounts.<a href="src/fern/accounts/client.py">names</a>(...) -> AccountsNamesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Query addresses or names of well-known accounts. Corresponds to the <a href="/chifra/accounts/#chifra-names">chifra names</a> command line.
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.accounts.names(
    terms=[
        "terms"
    ],
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

**terms:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — a space separated list of one or more search terms
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[bool]` — expand search to include all fields (search name, address, and symbol otherwise)
    
</dd>
</dl>

<dl>
<dd>

**match_case:** `typing.Optional[bool]` — do case-sensitive search
    
</dd>
</dl>

<dl>
<dd>

**all:** `typing.Optional[bool]` — include all (including custom) names in the search
    
</dd>
</dl>

<dl>
<dd>

**custom:** `typing.Optional[bool]` — include only custom named accounts in the search
    
</dd>
</dl>

<dl>
<dd>

**prefund:** `typing.Optional[bool]` — include prefund accounts in the search
    
</dd>
</dl>

<dl>
<dd>

**addr:** `typing.Optional[bool]` — display only addresses in the results (useful for scripting, assumes --no_header)
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[bool]` — export the list of tags and subtags only
    
</dd>
</dl>

<dl>
<dd>

**clean:** `typing.Optional[bool]` — clean the data (addrs to lower case, sort by addr)
    
</dd>
</dl>

<dl>
<dd>

**regular:** `typing.Optional[bool]` — only available with --clean, cleans regular names database
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[bool]` — return the number of names matching the search terms or other options
    
</dd>
</dl>

<dl>
<dd>

**dry_run:** `typing.Optional[bool]` — only available with --clean or --autoname, outputs changes to stdout instead of updating databases
    
</dd>
</dl>

<dl>
<dd>

**autoname:** `typing.Optional[str]` — an address assumed to be a token, added automatically to names database if true
    
</dd>
</dl>

<dl>
<dd>

**create:** `typing.Optional[str]` — create a new item
    
</dd>
</dl>

<dl>
<dd>

**update:** `typing.Optional[str]` — update an existing item
    
</dd>
</dl>

<dl>
<dd>

**delete:** `typing.Optional[str]` — delete the item, but do not remove it
    
</dd>
</dl>

<dl>
<dd>

**undelete:** `typing.Optional[str]` — undelete a previously deleted item
    
</dd>
</dl>

<dl>
<dd>

**remove:** `typing.Optional[str]` — remove a previously deleted item
    
</dd>
</dl>

<dl>
<dd>

**chain:** `typing.Optional[str]` — the chain to use
    
</dd>
</dl>

<dl>
<dd>

**no_header:** `typing.Optional[bool]` — suppress the header in the output
    
</dd>
</dl>

<dl>
<dd>

**fmt:** `typing.Optional[str]` — export format, one of [ txt | csv | json ]
    
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

<details><summary><code>client.accounts.<a href="src/fern/accounts/client.py">abis</a>(...) -> AccountsAbisResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches the ABI for a smart contract. Corresponds to the <a href="/chifra/accounts/#chifra-abis">chifra abis</a> command line.
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.accounts.abis(
    addrs=[
        "addrs"
    ],
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

**addrs:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — a list of one or more smart contracts whose ABIs to display
    
</dd>
</dl>

<dl>
<dd>

**known:** `typing.Optional[bool]` — load common 'known' ABIs from cache
    
</dd>
</dl>

<dl>
<dd>

**proxy_for:** `typing.Optional[str]` — redirects the query to this implementation
    
</dd>
</dl>

<dl>
<dd>

**list:** `typing.Optional[bool]` — a list of downloaded abi files
    
</dd>
</dl>

<dl>
<dd>

**details:** `typing.Optional[bool]` — show the functions and events instead of summaries for all abi files
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[bool]` — show the number of abis downloaded
    
</dd>
</dl>

<dl>
<dd>

**find:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — search for function or event declarations given a four- or 32-byte code(s)
    
</dd>
</dl>

<dl>
<dd>

**hint:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — for the --find option only, provide hints to speed up the search
    
</dd>
</dl>

<dl>
<dd>

**encode:** `typing.Optional[str]` — generate the 32-byte encoding for a given canonical function or event signature
    
</dd>
</dl>

<dl>
<dd>

**chain:** `typing.Optional[str]` — the chain to use
    
</dd>
</dl>

<dl>
<dd>

**no_header:** `typing.Optional[bool]` — suppress the header in the output
    
</dd>
</dl>

<dl>
<dd>

**cache:** `typing.Optional[bool]` — force the results of the query into the cache
    
</dd>
</dl>

<dl>
<dd>

**decache:** `typing.Optional[bool]` — removes related items from the cache
    
</dd>
</dl>

<dl>
<dd>

**fmt:** `typing.Optional[str]` — export format, one of [ txt | csv | json ]
    
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

## Chain Data
<details><summary><code>client.chain_data.<a href="src/fern/chain_data/client.py">chaindata_blocks</a>(...) -> ChaindataBlocksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve one or more blocks from the chain or local cache. Corresponds to the <a href="/chifra/chaindata/#chifra-blocks">chifra blocks</a> command line.
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.chain_data.chaindata_blocks(
    blocks=[
        "blocks"
    ],
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

**blocks:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — a space-separated list of one or more block identifiers
    
</dd>
</dl>

<dl>
<dd>

**hashes:** `typing.Optional[bool]` — display only transaction hashes, default is to display full transaction detail
    
</dd>
</dl>

<dl>
<dd>

**uncles:** `typing.Optional[bool]` — display uncle blocks (if any) instead of the requested block
    
</dd>
</dl>

<dl>
<dd>

**traces:** `typing.Optional[bool]` — export the traces from the block as opposed to the block data
    
</dd>
</dl>

<dl>
<dd>

**uniq:** `typing.Optional[bool]` — display a list of uniq address appearances per transaction
    
</dd>
</dl>

<dl>
<dd>

**flow:** `typing.Optional[ChaindataBlocksRequestFlow]` — for the --uniq option only, export only from or to (including trace from or to)
    
</dd>
</dl>

<dl>
<dd>

**logs:** `typing.Optional[bool]` — display only the logs found in the block(s)
    
</dd>
</dl>

<dl>
<dd>

**emitter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — for the --logs option only, filter logs to show only those logs emitted by the given address(es)
    
</dd>
</dl>

<dl>
<dd>

**topic:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — for the --logs option only, filter logs to show only those with this topic(s)
    
</dd>
</dl>

<dl>
<dd>

**withdrawals:** `typing.Optional[bool]` — export the withdrawals from the block as opposed to the block data
    
</dd>
</dl>

<dl>
<dd>

**articulate:** `typing.Optional[bool]` — for the --logs option only, articulate the retrieved data if ABIs can be found
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[bool]` — display only the count of appearances for --addrs or --uniq
    
</dd>
</dl>

<dl>
<dd>

**cache_txs:** `typing.Optional[bool]` — force a write of the block's transactions to the cache (slow)
    
</dd>
</dl>

<dl>
<dd>

**cache_traces:** `typing.Optional[bool]` — force a write of the block's traces to the cache (slower)
    
</dd>
</dl>

<dl>
<dd>

**chain:** `typing.Optional[str]` — the chain to use
    
</dd>
</dl>

<dl>
<dd>

**no_header:** `typing.Optional[bool]` — suppress the header in the output
    
</dd>
</dl>

<dl>
<dd>

**cache:** `typing.Optional[bool]` — force the results of the query into the cache
    
</dd>
</dl>

<dl>
<dd>

**decache:** `typing.Optional[bool]` — removes related items from the cache
    
</dd>
</dl>

<dl>
<dd>

**ether:** `typing.Optional[bool]` — export values in ether
    
</dd>
</dl>

<dl>
<dd>

**fmt:** `typing.Optional[str]` — export format, one of [ txt | csv | json ]
    
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

<details><summary><code>client.chain_data.<a href="src/fern/chain_data/client.py">chaindata_transactions</a>(...) -> ChaindataTransactionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve one or more transactions from the chain or local cache. Corresponds to the <a href="/chifra/chaindata/#chifra-transactions">chifra transactions</a> command line.
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.chain_data.chaindata_transactions(
    transactions=[
        "transactions"
    ],
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

**transactions:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — a space-separated list of one or more transaction identifiers
    
</dd>
</dl>

<dl>
<dd>

**articulate:** `typing.Optional[bool]` — articulate the retrieved data if ABIs can be found
    
</dd>
</dl>

<dl>
<dd>

**traces:** `typing.Optional[bool]` — include the transaction's traces in the results
    
</dd>
</dl>

<dl>
<dd>

**uniq:** `typing.Optional[bool]` — display a list of uniq addresses found in the transaction
    
</dd>
</dl>

<dl>
<dd>

**flow:** `typing.Optional[ChaindataTransactionsRequestFlow]` — for the uniq option only, export only from or to (including trace from or to)
    
</dd>
</dl>

<dl>
<dd>

**logs:** `typing.Optional[bool]` — display only the logs found in the transaction(s)
    
</dd>
</dl>

<dl>
<dd>

**emitter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — for the --logs option only, filter logs to show only those logs emitted by the given address(es)
    
</dd>
</dl>

<dl>
<dd>

**topic:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — for the --logs option only, filter logs to show only those with this topic(s)
    
</dd>
</dl>

<dl>
<dd>

**cache_traces:** `typing.Optional[bool]` — force the transaction's traces into the cache
    
</dd>
</dl>

<dl>
<dd>

**chain:** `typing.Optional[str]` — the chain to use
    
</dd>
</dl>

<dl>
<dd>

**no_header:** `typing.Optional[bool]` — suppress the header in the output
    
</dd>
</dl>

<dl>
<dd>

**cache:** `typing.Optional[bool]` — force the results of the query into the cache
    
</dd>
</dl>

<dl>
<dd>

**decache:** `typing.Optional[bool]` — removes related items from the cache
    
</dd>
</dl>

<dl>
<dd>

**ether:** `typing.Optional[bool]` — export values in ether
    
</dd>
</dl>

<dl>
<dd>

**fmt:** `typing.Optional[str]` — export format, one of [ txt | csv | json ]
    
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

<details><summary><code>client.chain_data.<a href="src/fern/chain_data/client.py">chaindata_receipts</a>(...) -> ChaindataReceiptsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve receipts for the given transaction(s). Corresponds to the <a href="/chifra/chaindata/#chifra-receipts">chifra receipts</a> command line.
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.chain_data.chaindata_receipts(
    transactions=[
        "transactions"
    ],
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

**transactions:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — a space-separated list of one or more transaction identifiers
    
</dd>
</dl>

<dl>
<dd>

**articulate:** `typing.Optional[bool]` — articulate the retrieved data if ABIs can be found
    
</dd>
</dl>

<dl>
<dd>

**chain:** `typing.Optional[str]` — the chain to use
    
</dd>
</dl>

<dl>
<dd>

**no_header:** `typing.Optional[bool]` — suppress the header in the output
    
</dd>
</dl>

<dl>
<dd>

**cache:** `typing.Optional[bool]` — force the results of the query into the cache
    
</dd>
</dl>

<dl>
<dd>

**decache:** `typing.Optional[bool]` — removes related items from the cache
    
</dd>
</dl>

<dl>
<dd>

**fmt:** `typing.Optional[str]` — export format, one of [ txt | csv | json ]
    
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

<details><summary><code>client.chain_data.<a href="src/fern/chain_data/client.py">chaindata_logs</a>(...) -> ChaindataLogsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve logs for the given transaction(s). Corresponds to the <a href="/chifra/chaindata/#chifra-logs">chifra logs</a> command line.
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.chain_data.chaindata_logs(
    transactions=[
        "transactions"
    ],
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

**transactions:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — a space-separated list of one or more transaction identifiers
    
</dd>
</dl>

<dl>
<dd>

**emitter:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — filter logs to show only those logs emitted by the given address(es)
    
</dd>
</dl>

<dl>
<dd>

**topic:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — filter logs to show only those with this topic(s)
    
</dd>
</dl>

<dl>
<dd>

**articulate:** `typing.Optional[bool]` — articulate the retrieved data if ABIs can be found
    
</dd>
</dl>

<dl>
<dd>

**chain:** `typing.Optional[str]` — the chain to use
    
</dd>
</dl>

<dl>
<dd>

**no_header:** `typing.Optional[bool]` — suppress the header in the output
    
</dd>
</dl>

<dl>
<dd>

**cache:** `typing.Optional[bool]` — force the results of the query into the cache
    
</dd>
</dl>

<dl>
<dd>

**decache:** `typing.Optional[bool]` — removes related items from the cache
    
</dd>
</dl>

<dl>
<dd>

**fmt:** `typing.Optional[str]` — export format, one of [ txt | csv | json ]
    
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

<details><summary><code>client.chain_data.<a href="src/fern/chain_data/client.py">chaindata_traces</a>(...) -> ChaindataTracesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve traces for the given transaction(s). Corresponds to the <a href="/chifra/chaindata/#chifra-traces">chifra traces</a> command line.
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.chain_data.chaindata_traces(
    transactions=[
        "transactions"
    ],
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

**transactions:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — a space-separated list of one or more transaction identifiers
    
</dd>
</dl>

<dl>
<dd>

**articulate:** `typing.Optional[bool]` — articulate the retrieved data if ABIs can be found
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[str]` — call the node's trace_filter routine with bang-separated filter
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[bool]` — display only the number of traces for the transaction (fast)
    
</dd>
</dl>

<dl>
<dd>

**chain:** `typing.Optional[str]` — the chain to use
    
</dd>
</dl>

<dl>
<dd>

**no_header:** `typing.Optional[bool]` — suppress the header in the output
    
</dd>
</dl>

<dl>
<dd>

**cache:** `typing.Optional[bool]` — force the results of the query into the cache
    
</dd>
</dl>

<dl>
<dd>

**decache:** `typing.Optional[bool]` — removes related items from the cache
    
</dd>
</dl>

<dl>
<dd>

**ether:** `typing.Optional[bool]` — export values in ether
    
</dd>
</dl>

<dl>
<dd>

**fmt:** `typing.Optional[str]` — export format, one of [ txt | csv | json ]
    
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

<details><summary><code>client.chain_data.<a href="src/fern/chain_data/client.py">chaindata_when</a>(...) -> ChaindataWhenResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Find block(s) based on date, blockNum, timestamp, or 'special'. Corresponds to the <a href="/chifra/chaindata/#chifra-when">chifra when</a> command line.
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.chain_data.chaindata_when()

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

**blocks:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — one or more dates, block numbers, hashes, or special named blocks (see notes)
    
</dd>
</dl>

<dl>
<dd>

**list:** `typing.Optional[bool]` — export a list of the 'special' blocks
    
</dd>
</dl>

<dl>
<dd>

**timestamps:** `typing.Optional[bool]` — display or process timestamps
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[bool]` — with --timestamps only, returns the number of timestamps in the cache
    
</dd>
</dl>

<dl>
<dd>

**repair:** `typing.Optional[bool]` — with --timestamps only, repairs block(s) in the block range by re-querying from the chain
    
</dd>
</dl>

<dl>
<dd>

**check:** `typing.Optional[bool]` — with --timestamps only, checks the validity of the timestamp data
    
</dd>
</dl>

<dl>
<dd>

**update:** `typing.Optional[bool]` — with --timestamps only, bring the timestamp database forward to the latest block
    
</dd>
</dl>

<dl>
<dd>

**deep:** `typing.Optional[int]` — with --timestamps --check only, verifies every N timestamp directly from the chain (slow)
    
</dd>
</dl>

<dl>
<dd>

**chain:** `typing.Optional[str]` — the chain to use
    
</dd>
</dl>

<dl>
<dd>

**no_header:** `typing.Optional[bool]` — suppress the header in the output
    
</dd>
</dl>

<dl>
<dd>

**cache:** `typing.Optional[bool]` — force the results of the query into the cache
    
</dd>
</dl>

<dl>
<dd>

**decache:** `typing.Optional[bool]` — removes related items from the cache
    
</dd>
</dl>

<dl>
<dd>

**fmt:** `typing.Optional[str]` — export format, one of [ txt | csv | json ]
    
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

## Chain State
<details><summary><code>client.chain_state.<a href="src/fern/chain_state/client.py">chainstate_state</a>(...) -> ChainstateStateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve account balance(s) for one or more addresses at given block(s). Corresponds to the <a href="/chifra/chainstate/#chifra-state">chifra state</a> command line.
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.chain_state.chainstate_state(
    addrs=[
        "addrs"
    ],
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

**addrs:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — one or more addresses (0x...) from which to retrieve balances
    
</dd>
</dl>

<dl>
<dd>

**blocks:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — an optional list of one or more blocks at which to report balances, defaults to 'latest'
    
</dd>
</dl>

<dl>
<dd>

**parts:** `typing.Optional[typing.Union[ChainstateStateRequestPartsItem, typing.Sequence[ChainstateStateRequestPartsItem]]]` — control which state to export
    
</dd>
</dl>

<dl>
<dd>

**changes:** `typing.Optional[bool]` — only report a balance when it changes from one block to the next
    
</dd>
</dl>

<dl>
<dd>

**no_zero:** `typing.Optional[bool]` — suppress the display of zero balance accounts
    
</dd>
</dl>

<dl>
<dd>

**call:** `typing.Optional[bool]` — write-only call (a query) to a smart contract
    
</dd>
</dl>

<dl>
<dd>

**calldata:** `typing.Optional[str]` — for commands (--call or --send), provides the call data (in various forms) for the command (may be empty for --send)
    
</dd>
</dl>

<dl>
<dd>

**articulate:** `typing.Optional[bool]` — for commands only, articulate the retrieved data if ABIs can be found
    
</dd>
</dl>

<dl>
<dd>

**proxy_for:** `typing.Optional[str]` — for commands only, redirects calls to this implementation
    
</dd>
</dl>

<dl>
<dd>

**chain:** `typing.Optional[str]` — the chain to use
    
</dd>
</dl>

<dl>
<dd>

**no_header:** `typing.Optional[bool]` — suppress the header in the output
    
</dd>
</dl>

<dl>
<dd>

**cache:** `typing.Optional[bool]` — force the results of the query into the cache
    
</dd>
</dl>

<dl>
<dd>

**decache:** `typing.Optional[bool]` — removes related items from the cache
    
</dd>
</dl>

<dl>
<dd>

**ether:** `typing.Optional[bool]` — export values in ether
    
</dd>
</dl>

<dl>
<dd>

**fmt:** `typing.Optional[str]` — export format, one of [ txt | csv | json ]
    
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

<details><summary><code>client.chain_state.<a href="src/fern/chain_state/client.py">chainstate_tokens</a>(...) -> ChainstateTokensResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve token balance(s) for one or more addresses at given block(s). Corresponds to the <a href="/chifra/chainstate/#chifra-tokens">chifra tokens</a> command line.
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.chain_state.chainstate_tokens(
    addrs=[
        "addrs"
    ],
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

**addrs:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — two or more addresses (one for --approvals), the first is an ERC20 token, balances for the rest are reported
    
</dd>
</dl>

<dl>
<dd>

**blocks:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — an optional list of one or more blocks at which to report balances, defaults to 'latest'
    
</dd>
</dl>

<dl>
<dd>

**approvals:** `typing.Optional[bool]` — returns all open approvals for the given address(es)
    
</dd>
</dl>

<dl>
<dd>

**parts:** `typing.Optional[typing.Union[ChainstateTokensRequestPartsItem, typing.Sequence[ChainstateTokensRequestPartsItem]]]` — which parts of the token information to retrieve
    
</dd>
</dl>

<dl>
<dd>

**by_acct:** `typing.Optional[bool]` — consider each address an ERC20 token except the last, whose balance is reported for each token
    
</dd>
</dl>

<dl>
<dd>

**changes:** `typing.Optional[bool]` — only report a balance when it changes from one block to the next
    
</dd>
</dl>

<dl>
<dd>

**no_zero:** `typing.Optional[bool]` — suppress the display of zero balance accounts
    
</dd>
</dl>

<dl>
<dd>

**chain:** `typing.Optional[str]` — the chain to use
    
</dd>
</dl>

<dl>
<dd>

**no_header:** `typing.Optional[bool]` — suppress the header in the output
    
</dd>
</dl>

<dl>
<dd>

**cache:** `typing.Optional[bool]` — force the results of the query into the cache
    
</dd>
</dl>

<dl>
<dd>

**decache:** `typing.Optional[bool]` — removes related items from the cache
    
</dd>
</dl>

<dl>
<dd>

**fmt:** `typing.Optional[str]` — export format, one of [ txt | csv | json ]
    
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

## Admin
<details><summary><code>client.admin.<a href="src/fern/admin/client.py">config</a>(...) -> AdminConfigResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Report on and edit the configuration of the TrueBlocks system. Corresponds to the <a href="/chifra/admin/#chifra-config">chifra config</a> command line.
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.admin.config()

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

**mode:** `typing.Optional[AdminConfigRequestMode]` — either show or edit the configuration
    
</dd>
</dl>

<dl>
<dd>

**paths:** `typing.Optional[bool]` — show the configuration paths for the system
    
</dd>
</dl>

<dl>
<dd>

**dump:** `typing.Optional[bool]` — dump the configuration to stdout
    
</dd>
</dl>

<dl>
<dd>

**chain:** `typing.Optional[str]` — the chain to use
    
</dd>
</dl>

<dl>
<dd>

**no_header:** `typing.Optional[bool]` — suppress the header in the output
    
</dd>
</dl>

<dl>
<dd>

**fmt:** `typing.Optional[str]` — export format, one of [ txt | csv | json ]
    
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

<details><summary><code>client.admin.<a href="src/fern/admin/client.py">status</a>(...) -> AdminStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Report on the state of the internal binary caches. Corresponds to the <a href="/chifra/admin/#chifra-status">chifra status</a> command line.
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.admin.status()

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

**modes:** `typing.Optional[typing.Union[AdminStatusRequestModesItem, typing.Sequence[AdminStatusRequestModesItem]]]` — the (optional) name of the binary cache to report on, terse otherwise
    
</dd>
</dl>

<dl>
<dd>

**diagnose:** `typing.Optional[bool]` — same as the default but with additional diagnostics
    
</dd>
</dl>

<dl>
<dd>

**first_record:** `typing.Optional[int]` — the first record to process
    
</dd>
</dl>

<dl>
<dd>

**max_records:** `typing.Optional[int]` — the maximum number of records to process
    
</dd>
</dl>

<dl>
<dd>

**chains:** `typing.Optional[bool]` — include a list of chain configurations in the output
    
</dd>
</dl>

<dl>
<dd>

**caches:** `typing.Optional[bool]` — include a list of cache items in the output
    
</dd>
</dl>

<dl>
<dd>

**healthcheck:** `typing.Optional[bool]` — an alias for the diagnose endpoint
    
</dd>
</dl>

<dl>
<dd>

**chain:** `typing.Optional[str]` — the chain to use
    
</dd>
</dl>

<dl>
<dd>

**no_header:** `typing.Optional[bool]` — suppress the header in the output
    
</dd>
</dl>

<dl>
<dd>

**fmt:** `typing.Optional[str]` — export format, one of [ txt | csv | json ]
    
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

<details><summary><code>client.admin.<a href="src/fern/admin/client.py">chunks</a>(...) -> AdminChunksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manage, investigate, and display the Unchained Index. Corresponds to the <a href="/chifra/admin/#chifra-chunks">chifra chunks</a> command line.
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.admin.chunks(
    mode="manifest",
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

**mode:** `AdminChunksRequestMode` — the type of data to process
    
</dd>
</dl>

<dl>
<dd>

**blocks:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — an optional list of blocks to intersect with chunk ranges
    
</dd>
</dl>

<dl>
<dd>

**check:** `typing.Optional[bool]` — check the manifest, index, or blooms for internal consistency
    
</dd>
</dl>

<dl>
<dd>

**belongs:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — in index mode only, checks the address(es) for inclusion in the given index chunk
    
</dd>
</dl>

<dl>
<dd>

**first_block:** `typing.Optional[float]` — first block to process (inclusive)
    
</dd>
</dl>

<dl>
<dd>

**last_block:** `typing.Optional[float]` — last block to process (inclusive)
    
</dd>
</dl>

<dl>
<dd>

**max_addrs:** `typing.Optional[int]` — the max number of addresses to process in a given chunk
    
</dd>
</dl>

<dl>
<dd>

**deep:** `typing.Optional[bool]` — if true, dig more deeply during checking (manifest only)
    
</dd>
</dl>

<dl>
<dd>

**rewrite:** `typing.Optional[bool]` — for the --pin --deep mode only, writes the manifest back to the index folder (see notes)
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[bool]` — for certain modes only, display the count of records
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[bool]` — for --pin only, pin only metadata files (ts.bin and manifest.json)
    
</dd>
</dl>

<dl>
<dd>

**sleep:** `typing.Optional[float]` — for --remote pinning only, seconds to sleep between API calls
    
</dd>
</dl>

<dl>
<dd>

**chain:** `typing.Optional[str]` — the chain to use
    
</dd>
</dl>

<dl>
<dd>

**no_header:** `typing.Optional[bool]` — suppress the header in the output
    
</dd>
</dl>

<dl>
<dd>

**fmt:** `typing.Optional[str]` — export format, one of [ txt | csv | json ]
    
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

<details><summary><code>client.admin.<a href="src/fern/admin/client.py">init</a>(...) -> AdminInitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Initialize the TrueBlocks system by downloading the Unchained Index from IPFS. Corresponds to the <a href="/chifra/admin/#chifra-init">chifra init</a> command line.
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.admin.init()

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

**all:** `typing.Optional[bool]` — in addition to Bloom filters, download full index chunks (recommended)
    
</dd>
</dl>

<dl>
<dd>

**example:** `typing.Optional[str]` — create an example for the SDK with the given name
    
</dd>
</dl>

<dl>
<dd>

**dry_run:** `typing.Optional[bool]` — display the results of the download without actually downloading
    
</dd>
</dl>

<dl>
<dd>

**first_block:** `typing.Optional[float]` — do not download any chunks earlier than this block
    
</dd>
</dl>

<dl>
<dd>

**sleep:** `typing.Optional[float]` — seconds to sleep between downloads
    
</dd>
</dl>

<dl>
<dd>

**chain:** `typing.Optional[str]` — the chain to use
    
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

## Other
<details><summary><code>client.other.<a href="src/fern/other/client.py">slurp</a>(...) -> OtherSlurpResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch data from Etherscan and other APIs for any address. Corresponds to the <a href="/chifra/other/#chifra-slurp">chifra slurp</a> command line.
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.other.slurp(
    addrs=[
        "addrs"
    ],
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

**addrs:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — one or more addresses to slurp from Etherscan
    
</dd>
</dl>

<dl>
<dd>

**blocks:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — an optional range of blocks to slurp
    
</dd>
</dl>

<dl>
<dd>

**parts:** `typing.Optional[typing.Union[OtherSlurpRequestPartsItem, typing.Sequence[OtherSlurpRequestPartsItem]]]` — which types of transactions to request
    
</dd>
</dl>

<dl>
<dd>

**appearances:** `typing.Optional[bool]` — show only the blocknumber.tx_id appearances of the exported transactions
    
</dd>
</dl>

<dl>
<dd>

**articulate:** `typing.Optional[bool]` — articulate the retrieved data if ABIs can be found
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[OtherSlurpRequestSource]` — the source of the slurped data
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[bool]` — for --appearances mode only, display only the count of records
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — the page to retrieve (page number)
    
</dd>
</dl>

<dl>
<dd>

**page_id:** `typing.Optional[str]` — the page to retrieve (page ID)
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — the number of records to request on each page
    
</dd>
</dl>

<dl>
<dd>

**sleep:** `typing.Optional[float]` — seconds to sleep between requests
    
</dd>
</dl>

<dl>
<dd>

**chain:** `typing.Optional[str]` — the chain to use
    
</dd>
</dl>

<dl>
<dd>

**no_header:** `typing.Optional[bool]` — suppress the header in the output
    
</dd>
</dl>

<dl>
<dd>

**cache:** `typing.Optional[bool]` — force the results of the query into the cache
    
</dd>
</dl>

<dl>
<dd>

**decache:** `typing.Optional[bool]` — removes related items from the cache
    
</dd>
</dl>

<dl>
<dd>

**ether:** `typing.Optional[bool]` — export values in ether
    
</dd>
</dl>

<dl>
<dd>

**fmt:** `typing.Optional[str]` — export format, one of [ txt | csv | json ]
    
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

