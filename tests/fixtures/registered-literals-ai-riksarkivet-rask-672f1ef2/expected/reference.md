# Reference
## Admin
<details><summary><code>client.admin.<a href="src/fern/admin/client.py#L27-L63">list_dlq</a>(...) -> DlqBacklog</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The outbox saturation snapshot + the visible at-risk events (oldest first, capped at ``limit``).

``depth``/``oldest_age_seconds`` are the raw system-health signal; ``events`` is the per-dataset-governed
subset the caller may see. Requires an authenticated principal when FGA is on (else the raw depth would
leak to an anonymous caller); the event list is then filtered by dataset visibility.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.admin.list_dlq()

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

**limit:** `typing.Optional[int]` 
    
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

<details><summary><code>client.admin.<a href="src/fern/admin/client.py#L65-L112">replay_dlq</a>(...) -> DlqReplayResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Re-ingest one staged event on demand, re-publish it, then drop it — the manual twin of the reconcile relay's drain.

A replay IS a re-ingest, so it carries the SAME authz as a fresh ingest, twice over: the relay's gate on
the staged bytes (:func:`enforce_bus_authz` — signature and stamped author) and the ingest door's on the
operator (:func:`enforce_output_authz` — ``can_write_data`` on the outputs, ``can_get_metadata`` on the
inputs, fail-closed). Both doors are idempotent: a run MERGEs on its run id, a static change on its
derived feed id, and the durable feed insert is ON CONFLICT DO NOTHING. The staged bytes are re-published
to the lineage topic exactly as the relay re-publishes them, so subscribers hear of the event as well as
the graph. The drop is only reached on success — a failed re-ingest or re-publish leaves the object
staged for the relay to retry, and a failed re-publish answers 503 because the graph is already
repaired.

Non-disclosure (audit 2026-07-20): replay must not become an oracle for events ``list_dlq`` hid. So a
run whose datasets the caller cannot SEE (or an unparseable poison object, which the governed list also
hides) returns the SAME 404 as a missing run — never a distinct 422 or a 403 echoing hidden dataset
names. Only an event the caller could have listed reaches ``enforce_output_authz``.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.admin.replay_dlq(
    run_id="run_id",
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

**run_id:** `str` 
    
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

## Ingest
<details><summary><code>client.ingest.<a href="src/fern/ingest/client.py#L28-L82">ingest_event</a>(...) -> typing.Dict[str, typing.Optional[str]]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Ingest one OpenLineage event — a ``RunEvent``, or a ``DatasetEvent`` for a change no job performed.

PARSED HERE RATHER THAN BY THE SIGNATURE, so this door and the bus door share ONE discriminator
(`models.parse_event`). Declaring the body as `RunEvent` is what made a static event 422 before
any handler ran: [[LIN-004]] moved catalog DDL onto `DatasetEvent` and taught only the bus. The
catalog's HTTP emitter is best-effort, so every create it sent lost its provenance in silence —
measured 2026-09-24, three creates, `{"events":[]}` in the durable feed, and a governance
assertion reading `expected lineage creator=..., got None`.

A body that is neither shape raises `RequestValidationError`, which `install_problem_handlers`
renders exactly as FastAPI's own 422 — the wire answer for a malformed payload is unchanged.

This is the OpenLineage HTTP-transport default path, so any OpenLineage producer
(our emitter, Airflow, Spark, dbt, …) configured with ``OPENLINEAGE_URL`` pointed
here ingests with no glue — the lightweight-Marquez contract.

When OIDC is enabled the ``CurrentToken`` dependency requires a verified bearer token
(401 otherwise), :func:`~lineage.api.fga_deps.enforce_author` binds the run author to that
token's subject (no self-asserted identity), and :func:`~lineage.api.fga_deps.enforce_output_authz`
requires ``can_write_data`` on every output dataset (a producer can't record provenance for a table
it can't write). Both are no-ops when auth is off.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.ingest.ingest_event(
    request={
        "key": "value"
    },
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

**request:** `typing.Dict[str, typing.Any]` — A RunEvent, or a DatasetEvent for a dataset change no job performed.
    
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

## PubSub
<details><summary><code>client.pub_sub.<a href="src/fern/pub_sub/client.py#L25-L51">get_subscriptions</a>() -> typing.Any</code></summary>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.pub_sub.get_subscriptions()

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

## Discovery
<details><summary><code>client.discovery.<a href="src/fern/discovery/client.py#L30-L80">list_datasets</a>(...) -> Datasets</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Browse every dataset the caller may see — the lineage catalog's landing list.

Governed (a dataset is shown only if the caller ``can_get_metadata`` on it), optionally filtered by
``?namespace=`` / ``?tag=``, and paginated over the *visible* set. This is the entry point the graph
reads (``/datasets/{name}/...``) needed but could not provide — you no longer must know a name first.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.discovery.list_datasets()

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

**namespace:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
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

<details><summary><code>client.discovery.<a href="src/fern/discovery/client.py#L82-L121">estate_graph</a>(...) -> EstateGraph</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The whole visible lineage graph in ONE response — the graph page's bulk read.

Before this the UI recomposed the estate graph client-side from the per-``{name}`` reads —
one ``/datasets/{name}/graph`` (plus ``/producers``) per dataset per refresh, a 2N+-request
storm at N datasets. Governance is identical to ``/datasets``: a node the caller may not see
is dropped, and an edge needs BOTH endpoints visible (the same transitive-disclosure
guarantee as the per-dataset graph). Nodes are capped at ``limit`` deterministically (sorted
by name) with ``total``/``capped`` reporting the truth.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.discovery.estate_graph()

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

**limit:** `typing.Optional[int]` 
    
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

<details><summary><code>client.discovery.<a href="src/fern/discovery/client.py#L123-L154">list_jobs</a>() -> Jobs</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The jobs (compute identities) that have run — governed by the datasets each wrote.

A job is shown only if the caller can see every dataset it wrote (a read-only / output-less job is
hidden when auth is on, mirroring how ``/events`` drops a dataset-less row). Auth off → pass-through.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.discovery.list_jobs()

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

<details><summary><code>client.discovery.<a href="src/fern/discovery/client.py#L156-L186">list_namespaces</a>() -> Namespaces</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The namespaces containing at least one dataset the caller may see (for a namespace-tree browse).

Derived from the governed dataset set, so a namespace the caller can see no dataset in never appears.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.discovery.list_namespaces()

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

<details><summary><code>client.discovery.<a href="src/fern/discovery/client.py#L188-L233">search</a>(...) -> SearchResults</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Governed search over the discovery estate (P1 Search tier 1, 2026-07-11).

Case-insensitive substring over dataset NAMES, NAMESPACES, governance TAGS, and the CURRENT
COLUMN inventory — each hit says WHY it matched (``name`` / ``namespace`` / ``tag:…`` /
``column:…``), so "which tables have an embedding column" and "what's in layer=gold" are one
query. Governance is identical to ``/datasets``: the visibility filter runs over the FULL hit
set BEFORE the limit, so search can never disclose (or even count) tables outside the caller's
reach. 📌 Tier 2 (Lance FTS + FLAT vector content search, the rask pattern) stays decision-
pinned in docs/DECISIONS.md §9 behind its measured recall gate — this tier is metadata-only
by design.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.discovery.search(
    q="q",
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

**q:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
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

## Query
<details><summary><code>client.query.<a href="src/fern/query/client.py#L38-L83">get_dataset_columns</a>(...) -> ColumnGraph</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The column-level lineage subgraph around ``name`` (#24) — the field-to-field analogue of
``/graph``, for a DAG view of how each column was produced.

``depth`` counts DATASET hops outward; 1 is the single-hop answer this returned before the
parameter existed, so every existing caller is unaffected. The bound is FastAPI's here AND the
repository's — governance below runs over whatever the walk returned, so a depth the service did
not agree to would enlarge the set being filtered, not the set being disclosed.

Nodes/edges touching a dataset the caller can't see are dropped (an edge needs BOTH endpoints'
datasets visible); ``name``'s own columns are always shown (the route gate authorized it).
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.query.get_dataset_columns(
    name="name",
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

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**depth:** `typing.Optional[int]` 
    
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

<details><summary><code>client.query.<a href="src/fern/query/client.py#L85-L131">get_column_downstream</a>(...) -> ColumnNeighbors</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Column-level impact (#24): the columns (transitively) derived from ``name.field``. Gated +
governed exactly like the column upstream view — related columns in datasets the caller can't see
are dropped.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.query.get_column_downstream(
    name="name",
    field="field",
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

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**field:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**depth:** `typing.Optional[int]` 
    
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

<details><summary><code>client.query.<a href="src/fern/query/client.py#L133-L182">get_column_upstream</a>(...) -> ColumnNeighbors</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Column-level provenance (#24): the columns ``name.field`` was (transitively) derived from.

Our deepest moat — field-to-field lineage a format-unaware catalog cannot derive. Gated on
``can_get_metadata`` for the owning ``name``; related columns whose *owning dataset* the caller can't
see are dropped (a column has no ACL of its own — it inherits its table's), closing the same
transitive-disclosure hole at column resolution. Auth off → pass-through.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.query.get_column_upstream(
    name="name",
    field="field",
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

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**field:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**depth:** `typing.Optional[int]` 
    
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

<details><summary><code>client.query.<a href="src/fern/query/client.py#L184-L216">get_creator</a>(...) -> Creator</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Who created ``name`` (the verified catalog principal). Gated on ``can_get_metadata``.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.query.get_creator(
    name="name",
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

**name:** `str` 
    
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

<details><summary><code>client.query.<a href="src/fern/query/client.py#L218-L257">get_downstream</a>(...) -> Neighbors</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

What derives from ``name`` (impact). Gated; non-visible related datasets are dropped.

``depth`` bounds the walk exactly as on `/upstream` — impact is the direction that fans OUT, so a
hub dataset is where an unbounded walk costs most.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.query.get_downstream(
    name="name",
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

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**depth:** `typing.Optional[int]` 
    
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

<details><summary><code>client.query.<a href="src/fern/query/client.py#L259-L311">get_graph</a>(...) -> LineageGraph</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The connected lineage subgraph around ``name`` (nodes + edges) for a DAG view.

``depth`` bounds the walk to that many hops in each direction, making this a ROOTED
NEIGHBOURHOOD rather than a whole connected component — the shape Marquez serves at
``/lineage?nodeId=&depth=N``. Omitted, the walk is unbounded, which is the previous behaviour and
still what an un-rooted caller wants.

Bounding here rather than in the client is the point: a UI depth control that filters an
already-fetched window cannot reach anything the window excluded, however small the depth.

`ge=1, le=MAX_WALK_DEPTH` is the FIRST of two guards and the one that answers the caller: a bad
depth is a 422 here rather than a 500 from the repository. The repository re-checks anyway,
because the hop range is interpolated into Cypher and that check must not depend on every caller
having gone through this route.

Nodes the caller may not see (and edges touching them) are dropped; the requested ``name``
is already authorized by the route gate.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.query.get_graph(
    name="name",
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

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**depth:** `typing.Optional[int]` 
    
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

<details><summary><code>client.query.<a href="src/fern/query/client.py#L313-L352">get_producers</a>(...) -> Producers</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The runs that wrote ``name`` — who / when / how. Gated on ``can_get_metadata``.

Bounded like ``/readers`` beside it: newest-first, so the page a caller gets is the part that
answers "what wrote this", and the tail it loses is history the run board serves instead.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.query.get_producers(
    name="name",
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

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
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

<details><summary><code>client.query.<a href="src/fern/query/client.py#L354-L395">get_readers</a>(...) -> Readers</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Who has READ ``name`` — the read-audit log's query surface (#41 was capture-only until now).

Owner/writer-gated (``require_write_access``, on TOP of the router's ``can_get_metadata``): an access
log reveals *who* touched a dataset, so only a data owner may audit it — a casual reader can trace the
dataset's provenance but not enumerate who else viewed it. Aggregated per principal (last read + count,
newest first). Empty when read-auditing is/was off (the log table exists but has no rows).
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.query.get_readers(
    name="name",
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

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
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

<details><summary><code>client.query.<a href="src/fern/query/client.py#L397-L442">get_reconcile</a>(...) -> ReconcileStatus</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Does the lineage graph agree with the **actual Lance file on storage**? (#23)

Our moat over format-unaware catalogs: because we own a Lance lakehouse we
read the real on-disk version and cross-check it against the version the graph recorded on the
``WROTE`` edge — surfacing a write that bypassed lineage (``storage_ahead``) or a lineage claim
with no data behind it (``missing_on_storage``). Gated on ``can_get_metadata`` for ``name``; the
Lance read runs in the threadpool so the blocking object-store I/O never stalls the event loop.

``versions_without_lineage`` is the axis the version comparison cannot answer: it compares two
MAXIMA, so a write whose event was lost and which a later write superseded leaves both equal and the
dataset reports ``in_sync``. Measured on the live estate 2026-09-11, ``bronze$events`` answered
in_sync at 87/87 with four retained versions carrying no lineage at all. READ-ONLY here — this door
reports the holes and the cron sweep is what recovers them, so an operator asking a question never
mutates the graph as a side effect.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.query.get_reconcile(
    name="name",
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

**name:** `str` 
    
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

<details><summary><code>client.query.<a href="src/fern/query/client.py#L444-L488">get_schema</a>(...) -> DatasetSchema</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The persisted column schema for ``name`` — at ``?version=N`` if given, else the latest. (#24)

Captured from the standard ``SchemaDatasetFacet`` at ingest and stored per-version on the ``WROTE``
edge (previously the facet was received and discarded). Gated on ``can_get_metadata`` for ``name``;
this is the prerequisite for column-level lineage and powers schema-diffing between Lance versions.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.query.get_schema(
    name="name",
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

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[int]` 
    
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

<details><summary><code>client.query.<a href="src/fern/query/client.py#L490-L536">get_upstream</a>(...) -> Neighbors</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

What ``name`` was derived from (provenance).

Gated on ``can_get_metadata`` for ``name``; related datasets the caller may not see are
dropped so the graph can't disclose tables outside its reach.

``depth`` bounds the walk, the same shape and ceiling `/graph` already offers. The repository has
accepted it since the helper landed; only this door never declared it, so every request reached the
unbounded `*1..` statement whatever the caller wanted. Omitted it stays unbounded — the previous
behaviour, and what an un-rooted caller asks for — but it is now a caller's CHOICE rather than the
only thing the door can do. `age.py` names that unbounded path over a grown graph as the reason a
pooled connection cannot be pinned.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.query.get_upstream(
    name="name",
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

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**depth:** `typing.Optional[int]` 
    
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

<details><summary><code>client.query.<a href="src/fern/query/client.py#L538-L595">get_events</a>(...) -> Events</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The most-recent ingested OpenLineage events (newest first) — the Marquez-style event feed.

**Durable** (read from Postgres, survives restart / replica-shared) and **governed**: when auth is
on the feed is filtered like the per-dataset reads — an event is shown only if the caller
``can_get_metadata`` on *every* dataset it references (and a dataset-less event is hidden), so the
audit feed never discloses a table outside the caller's reach. Auth off → pass-through. (#22)

Pagination (additive, defaults = the old behavior): ``after`` = keyset cursor (the previous
page's ``next_cursor``); ``limit`` ≤ 500 (server-capped); ``summary=true`` drops the full-JSONB
``event`` payload at the SQL layer. The governance filter ALWAYS runs before the slice —
pagination can never disclose a hidden row's CONTENT. ``next_cursor`` is a WINDOW FLOOR, not
necessarily a visible row's seq (on a hidden-dense page it is the fetch window's last seq —
exclusive, so the hidden row itself is never returned; bare seq numbers were already inferable
from gaps in the pre-pagination feed, so this adds no new disclosure class — reviewed
2026-07-11).
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.query.get_events()

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

**after:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**summary:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.query.<a href="src/fern/query/client.py#L597-L663">get_events_projection</a>(...) -> Events</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The feed WITHOUT the per-dataset filter, for a caller that observes the estate (§ G1).

WHY A SECOND DOOR RATHER THAN A FLAG ON THE FIRST. `/events` is governed per dataset, which is
right for a person: an event naming a table you cannot see must not disclose it. It is wrong for a
SERVICE that has to reconcile the whole estate, and the wrongness is silent in both directions —
measured on this estate 2026-09-09, a run that demonstrably exists answered **404** to a service
principal, and its inputs answered **200 with an empty list**. A walker sees "nothing here", and an
estate with no work looks identical to an estate it cannot see.

THE SERVICE IS NOT THE DISCLOSURE BOUNDARY, and that is what makes this sound rather than a hole.
A reconciler reads the feed to decide who to TELL; the telling is gated per subject at delivery
(`can_be_notified`), which is the check that actually protects a person's inbox. Filtering the
reconciler's own view protects nobody and only guarantees it cannot find the events it exists to
catch. `can_be_notified` stays the sole disclosure gate; this door moves the estate-read decision
to the rung that means "may observe the estate".

`can_observe_events` ON THE ROOT OBJECT — the same rung `POST /v1/projects` and `POST /v1/stores`
already gate on, so an estate privilege means one thing everywhere. It is `owner` on the root in
`model.fga`, so nobody holds it by accident and granting it is a deliberate act.

Identical shape to `/events` otherwise — same keyset cursor, same cap, same `summary` — so a caller
can move between the two without a second client. `oldest_seq` is reported here too: a walker whose
cursor falls below it lost a window to the prune, which is the one signal that distinguishes
"caught up" from "rows went past me".
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.query.get_events_projection()

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

**after:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**summary:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.query.<a href="src/fern/query/client.py#L665-L711">get_runs</a>(...) -> Runs</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Live run-status board — each run's current state folded onto its ``(:Run)`` node in Apache AGE.

**Durable** (survives restart / replica-shared) and **governed** like ``/events`` and the per-dataset
reads: a run is shown only if the caller ``can_get_metadata`` on every dataset it wrote, so the board
can't enumerate dataset names / creators / errors outside the caller's reach. Auth off → pass-through.

**BOUNDED AT THE QUERY, newest first.** The board is polled every two seconds and the graph has no run
retention, so an unbounded read grows without limit: measured live 2026-09-07 it answered 5,122 runs /
2.65 MB, against 272 rows fifteen days earlier. A limit applied here rather than in the Cypher would
change nothing — the cost is the READ, and asking for one run took 2.5 s while asking for a hundred
took 1.4 s.

The over-fetch window is ``/events``' answer, for the same reason: governance drops rows AFTER the
read, so a page cut to size first comes back short — or empty — while visible runs sit below it. With
auth off the filter is pass-through and the headroom is pure waste, so the fetch is exactly ``limit``.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.query.get_runs()

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

**limit:** `typing.Optional[int]` 
    
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

<details><summary><code>client.query.<a href="src/fern/query/client.py#L713-L755">get_run</a>(...) -> RunStatus</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

ONE run's state — the point read the board is not.

"Is this run in the graph?" was answered by downloading `/runs` and scanning it, which is
O(estate) for a one-row question and became WRONG once the board was bounded: a run outside the
newest page is missing from the response while present in the graph, so the caller concluded
ABSENT and reported a provenance defect that did not exist.

GOVERNED EXACTLY LIKE THE BOARD — visible only if the caller `can_get_metadata` on every dataset
the run wrote — and an invisible run answers 404, the same as one that is not there. Deliberately
the same answer: distinguishing them would let a caller enumerate runs it may not see by watching
which ids give a different refusal.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.query.get_run(
    run_id="run_id",
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

**run_id:** `str` 
    
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

<details><summary><code>client.query.<a href="src/fern/query/client.py#L757-L795">get_run_inputs</a>(...) -> RunInputs</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The inputs a run consumed, each with the version it PINNED — the per-run reproducibility answer.

The pinned version rides the graph's ``READ`` edge (the Ray TRAIN job pins every feature — #115
D1); this endpoint is its API surface (before, Cypher-only). Kept OFF the 2s-polled ``/runs`` board
— it's a per-run drill-in, and adding a per-run READ-edge fetch to the board would be N+1 on the hot
path. Governed like every read: an input the caller can't ``can_get_metadata`` is dropped (an empty
list for a run the caller can't see into is itself non-disclosing). Auth off → pass-through.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.query.get_run_inputs(
    run_id="run_id",
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

**run_id:** `str` 
    
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

## Governance
<details><summary><code>client.governance.<a href="src/fern/governance/client.py#L29-L66">set_description</a>(...) -> DatasetGovernance</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set the dataset's description (an empty string clears it).
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.governance.set_description(
    name="name",
    description="description",
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

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` 
    
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

<details><summary><code>client.governance.<a href="src/fern/governance/client.py#L68-L102">get_governance</a>(...) -> DatasetGovernance</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The dataset's curated tags + description with last-writer attribution (who/when per field).
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.governance.get_governance(
    name="name",
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

**name:** `str` 
    
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

<details><summary><code>client.governance.<a href="src/fern/governance/client.py#L104-L141">add_tag</a>(...) -> DatasetGovernance</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add one governance tag (idempotent — re-adding an existing tag is a no-op re-stamp).
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.governance.add_tag(
    name="name",
    tag="tag",
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

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**tag:** `str` 
    
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

<details><summary><code>client.governance.<a href="src/fern/governance/client.py#L143-L184">remove_tag</a>(...) -> DatasetGovernance</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove one governance tag (idempotent — removing an absent tag is a no-op re-stamp).

Deliberately unvalidated: removal only filters an existing element out of storage, so any string is
safe — and it lets a curator purge a non-conforming tag (e.g. an old producer label) that the add
path would refuse.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.governance.remove_tag(
    name="name",
    tag="tag",
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

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**tag:** `str` 
    
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

## Demo
<details><summary><code>client.demo.<a href="src/fern/demo/client.py#L26-L61">demo_datasets</a>() -> DemoDatasets</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The medallion datasets as they currently exist on S3 — schema per Lance version + rows.

GOVERNED (audit: this endpoint reads real medallion schemas/row-counts + gold's lineage JSONB from S3
with the SERVICE root credentials, so it must not disclose a dataset the caller cannot see). Every
other lineage read gates on ``can_get_metadata``; this does the same via the shared batch filter —
ONE ``batch_check`` over the layout, not a per-dataset round-trip loop (F-LIN-13). The ladder is
unchanged: 401 unauthenticated / 503 FGA unwired propagate; a denied dataset is dropped, not fatal.
FGA off → pass-through (the dev demo).
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.demo.demo_datasets()

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

## Health
<details><summary><code>client.health.<a href="src/fern/health/client.py#L27-L53">livez</a>() -> Liveness</code></summary>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.health.livez()

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

<details><summary><code>client.health.<a href="src/fern/health/client.py#L55-L81">readyz</a>() -> Readiness</code></summary>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.health.readyz()

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

