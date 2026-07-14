# Reference
## Webhooks
<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">event_logs_all</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List event logs
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
    api_key="YOUR_API_KEY",
)
client.webhooks.event_logs_all(
    apideck_app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
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

**apideck_app_id:** `str` — The ID of your Unify application
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return. Minimum 1, Maximum 200, Default 20
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[WebhookEventLogsFilter]` — Filter results
    
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

<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">resolve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Resolve a webhook based on lookup_id and then execute it
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
    api_key="YOUR_API_KEY",
)
client.webhooks.resolve(
    id="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Ijk2MDAwYzIzLWI1NmItNGRlOC1iZmEzLTMxNTAzMTE3YzBmNyJ9.rAXnsmZ4O7eF0aDwdflkxAJQwMUfWs5989WfmspNZ6Q",
    service_id="factorialhr",
    e="Employees::Events::EmployeeCreated",
    request={"key": "value"},
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

**id:** `str` — JWT Webhook token that represents the connection lookupId. Signed so we know source came from us
    
</dd>
</dl>

<dl>
<dd>

**service_id:** `str` — Service provider ID.
    
</dd>
</dl>

<dl>
<dd>

**request:** `WebhooksResolveRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**e:** `typing.Optional[str]` — The name of downstream event when connector does not supply in body or header
    
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

<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">all_</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all webhook subscriptions
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
    api_key="YOUR_API_KEY",
)
client.webhooks.all_(
    apideck_app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
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

**apideck_app_id:** `str` — The ID of your Unify application
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return. Minimum 1, Maximum 200, Default 20
    
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

<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">add</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a webhook subscription to receive events
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
from fern import FernApi, Status, UnifiedApiId, WebhookEventType

client = FernApi(
    api_key="YOUR_API_KEY",
)
client.webhooks.add(
    apideck_app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    delivery_url="https://example.com/my/webhook/endpoint",
    events=[
        WebhookEventType.VAULT_CONNECTION_CREATED,
        WebhookEventType.VAULT_CONNECTION_UPDATED,
    ],
    status=Status.ENABLED,
    unified_api=UnifiedApiId.ACCOUNTING,
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

**apideck_app_id:** `str` — The ID of your Unify application
    
</dd>
</dl>

<dl>
<dd>

**delivery_url:** `DeliveryUrl` 
    
</dd>
</dl>

<dl>
<dd>

**events:** `typing.Sequence[WebhookEventType]` — The list of subscribed events for this webhook. [`*`] indicates that all events are enabled.
    
</dd>
</dl>

<dl>
<dd>

**status:** `Status` 
    
</dd>
</dl>

<dl>
<dd>

**unified_api:** `UnifiedApiId` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[Description]` 
    
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

<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">one</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the webhook subscription details
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
    api_key="YOUR_API_KEY",
)
client.webhooks.one(
    id="id",
    apideck_app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
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

**id:** `str` — JWT Webhook token that represents the unifiedApi and applicationId associated to the event source.
    
</dd>
</dl>

<dl>
<dd>

**apideck_app_id:** `str` — The ID of your Unify application
    
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

<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a webhook subscription
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
    api_key="YOUR_API_KEY",
)
client.webhooks.delete(
    id="id",
    apideck_app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
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

**id:** `str` — JWT Webhook token that represents the unifiedApi and applicationId associated to the event source.
    
</dd>
</dl>

<dl>
<dd>

**apideck_app_id:** `str` — The ID of your Unify application
    
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

<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a webhook subscription
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
    api_key="YOUR_API_KEY",
)
client.webhooks.update(
    id="id",
    apideck_app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
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

**id:** `str` — JWT Webhook token that represents the unifiedApi and applicationId associated to the event source.
    
</dd>
</dl>

<dl>
<dd>

**apideck_app_id:** `str` — The ID of your Unify application
    
</dd>
</dl>

<dl>
<dd>

**delivery_url:** `typing.Optional[DeliveryUrl]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[Description]` 
    
</dd>
</dl>

<dl>
<dd>

**events:** `typing.Optional[typing.Sequence[WebhookEventType]]` — The list of subscribed events for this webhook. [`*`] indicates that all events are enabled.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[Status]` 
    
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

<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">execute</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Execute a webhook
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
    api_key="YOUR_API_KEY",
)
client.webhooks.execute(
    id="id",
    service_id="factorialhr",
    request={"key": "value"},
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

**id:** `str` — JWT Webhook token that represents the unifiedApi and applicationId associated to the event source.
    
</dd>
</dl>

<dl>
<dd>

**service_id:** `str` — Service provider ID.
    
</dd>
</dl>

<dl>
<dd>

**request:** `WebhooksExecuteRequestBody` 
    
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

<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">short_execute</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Execute a webhook
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
    api_key="YOUR_API_KEY",
)
client.webhooks.short_execute(
    id="id",
    service_id="factorialhr",
    l_id="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjA3NWUwNmEzLTUwNzUtNDY3Yi1hNTk5LWVkNmM5YTg5NTYyOCJ9._ppKdmBaCB2RHjBTifMNP2xKNeLBfNPim2CiHSUd0Zg",
    e="Employees::Events::EmployeeCreated",
    request={"key": "value"},
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

**id:** `str` — JWT Webhook token that represents the unifiedApi and applicationId associated to the event source.
    
</dd>
</dl>

<dl>
<dd>

**service_id:** `str` — Service provider ID.
    
</dd>
</dl>

<dl>
<dd>

**request:** `WebhooksShortExecuteRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**l_id:** `typing.Optional[str]` — Unique identifier to used to look up consumer/connection when receiving connector events from downstream.
    
</dd>
</dl>

<dl>
<dd>

**e:** `typing.Optional[str]` — The name of downstream event when connector does not supply in body or header
    
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

