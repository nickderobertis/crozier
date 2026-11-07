# Reference
## Ping
<details><summary><code>client.ping.<a href="src/fern/ping/client.py">ping_ping</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Ping.
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

client.ping.ping_ping()

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

<details><summary><code>client.ping.<a href="src/fern/ping/client.py">ping_headping</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Ping headers.
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

client.ping.ping_headping()

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

## Prerecordings
<details><summary><code>client.prerecordings.<a href="src/fern/prerecordings/client.py">prerecordings_event_start_download</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Download a prerecording.
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
import datetime

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.prerecordings.prerecordings_event_start_download(
    event="event",
    start=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
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

**event:** `DownloadRequestEvent` 
    
</dd>
</dl>

<dl>
<dd>

**start:** `DownloadRequestStart` — Datetime without timezone.
    
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

<details><summary><code>client.prerecordings.<a href="src/fern/prerecordings/client.py">prerecordings_event_start_upload</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload a prerecording.
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
import datetime

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.prerecordings.prerecordings_event_start_upload(
    event="event",
    start=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    request="string",
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

**event:** `UploadRequestEvent` 
    
</dd>
</dl>

<dl>
<dd>

**start:** `UploadRequestStart` — Datetime without timezone.
    
</dd>
</dl>

<dl>
<dd>

**request:** `bytes` 
    
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

<details><summary><code>client.prerecordings.<a href="src/fern/prerecordings/client.py">prerecordings_event_start_delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a prerecording.
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
import datetime

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.prerecordings.prerecordings_event_start_delete(
    event="event",
    start=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
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

**event:** `DeleteRequestEvent` 
    
</dd>
</dl>

<dl>
<dd>

**start:** `DeleteRequestStart` — Datetime without timezone.
    
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

<details><summary><code>client.prerecordings.<a href="src/fern/prerecordings/client.py">prerecordings_event_start_headdownload</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Download prerecording headers.
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
import datetime

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.prerecordings.prerecordings_event_start_headdownload(
    event="event",
    start=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
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

**event:** `HeadDownloadRequestEvent` 
    
</dd>
</dl>

<dl>
<dd>

**start:** `HeadDownloadRequestStart` — Datetime without timezone.
    
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

<details><summary><code>client.prerecordings.<a href="src/fern/prerecordings/client.py">prerecordings_event_list</a>(...) -> ListResponseResults</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List prerecordings.
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

client.prerecordings.prerecordings_event_list(
    event="event",
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

**event:** `ListRequestEvent` 
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[PrerecordingsEventListRequestAfter]` — Only list prerecordings after this datetime (in event timezone).
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[PrerecordingsEventListRequestBefore]` — Only list prerecordings before this datetime (in event timezone).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[PrerecordingsEventListRequestLimit]` — Maximum number of prerecordings to return. Default is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[PrerecordingsEventListRequestOffset]` — Number of prerecordings to skip.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[PrerecordingsEventListRequestOrder]` — Order to apply to the results.
    
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

## Sse
<details><summary><code>client.sse.<a href="src/fern/sse/client.py">sse_subscribe</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a stream of Server-Sent Events.
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

client.sse.sse_subscribe()

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

**types:** `typing.Optional[SseSubscribeRequestTypes]` — Types of events to subscribe to.
    
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

## Test
<details><summary><code>client.test.<a href="src/fern/test/client.py">test_test</a>(...) -> TestResponseResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Test.
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

client.test.test_test()

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

**parameters:** `typing.Optional[TestTestRequestParameters]` — Parameters for testing.
    
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

