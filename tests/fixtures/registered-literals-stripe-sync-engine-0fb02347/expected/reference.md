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

## Pipelines
<details><summary><code>client.pipelines.<a href="src/fern/pipelines/client.py">list</a>() -> PipelinesListResponse</code></summary>
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

client.pipelines.list()

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

<details><summary><code>client.pipelines.<a href="src/fern/pipelines/client.py">create</a>(...) -> Pipeline</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, SourceConfig_Stripe, SourceStripeConfig, DestinationConfig_Postgres, DestinationPostgresConfig

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.pipelines.create(
    source=SourceConfig_Stripe(
        stripe=SourceStripeConfig(
            api_key="api_key",
        ),
    ),
    destination=DestinationConfig_Postgres(
        postgres=DestinationPostgresConfig(),
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

**source:** `SourceConfig` 
    
</dd>
</dl>

<dl>
<dd>

**destination:** `DestinationConfig` 
    
</dd>
</dl>

<dl>
<dd>

**skip_check:** `typing.Optional[bool]` — Skip connector validation checks
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — Optional pipeline identifier. If omitted, the service generates one (e.g. pipe_abc123).
    
</dd>
</dl>

<dl>
<dd>

**streams:** `typing.Optional[typing.List[PipelinesCreateRequestStreamsItem]]` — Selected streams to sync. All streams synced if omitted.
    
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

<details><summary><code>client.pipelines.<a href="src/fern/pipelines/client.py">get</a>(...) -> Pipeline</code></summary>
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

client.pipelines.get(
    id="pipe_abc123",
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

**id:** `str` — Unique pipeline identifier (e.g. pipe_abc123).
    
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

<details><summary><code>client.pipelines.<a href="src/fern/pipelines/client.py">delete</a>(...) -> PipelinesDeleteResponse</code></summary>
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

client.pipelines.delete(
    id="pipe_abc123",
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

**id:** `str` — Unique pipeline identifier (e.g. pipe_abc123).
    
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

<details><summary><code>client.pipelines.<a href="src/fern/pipelines/client.py">update</a>(...) -> Pipeline</code></summary>
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

client.pipelines.update(
    id_path_param="pipe_abc123",
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

**id_path_param:** `str` — Unique pipeline identifier (e.g. pipe_abc123).
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — Optional pipeline identifier. If omitted, the service generates one (e.g. pipe_abc123).
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[SourceConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**destination:** `typing.Optional[DestinationConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**streams:** `typing.Optional[typing.List[PipelinesUpdateRequestStreamsItem]]` — Selected streams to sync. All streams synced if omitted.
    
</dd>
</dl>

<dl>
<dd>

**desired_status:** `typing.Optional[PipelinesUpdateRequestDesiredStatus]` — Set to "paused" to pause, "active" to resume, "deleted" to tear down.
    
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

<details><summary><code>client.pipelines.<a href="src/fern/pipelines/client.py">sync</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Triggers an ad-hoc sync run for the pipeline and streams NDJSON messages (records, state, progress, eof) back to the client. Persists the ending sync_state on the pipeline so the next run resumes where this one left off.
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

client.pipelines.sync(
    id="pipe_abc123",
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

**id:** `str` — Unique pipeline identifier (e.g. pipe_abc123).
    
</dd>
</dl>

<dl>
<dd>

**time_limit:** `typing.Optional[float]` — Stop after N seconds
    
</dd>
</dl>

<dl>
<dd>

**run_id:** `typing.Optional[str]` — Sync run identifier (resumes or starts fresh)
    
</dd>
</dl>

<dl>
<dd>

**reset_state:** `typing.Optional[bool]` — Ignore persisted sync state and start fresh (ending state is still saved)
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[SourceConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**destination:** `typing.Optional[DestinationConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**streams:** `typing.Optional[typing.List[PipelinesSyncRequestStreamsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**sync_state:** `typing.Optional[SyncState]` — Explicit sync checkpoint override for resumed ad-hoc runs
    
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

<details><summary><code>client.pipelines.<a href="src/fern/pipelines/client.py">sync_batch</a>(...) -> EofPayload</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Runs the full sync pipeline and returns the final EofPayload as a single JSON response. Persists the ending sync_state on the pipeline so the next run resumes where this one left off.
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

client.pipelines.sync_batch(
    id="pipe_abc123",
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

**id:** `str` — Unique pipeline identifier (e.g. pipe_abc123).
    
</dd>
</dl>

<dl>
<dd>

**state_limit:** `typing.Optional[int]` — Stop after N source_state messages
    
</dd>
</dl>

<dl>
<dd>

**run_id:** `typing.Optional[str]` — Sync run identifier (resumes or starts fresh)
    
</dd>
</dl>

<dl>
<dd>

**reset_state:** `typing.Optional[bool]` — Ignore persisted sync state and start fresh (ending state is still saved)
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[SourceConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**destination:** `typing.Optional[DestinationConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**streams:** `typing.Optional[typing.List[PipelinesSyncBatchRequestStreamsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**sync_state:** `typing.Optional[SyncState]` — Explicit sync checkpoint override for resumed ad-hoc runs
    
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

<details><summary><code>client.pipelines.<a href="src/fern/pipelines/client.py">check</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Runs the `check()` method on source and/or destination connectors and streams back NDJSON messages (connection_status, log, trace). Pass ?only=source or ?only=destination to check a single side.
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

client.pipelines.check(
    id="pipe_abc123",
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

**id:** `str` — Unique pipeline identifier (e.g. pipe_abc123).
    
</dd>
</dl>

<dl>
<dd>

**only:** `typing.Optional[PipelinesCheckRequestOnly]` — Run only the source or destination side
    
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

<details><summary><code>client.pipelines.<a href="src/fern/pipelines/client.py">setup</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Runs the `setup()` method on source and/or destination connectors (e.g. creating destination tables). Streams NDJSON messages (control, log, trace). Pass ?only=source or ?only=destination to run a single side.
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

client.pipelines.setup(
    id="pipe_abc123",
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

**id:** `str` — Unique pipeline identifier (e.g. pipe_abc123).
    
</dd>
</dl>

<dl>
<dd>

**only:** `typing.Optional[PipelinesSetupRequestOnly]` — Run only the source or destination side
    
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

<details><summary><code>client.pipelines.<a href="src/fern/pipelines/client.py">teardown</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Runs the `teardown()` method on source and/or destination connectors (e.g. dropping destination tables). Streams NDJSON messages (log, trace). Pass ?only=source or ?only=destination to run a single side.
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

client.pipelines.teardown(
    id="pipe_abc123",
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

**id:** `str` — Unique pipeline identifier (e.g. pipe_abc123).
    
</dd>
</dl>

<dl>
<dd>

**only:** `typing.Optional[PipelinesTeardownRequestOnly]` — Run only the source or destination side
    
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

<details><summary><code>client.pipelines.<a href="src/fern/pipelines/client.py">simulate_webhook_sync</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches events from /v1/events using the pipeline's Stripe API key, then pipes them as input into the sync engine's push mode. This exercises the same code path as real webhooks without needing webhook delivery.
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

client.pipelines.simulate_webhook_sync(
    id="pipe_abc123",
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

**id:** `str` — Unique pipeline identifier (e.g. pipe_abc123).
    
</dd>
</dl>

<dl>
<dd>

**created_after:** `typing.Optional[float]` — Only fetch events created after this Unix timestamp (default: 24 hours ago)
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Max events to fetch (default: all)
    
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

<details><summary><code>client.pipelines.<a href="src/fern/pipelines/client.py">sync_workflow_test</a>(...) -> PipelinesSyncWorkflowTestResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Exercises the same backfill loop code that the Temporal workflow uses, but runs inline without a Temporal server. Useful for testing the full workflow logic end-to-end.
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

client.pipelines.sync_workflow_test(
    id="pipe_abc123",
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

**id:** `str` — Unique pipeline identifier (e.g. pipe_abc123).
    
</dd>
</dl>

<dl>
<dd>

**time_limit:** `typing.Optional[float]` — Time limit per iteration (seconds)
    
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

## Webhooks
<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">push</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Receives a raw Stripe webhook event, verifies its signature using the pipeline's webhook secret, and enqueues it for processing by the active pipeline.
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

client.webhooks.push(
    pipeline_id="pipeline_id",
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

**pipeline_id:** `str` 
    
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

