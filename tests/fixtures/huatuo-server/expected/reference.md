# Reference
<details><summary><code>client.<a href="src/fern/client.py">get_open_api</a>() -> typing.Dict[str, typing.Any]</code></summary>
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

client.get_open_api()

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

## readiness
<details><summary><code>client.readiness.<a href="src/fern/readiness/client.py">get_readiness</a>()</code></summary>
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

client.readiness.get_readiness()

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

## profiling
<details><summary><code>client.profiling.<a href="src/fern/profiling/client.py">list_profiling_jobs</a>(...) -> ProfilingJobListResponse</code></summary>
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

client.profiling.list_profiling_jobs()

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

**offset:** `typing.Optional[int]` 
    
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

<details><summary><code>client.profiling.<a href="src/fern/profiling/client.py">create_profiling_job</a>(...) -> ProfilingJobResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ProfilingLanguage, ProfilingMode, ApisV1ComponentsObservationScope, ProfilingType

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.profiling.create_profiling_job(
    duration_seconds=1000000,
    hostname="hostname",
    language=ProfilingLanguage.C,
    mode=ProfilingMode.ON_CPU,
    scope=ApisV1ComponentsObservationScope.HOST,
    type=ProfilingType.CPU,
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

**duration_seconds:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**hostname:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**language:** `ProfilingLanguage` 
    
</dd>
</dl>

<dl>
<dd>

**mode:** `ProfilingMode` 
    
</dd>
</dl>

<dl>
<dd>

**scope:** `ApisV1ComponentsObservationScope` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `ProfilingType` 
    
</dd>
</dl>

<dl>
<dd>

**binary_match_path:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**container_id:** `typing.Optional[str]` 
    
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

<details><summary><code>client.profiling.<a href="src/fern/profiling/client.py">get_profiling_capabilities</a>() -> ProfilingCapabilitiesResponse</code></summary>
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

client.profiling.get_profiling_capabilities()

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

<details><summary><code>client.profiling.<a href="src/fern/profiling/client.py">get_profile_label_names</a>() -> typing.Iterator[bytes]</code></summary>
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

client.profiling.get_profile_label_names()

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

<details><summary><code>client.profiling.<a href="src/fern/profiling/client.py">get_profile_label_values</a>() -> typing.Iterator[bytes]</code></summary>
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

client.profiling.get_profile_label_values()

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

<details><summary><code>client.profiling.<a href="src/fern/profiling/client.py">get_profile_types</a>() -> typing.Iterator[bytes]</code></summary>
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

client.profiling.get_profile_types()

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

<details><summary><code>client.profiling.<a href="src/fern/profiling/client.py">select_merge_stacktraces</a>() -> typing.Iterator[bytes]</code></summary>
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

client.profiling.select_merge_stacktraces()

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

<details><summary><code>client.profiling.<a href="src/fern/profiling/client.py">get_profiling_job</a>(...) -> ProfilingJobResponse</code></summary>
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

client.profiling.get_profiling_job(
    request_id="request_id",
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

**request_id:** `str` 
    
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

<details><summary><code>client.profiling.<a href="src/fern/profiling/client.py">get_raw_profiles</a>(...) -> RawProfilePageResponse</code></summary>
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

client.profiling.get_raw_profiles(
    request_id="request_id",
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

**request_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
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

<details><summary><code>client.profiling.<a href="src/fern/profiling/client.py">stop_profiling_job</a>(...) -> ProfilingJobResponse</code></summary>
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

client.profiling.stop_profiling_job(
    request_id="request_id",
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

**request_id:** `str` 
    
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

## tracing
<details><summary><code>client.tracing.<a href="src/fern/tracing/client.py">list_tracing_jobs</a>(...) -> TracingJobListResponse</code></summary>
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

client.tracing.list_tracing_jobs()

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

**offset:** `typing.Optional[int]` 
    
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

<details><summary><code>client.tracing.<a href="src/fern/tracing/client.py">create_tracing_job</a>(...) -> TracingJobResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ApisV1ComponentsObservationScope, TracingType

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.tracing.create_tracing_job(
    duration_seconds=1000000,
    hostname="hostname",
    scope=ApisV1ComponentsObservationScope.HOST,
    type=TracingType.NETWORKING_DROP,
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

**duration_seconds:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**hostname:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**scope:** `ApisV1ComponentsObservationScope` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `TracingType` 
    
</dd>
</dl>

<dl>
<dd>

**container_id:** `typing.Optional[str]` 
    
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

<details><summary><code>client.tracing.<a href="src/fern/tracing/client.py">get_tracing_capabilities</a>() -> TracingCapabilitiesResponse</code></summary>
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

client.tracing.get_tracing_capabilities()

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

<details><summary><code>client.tracing.<a href="src/fern/tracing/client.py">get_tracing_job</a>(...) -> TracingJobResponse</code></summary>
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

client.tracing.get_tracing_job(
    request_id="request_id",
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

**request_id:** `str` 
    
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

<details><summary><code>client.tracing.<a href="src/fern/tracing/client.py">stop_tracing_job</a>(...) -> TracingJobResponse</code></summary>
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

client.tracing.stop_tracing_job(
    request_id="request_id",
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

**request_id:** `str` 
    
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

