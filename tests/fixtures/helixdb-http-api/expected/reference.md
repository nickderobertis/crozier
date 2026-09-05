# Reference
## Queries
<details><summary><code>client.queries.<a href="src/fern/queries/client.py">execute_query</a>(...) -> typing.Optional[QueryResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Executes one read or write batch. request_type must match the closed read or write variant under query. Local servers accept request bodies up to 16 MiB. Helix Cloud gateways accept request bodies up to 2 MiB.
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
from fern import FernApi, QueryRequest_Read, ReadBatchQuery, Batch, BatchEntryQuery, NamedQuery
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.queries.execute_query(
    request=QueryRequest_Read(
        query=ReadBatchQuery(
            read=Batch(
                entries=[
                    BatchEntryQuery(
                        query=NamedQuery(
                            root={
                                "key": "value"
                            },
                        ),
                    )
                ],
            ),
        ),
    ),
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

**request:** `QueryRequest` 
    
</dd>
</dl>

<dl>
<dd>

**helix_database_id:** `typing.Optional[str]` — Database identifier shown in Helix Cloud connection details. Required by the GA shared gateway, not needed by a standalone local server, and not allowed by a database-specific cluster-mode gateway. The legacy X-Helix-Tenant-Id alias is also accepted in GA mode.
    
</dd>
</dl>

<dl>
<dd>

**helix_warm:** `typing.Optional[bool]` — Warm read execution state. Valid only for read requests.
    
</dd>
</dl>

<dl>
<dd>

**helix_require_writer:** `typing.Optional[bool]` — Reject the request unless it reaches a writer-capable server.
    
</dd>
</dl>

<dl>
<dd>

**helix_await_durable:** `typing.Optional[bool]` — Flush the writer before acknowledging success. Valid only for write requests.
    
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

## Health
<details><summary><code>client.health.<a href="src/fern/health/client.py">get_health</a>() -> HealthResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reports process liveness and the current database and index-runtime state. Liveness returns 200 even when ready is false.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.health.get_health()

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

<details><summary><code>client.health.<a href="src/fern/health/client.py">get_readiness</a>() -> HealthResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns 200 only when the configured database handle and index runtime are ready to serve queries.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.health.get_readiness()

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

