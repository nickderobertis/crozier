# Reference
## Index
<details><summary><code>client.index.<a href="src/fern/index/client.py">search_index</a>(...) -> Error</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

EXPERIMENTAL - this endpoint is offered as best effort only and may be changed or removed in future releases.
The results returned from this endpoint may be incomplete.
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

client.index.search_index()

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

**email:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**hash:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**operator:** `typing.Optional[SearchIndexOperator]` 
    
</dd>
</dl>

<dl>
<dd>

**public_key:** `typing.Optional[SearchIndexPublicKey]` 
    
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

## Tlog
<details><summary><code>client.tlog.<a href="src/fern/tlog/client.py">get_log_info</a>(...) -> Error</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the current root hash and size of the merkle tree used to store the log entries.
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

client.tlog.get_log_info()

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

**stable:** `typing.Optional[bool]` — Whether to return a stable checkpoint for the active shard
    
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

<details><summary><code>client.tlog.<a href="src/fern/tlog/client.py">get_log_proof</a>(...) -> Error</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of hashes for specified tree sizes that can be used to confirm the consistency of the transparency log
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

client.tlog.get_log_proof()

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

**first_size:** `typing.Optional[int]` — The size of the tree that you wish to prove consistency from (1 means the beginning of the log) Defaults to 1 if not specified
    
</dd>
</dl>

<dl>
<dd>

**last_size:** `typing.Optional[int]` — The size of the tree that you wish to prove consistency to
    
</dd>
</dl>

<dl>
<dd>

**tree_id:** `typing.Optional[str]` — The tree ID of the tree that you wish to prove consistency for
    
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

## Entries
<details><summary><code>client.entries.<a href="src/fern/entries/client.py">get_log_entry_by_index</a>(...) -> Error</code></summary>
<dl>
<dd>

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

client.entries.get_log_entry_by_index()

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

**log_index:** `typing.Optional[int]` — specifies the index of the entry in the transparency log to be retrieved
    
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

<details><summary><code>client.entries.<a href="src/fern/entries/client.py">create_log_entry</a>(...) -> Error</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an entry in the transparency log for a detached signature, public key, and content. Items can be included in the request or fetched by the server when URLs are specified.
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

client.entries.create_log_entry(
    kind="kind",
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

**request:** `ProposedEntry` 
    
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

<details><summary><code>client.entries.<a href="src/fern/entries/client.py">search_log_query</a>(...) -> Error</code></summary>
<dl>
<dd>

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

client.entries.search_log_query()

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

**entries:** `typing.Optional[typing.List[ProposedEntry]]` 
    
</dd>
</dl>

<dl>
<dd>

**entry_uui_ds:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**log_indexes:** `typing.Optional[typing.List[int]]` 
    
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

<details><summary><code>client.entries.<a href="src/fern/entries/client.py">get_log_entry_by_uuid</a>(...) -> Error</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the entry, root hash, tree size, and a list of hashes that can be used to calculate proof of an entry being included in the transparency log
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

client.entries.get_log_entry_by_uuid(
    entry_uuid="entryUUID",
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

**entry_uuid:** `str` — the UUID of the entry for which the inclusion proof information should be returned
    
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

## Pubkey
<details><summary><code>client.pubkey.<a href="src/fern/pubkey/client.py">get_public_key</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the public key that can be used to validate the signed tree head
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

client.pubkey.get_public_key()

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

**tree_id:** `typing.Optional[str]` — The tree ID of the tree you wish to get a public key for
    
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

