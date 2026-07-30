# Reference
## Status
<details><summary><code>client.status.<a href="src/fern/status/client.py">health</a>() -> HealthResponse</code></summary>
<dl>
<dd>

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

client.status.health()

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

## StatelessSyncApi
<details><summary><code>client.stateless_sync_api.<a href="src/fern/stateless_sync_api/client.py">pipeline_check</a>(...) -> CheckOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Validates the source/destination config and tests connectivity. Streams NDJSON messages (connection_status, log, trace) tagged with _emitted_by. Pass only=source or only=destination to check a single side.
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
from fern import FernApi, PipelineConfig, SourceConfig_Stripe, SourceStripeConfig, DestinationConfig_Postgres, DestinationPostgresConfig

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.stateless_sync_api.pipeline_check(
    pipeline=PipelineConfig(
        source=SourceConfig_Stripe(
            stripe=SourceStripeConfig(
                api_key="api_key",
            ),
        ),
        destination=DestinationConfig_Postgres(
            postgres=DestinationPostgresConfig(),
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

**pipeline:** `PipelineConfig` 
    
</dd>
</dl>

<dl>
<dd>

**only:** `typing.Optional[PipelineCheckRequestOnly]` — Run only the source or destination side. Useful for optimistic destination setup or isolating a connector when debugging.
    
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

<details><summary><code>client.stateless_sync_api.<a href="src/fern/stateless_sync_api/client.py">pipeline_setup</a>(...) -> SetupOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates destination tables and applies migrations. Streams NDJSON messages (control, log, trace) tagged with _emitted_by. Pass only=destination to run destination setup alone (e.g. optimistic table creation) or only=source to isolate the source.
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
from fern import FernApi, PipelineConfig, SourceConfig_Stripe, SourceStripeConfig, DestinationConfig_Postgres, DestinationPostgresConfig

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.stateless_sync_api.pipeline_setup(
    pipeline=PipelineConfig(
        source=SourceConfig_Stripe(
            stripe=SourceStripeConfig(
                api_key="api_key",
            ),
        ),
        destination=DestinationConfig_Postgres(
            postgres=DestinationPostgresConfig(),
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

**pipeline:** `PipelineConfig` 
    
</dd>
</dl>

<dl>
<dd>

**only:** `typing.Optional[PipelineSetupRequestOnly]` — Run only the source or destination side. Useful for optimistic destination setup or isolating a connector when debugging.
    
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

<details><summary><code>client.stateless_sync_api.<a href="src/fern/stateless_sync_api/client.py">pipeline_teardown</a>(...) -> TeardownOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Drops destination tables. Streams NDJSON messages (log, trace) tagged with _emitted_by. Pass only=destination or only=source to run a single side.
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
from fern import FernApi, PipelineConfig, SourceConfig_Stripe, SourceStripeConfig, DestinationConfig_Postgres, DestinationPostgresConfig

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.stateless_sync_api.pipeline_teardown(
    pipeline=PipelineConfig(
        source=SourceConfig_Stripe(
            stripe=SourceStripeConfig(
                api_key="api_key",
            ),
        ),
        destination=DestinationConfig_Postgres(
            postgres=DestinationPostgresConfig(),
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

**pipeline:** `PipelineConfig` 
    
</dd>
</dl>

<dl>
<dd>

**only:** `typing.Optional[PipelineTeardownRequestOnly]` — Run only the source or destination side. Useful for optimistic destination setup or isolating a connector when debugging.
    
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

<details><summary><code>client.stateless_sync_api.<a href="src/fern/stateless_sync_api/client.py">source_discover</a>(...) -> DiscoverOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Streams NDJSON messages (catalog, logs, traces) for the configured source.
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
from fern.stateless_sync_api import SourceDiscoverRequestSource

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.stateless_sync_api.source_discover(
    source=SourceDiscoverRequestSource(
        type="type",
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

**source:** `SourceDiscoverRequestSource` — Source config ({ type, ...config })
    
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

<details><summary><code>client.stateless_sync_api.<a href="src/fern/stateless_sync_api/client.py">pipeline_read</a>(...) -> Message</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Streams NDJSON messages (records, state, catalog).
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
from fern import FernApi, PipelineConfig, SourceConfig_Stripe, SourceStripeConfig, DestinationConfig_Postgres, DestinationPostgresConfig

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.stateless_sync_api.pipeline_read(
    pipeline=PipelineConfig(
        source=SourceConfig_Stripe(
            stripe=SourceStripeConfig(
                api_key="api_key",
            ),
        ),
        destination=DestinationConfig_Postgres(
            postgres=DestinationPostgresConfig(),
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

**pipeline:** `PipelineConfig` 
    
</dd>
</dl>

<dl>
<dd>

**time_limit:** `typing.Optional[float]` — Stop streaming after N seconds.
    
</dd>
</dl>

<dl>
<dd>

**soft_time_limit:** `typing.Optional[float]` — Soft wall-clock deadline in seconds. Stops reading from the source between messages; the destination continues to drain and flush until time_limit fires.
    
</dd>
</dl>

<dl>
<dd>

**run_id:** `typing.Optional[str]` — Optional sync run identifier used to track bounded sync progress.
    
</dd>
</dl>

<dl>
<dd>

**stdin:** `typing.Optional[typing.List[Message]]` — Optional array of input messages (push mode). Without stdin, reads from the source connector (backfill mode).
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[SyncState]` — SyncState ({ source, destination, sync_run }). Falls back to empty state if invalid.
    
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

<details><summary><code>client.stateless_sync_api.<a href="src/fern/stateless_sync_api/client.py">pipeline_write</a>(...) -> DestinationOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Writes messages to the destination. Pass an array of messages in the request body.
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
from fern import FernApi, PipelineConfig, SourceConfig_Stripe, SourceStripeConfig, DestinationConfig_Postgres, DestinationPostgresConfig, Message_Record, RecordMessageRecord
import datetime

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.stateless_sync_api.pipeline_write(
    pipeline=PipelineConfig(
        source=SourceConfig_Stripe(
            stripe=SourceStripeConfig(
                api_key="api_key",
            ),
        ),
        destination=DestinationConfig_Postgres(
            postgres=DestinationPostgresConfig(),
        ),
    ),
    stdin=[
        Message_Record(
            record=RecordMessageRecord(
                stream="stream",
                data={
                    "key": "value"
                },
                emitted_at=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
            ),
        )
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

**pipeline:** `PipelineConfig` 
    
</dd>
</dl>

<dl>
<dd>

**stdin:** `typing.List[Message]` — Array of messages to write to the destination.
    
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

<details><summary><code>client.stateless_sync_api.<a href="src/fern/stateless_sync_api/client.py">pipeline_sync</a>(...) -> SyncOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reads from the source connector and writes to the destination (backfill mode).
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
from fern import FernApi, PipelineConfig, SourceConfig_Stripe, SourceStripeConfig, DestinationConfig_Postgres, DestinationPostgresConfig

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.stateless_sync_api.pipeline_sync(
    pipeline=PipelineConfig(
        source=SourceConfig_Stripe(
            stripe=SourceStripeConfig(
                api_key="api_key",
            ),
        ),
        destination=DestinationConfig_Postgres(
            postgres=DestinationPostgresConfig(),
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

**pipeline:** `PipelineConfig` 
    
</dd>
</dl>

<dl>
<dd>

**time_limit:** `typing.Optional[float]` — Stop streaming after N seconds.
    
</dd>
</dl>

<dl>
<dd>

**soft_time_limit:** `typing.Optional[float]` — Soft wall-clock deadline in seconds. Stops reading from the source between messages; the destination continues to drain and flush until time_limit fires.
    
</dd>
</dl>

<dl>
<dd>

**run_id:** `typing.Optional[str]` — Optional sync run identifier used to track bounded sync progress.
    
</dd>
</dl>

<dl>
<dd>

**stdin:** `typing.Optional[typing.List[Message]]` — Optional array of input messages (push mode). Without stdin, reads from the source connector (backfill mode).
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[SyncState]` — SyncState ({ source, destination, sync_run }). Falls back to empty state if invalid.
    
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

<details><summary><code>client.stateless_sync_api.<a href="src/fern/stateless_sync_api/client.py">pipeline_sync_batch</a>(...) -> EofPayload</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Runs the full read → write pipeline and returns the final EofPayload as a single JSON response.
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
from fern import FernApi, PipelineConfig, SourceConfig_Stripe, SourceStripeConfig, DestinationConfig_Postgres, DestinationPostgresConfig

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.stateless_sync_api.pipeline_sync_batch(
    pipeline=PipelineConfig(
        source=SourceConfig_Stripe(
            stripe=SourceStripeConfig(
                api_key="api_key",
            ),
        ),
        destination=DestinationConfig_Postgres(
            postgres=DestinationPostgresConfig(),
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

**pipeline:** `PipelineConfig` 
    
</dd>
</dl>

<dl>
<dd>

**run_id:** `typing.Optional[str]` — Optional sync run identifier used to track bounded sync progress.
    
</dd>
</dl>

<dl>
<dd>

**state_limit:** `typing.Optional[int]` — Stop after yielding N source_state messages, inclusive.
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[SyncState]` — SyncState ({ source, destination, sync_run }). Falls back to empty state if invalid.
    
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

## Meta
<details><summary><code>client.meta.<a href="src/fern/meta/client.py">sources_list</a>() -> MetaSourcesListResponse</code></summary>
<dl>
<dd>

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

client.meta.sources_list()

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

<details><summary><code>client.meta.<a href="src/fern/meta/client.py">sources_get</a>(...) -> MetaSourcesGetResponse</code></summary>
<dl>
<dd>

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

client.meta.sources_get(
    type="type",
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

**type:** `str` 
    
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

<details><summary><code>client.meta.<a href="src/fern/meta/client.py">destinations_list</a>() -> MetaDestinationsListResponse</code></summary>
<dl>
<dd>

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

client.meta.destinations_list()

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

<details><summary><code>client.meta.<a href="src/fern/meta/client.py">destinations_get</a>(...) -> MetaDestinationsGetResponse</code></summary>
<dl>
<dd>

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

client.meta.destinations_get(
    type="type",
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

**type:** `str` 
    
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

## Internal
<details><summary><code>client.internal.<a href="src/fern/internal/client.py">query</a>(...) -> InternalQueryResponse</code></summary>
<dl>
<dd>

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

client.internal.query(
    sql="sql",
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

**sql:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**connection_string:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` 
    
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

