# Reference
## Service
<details><summary><code>client.service.<a href="src/fern/service/client.py">get_root</a>() -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of paths available from this API.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.service.get_root()

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

<details><summary><code>client.service.<a href="src/fern/service/client.py">head_root</a>() -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return root path headers
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.service.head_root()

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

<details><summary><code>client.service.<a href="src/fern/service/client.py">get_service</a>() -> Service</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Provide information about the service.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.service.get_service()

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

<details><summary><code>client.service.<a href="src/fern/service/client.py">post_service</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the service info.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.service.post_service()

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

**name:** `typing.Optional[str]` — The service instance name
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The service instance description
    
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

<details><summary><code>client.service.<a href="src/fern/service/client.py">head_service</a>() -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return service path headers
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.service.head_service()

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

<details><summary><code>client.service.<a href="src/fern/service/client.py">get_storage_backends</a>() -> StorageBackendsList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Provide information about the storage backends available on this service instance. These are populated on deployment of the service instance.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.service.get_storage_backends()

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

<details><summary><code>client.service.<a href="src/fern/service/client.py">head_storage_backends</a>() -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return storage backends path headers
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.service.head_storage_backends()

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

## Webhooks
<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">get_webhooks</a>(...) -> typing.List[WebhookGet]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the list of registered webhook URLs.
Service implementations SHOULD take steps to avoid displaying URLs to users other than those who have suitable permissions (e.g. the owning user).
Availability of this endpoint is indicated by the name "webhooks" appearing in the `event_stream_mechanisms` list on the [/service](#/operations/GET_service) endpoint.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.webhooks.get_webhooks()

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

**tag_name:** `typing.Optional[UrlTagList]` 

Filter on webhooks that have a tag named {name} with a value in the given comma-separated list of values.
The {name} and the value MUST be URL encoded where special characters are present.
Where the tag's value is a string, at least one of the given values will match.
Where the tag's value is an array, at least one value in the array will match at least one of the given values.
Partial string matches of the values are not valid.
    
</dd>
</dl>

<dl>
<dd>

**tag_exists_name:** `typing.Optional[bool]` 

Filter on webhooks that have a tag named {name} regardless of value.
The {name} MUST be URL encoded where special characters are present.
If set to true then the presence of the tag is filtered for.
If set to false then its absence is.
If left out then no filtering on tag presence is performed.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[str]` — Opaque string used by backend to access a specific page of results. Clients should read the next URL from the `Link` header returned with responses, or use value of the returned X-Paging-NextKey header. If not supplied, the first page is accessed. Service implementations should ensure a consistent sort order is applied to pages of results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Restrict the response to the specified number of results. Service implementations may specify their own default and maximum for the limit
    
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

<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">post_webhooks</a>(...) -> WebhookGet</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Register to receive event notifications as webhooks on a specified URL. Webhook messages will conform to the
format in the `webhooks` section of the API docs, depending on the event type (as defined in the same section).
Availability of this endpoint is indicated by the name "webhooks" appearing in the `event_stream_mechanisms`
list on the service endpoint.

HTTP requests from the service SHOULD include a `api_key_name` header with the 'api_key_value' value. Clients SHOULD verify this against the value they provided when registering the webhook.

API implementations MAY partially support event filtering and transformations.
API implementations SHALL return a 400 response code if the filtering or transformation specified in the request is not supported.

API implementations SHOULD consider the security implementations of providing webhooks, and include appropriate mitigations against Server Side Request Forgery (SSRF) attacks and similar. API implementations SHOULD take appropriate steps to authorize the modification of existing webhooks. This may take the form of RBAC, or ABAC.
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
from fern import FernApi, WebhookEventsItem
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.webhooks.post_webhooks(
    url="url",
    events=[
        WebhookEventsItem.FLOWS_CREATED
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

**url:** `str` — The URL to which the service instance should make HTTP POST requests with event data
    
</dd>
</dl>

<dl>
<dd>

**events:** `typing.List[WebhookEventsItem]` — List of event types to receive
    
</dd>
</dl>

<dl>
<dd>

**api_key_name:** `typing.Optional[str]` — The HTTP header name that is added to the event POST
    
</dd>
</dl>

<dl>
<dd>

**flow_ids:** `typing.Optional[typing.List[Uuid]]` — Limit Flow and Flow Segment events to Flows in the given list of Flow IDs
    
</dd>
</dl>

<dl>
<dd>

**source_ids:** `typing.Optional[typing.List[Uuid]]` — Limit Flow, Flow Segment and Source events to Sources in the given list of Source IDs
    
</dd>
</dl>

<dl>
<dd>

**flow_collected_by_ids:** `typing.Optional[typing.List[Uuid]]` — Limit Flow and Flow Segment events to those with Flow that is collected by a Flow Collection in the given list of Flow Collection IDs
    
</dd>
</dl>

<dl>
<dd>

**source_collected_by_ids:** `typing.Optional[typing.List[Uuid]]` — Limit Flow, Flow Segment and Source events to those with Source that is collected by a Source Collection in the given list of Source Collection IDs
    
</dd>
</dl>

<dl>
<dd>

**accept_get_urls:** `typing.Optional[typing.List[str]]` — List of labels of URLs to include in the `get_urls` property in `flows/segments_added` events. Where multiple `get_urls` filter query parameters are provided, the included `get_urls` will match all filters. This option is the same as the `accept_get_urls` query parameter for the [/flows/{flowId}/segments](#/operations/GET_flows-flowId-segments) API endpoint, except that the labels are represented using a JSON array rather than a (comma separated list) string.
    
</dd>
</dl>

<dl>
<dd>

**accept_storage_ids:** `typing.Optional[typing.List[Uuid]]` — List of labels of `storage_id`s to include in the `get_urls` property in `flows/segments_added` events. Where multiple `get_urls` filter query parameters are provided, the included `get_urls` will match all filters. This option is the same as the `accept_storage_ids` query parameter for the [/flows/{flowId}/segments](#/operations/GET_flows-flowId-segments) API endpoint, except that the IDs are represented using a JSON array rather than a (comma separated list) string.
    
</dd>
</dl>

<dl>
<dd>

**presigned:** `typing.Optional[bool]` — Whether to include presigned/non-presigned URLs in the `get_urls` property in `flows/segments_added` events. Where multiple `get_urls` filter query parameters are provided, the included `get_urls` will match all filters. This option is the same as the `presigned` query parameter for the [/flows/{flowId}/segments](#/operations/GET_flows-flowId-segments) API endpoint.
    
</dd>
</dl>

<dl>
<dd>

**verbose_storage:** `typing.Optional[bool]` — Whether to include storage metadata in the `get_urls` property in `flows/segments_added` events. This option is the same as the `verbose_storage` query parameter for the [/flows/{flowId}/segments](#/operations/GET_flows-flowId-segments) API endpoint.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[Tags]` 
    
</dd>
</dl>

<dl>
<dd>

**api_key_value:** `typing.Optional[str]` — The value that the HTTP header 'api_key_name' will be set to
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[WebhookPostStatus]` — Status of the Webhook. `created` will register the webhook in the created state and the service instance will attempt to start sending events. `disabled` will register the webhook in a disabled state and will not send events. Assumed to be `created` if not set.
    
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

<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">head_webhooks</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return webhooks path headers
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.webhooks.head_webhooks()

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

**tag_name:** `typing.Optional[UrlTagList]` 

Filter on webhooks that have a tag named {name} with a value in the given comma-separated list of values.
The {name} and the value MUST be URL encoded where special characters are present.
Where the tag's value is a string, at least one of the given values will match.
Where the tag's value is an array, at least one value in the array will match at least one of the given values.
Partial string matches of the values are not valid.
    
</dd>
</dl>

<dl>
<dd>

**tag_exists_name:** `typing.Optional[bool]` 

Filter on webhooks that have a tag named {name} regardless of value.
The {name} MUST be URL encoded where special characters are present.
If set to true then the presence of the tag is filtered for.
If set to false then its absence is.
If left out then no filtering on tag presence is performed.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[str]` — Opaque string used by backend to access a specific page of results. Clients should read the next URL from the `Link` header returned with responses, or use value of the returned X-Paging-NextKey header. If not supplied, the first page is accessed. Service implementations should ensure a consistent sort order is applied to pages of results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Restrict the response to the specified number of results. Service implementations may specify their own default and maximum for the limit
    
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

<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">get_webhooks_webhook_id</a>(...) -> WebhookGet</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the details of a webhook. Service implementations SHOULD take steps to avoid displaying URLs to users other than those who have suitable permissions (e.g. the owning user).
Availability of this endpoint is indicated by the name "webhooks" appearing in the `event_stream_mechanisms` list on the [`/service`](#/operations/GET_service) endpoint.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.webhooks.get_webhooks_webhook_id(
    webhook_id="webhookId",
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

**webhook_id:** `Uuid` — The Webhook identifier.
    
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

<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">put_webhooks</a>(...) -> WebhookGet</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the configuration of an existing webhook.

Webhook messages will conform to the format in the `webhooks` section of the API docs, depending on the event type (as defined in the same section).
Availability of this endpoint is indicated by the name "webhooks" appearing in the `event_stream_mechanisms` list on the [`/service`](#/operations/GET_service) endpoint.

HTTP events sent by the service to a client webhook's endpoint SHOULD include a `api_key_name` header with the 'api_key_value' value.
Clients SHOULD verify this against the value they provided when registering the webhook.

Service implementations MAY partially support event filtering and transformations.
Service implementations SHALL return a 400 response code if the filtering or transformation specified in the request is not supported.

Service implementations SHOULD consider the security implications of providing webhooks, and include appropriate mitigations against Server Side Request Forgery (SSRF) attacks and similar.
Service implementations SHOULD take appropriate steps to authorize the modification of existing webhooks. 
This may take the form of RBAC, or ABAC.
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
from fern import FernApi, WebhookEventsItem
from fern.environment import FernApiEnvironment
from fern.webhooks import WebhookPutStatus

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.webhooks.put_webhooks(
    webhook_id="webhookId",
    id="id",
    url="url",
    events=[
        WebhookEventsItem.FLOWS_CREATED
    ],
    status=WebhookPutStatus.CREATED,
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

**webhook_id:** `Uuid` — The Webhook identifier.
    
</dd>
</dl>

<dl>
<dd>

**id:** `Uuid` — Webhook identifier
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` — The URL to which the service instance should make HTTP POST requests with event data
    
</dd>
</dl>

<dl>
<dd>

**events:** `typing.List[WebhookEventsItem]` — List of event types to receive
    
</dd>
</dl>

<dl>
<dd>

**status:** `WebhookPutStatus` — Status of the Webhook. `created` indicates the webhook has been successfully registered but is yet to begin sending events or, depending on the service implementation, the worker responsible for sending the events has yet to start. `started` indicates the webhook is active and sending events. `disabled` indicates the webhook has been disabled by a client and is not currently sending events. `error` indicates an error condition has been encountered and the webhook has been disabled by the service instance. More information about the error condition will be indicated by the service instance in the `error` parameter. Service implementations SHOULD implement appropriate retries and only enter the `error` state when absolutely necesary. A webhook in the `error` or `disabled` state may be re-enabled by a client by setting the status to `created`. A webhook in the `created` or `started` state may be disabled by a client by setting the status to `disabled`. Attempting to transition an `error` status to `disabled` SHOULD be rejected.
    
</dd>
</dl>

<dl>
<dd>

**api_key_name:** `typing.Optional[str]` — The HTTP header name that is added to the event POST
    
</dd>
</dl>

<dl>
<dd>

**flow_ids:** `typing.Optional[typing.List[Uuid]]` — Limit Flow and Flow Segment events to Flows in the given list of Flow IDs
    
</dd>
</dl>

<dl>
<dd>

**source_ids:** `typing.Optional[typing.List[Uuid]]` — Limit Flow, Flow Segment and Source events to Sources in the given list of Source IDs
    
</dd>
</dl>

<dl>
<dd>

**flow_collected_by_ids:** `typing.Optional[typing.List[Uuid]]` — Limit Flow and Flow Segment events to those with Flow that is collected by a Flow Collection in the given list of Flow Collection IDs
    
</dd>
</dl>

<dl>
<dd>

**source_collected_by_ids:** `typing.Optional[typing.List[Uuid]]` — Limit Flow, Flow Segment and Source events to those with Source that is collected by a Source Collection in the given list of Source Collection IDs
    
</dd>
</dl>

<dl>
<dd>

**accept_get_urls:** `typing.Optional[typing.List[str]]` — List of labels of URLs to include in the `get_urls` property in `flows/segments_added` events. Where multiple `get_urls` filter query parameters are provided, the included `get_urls` will match all filters. This option is the same as the `accept_get_urls` query parameter for the [/flows/{flowId}/segments](#/operations/GET_flows-flowId-segments) API endpoint, except that the labels are represented using a JSON array rather than a (comma separated list) string.
    
</dd>
</dl>

<dl>
<dd>

**accept_storage_ids:** `typing.Optional[typing.List[Uuid]]` — List of labels of `storage_id`s to include in the `get_urls` property in `flows/segments_added` events. Where multiple `get_urls` filter query parameters are provided, the included `get_urls` will match all filters. This option is the same as the `accept_storage_ids` query parameter for the [/flows/{flowId}/segments](#/operations/GET_flows-flowId-segments) API endpoint, except that the IDs are represented using a JSON array rather than a (comma separated list) string.
    
</dd>
</dl>

<dl>
<dd>

**presigned:** `typing.Optional[bool]` — Whether to include presigned/non-presigned URLs in the `get_urls` property in `flows/segments_added` events. Where multiple `get_urls` filter query parameters are provided, the included `get_urls` will match all filters. This option is the same as the `presigned` query parameter for the [/flows/{flowId}/segments](#/operations/GET_flows-flowId-segments) API endpoint.
    
</dd>
</dl>

<dl>
<dd>

**verbose_storage:** `typing.Optional[bool]` — Whether to include storage metadata in the `get_urls` property in `flows/segments_added` events. This option is the same as the `verbose_storage` query parameter for the [/flows/{flowId}/segments](#/operations/GET_flows-flowId-segments) API endpoint.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[Tags]` 
    
</dd>
</dl>

<dl>
<dd>

**api_key_value:** `typing.Optional[str]` — The value that the HTTP header 'api_key_name' will be set to
    
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

<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">delete_webhooks_webhook_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the webhook. 
Availability of this endpoint is indicated by the name "webhooks" appearing in the `event_stream_mechanisms` list on the service endpoint.

Service implementations SHOULD consider the security implementations of providing webhooks, and include appropriate mitigations against Server Side Request Forgery (SSRF) attacks and similar. 
Service implementations SHOULD take appropriate steps to authorize the deleting of webhooks. 
This may take the form of RBAC, or ABAC.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.webhooks.delete_webhooks_webhook_id(
    webhook_id="webhookId",
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

**webhook_id:** `Uuid` — The Webhook identifier.
    
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

<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">head_webhooks_webhook_id</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return webhook path headers
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.webhooks.head_webhooks_webhook_id(
    webhook_id="webhookId",
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

**webhook_id:** `Uuid` — The Webhook identifier.
    
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

## Sources
<details><summary><code>client.sources.<a href="src/fern/sources/client.py">get_sources</a>(...) -> typing.List[Source]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the Sources registered in the TAMS service instance and their details.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sources.get_sources()

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

**label:** `typing.Optional[str]` — Filter on Sources that have the given label.
    
</dd>
</dl>

<dl>
<dd>

**tag_name:** `typing.Optional[UrlTagList]` 

Filter on Sources that have a tag named {name} with a value in the given comma-separated list of values.
The {name} and the value MUST be URL encoded where special characters are present.
Where the tag's value is a string, at least one of the given values will match.
Where the tag's value is an array, at least one value in the array will match at least one of the given values.
Partial string matches of the values are not valid.
    
</dd>
</dl>

<dl>
<dd>

**tag_exists_name:** `typing.Optional[bool]` 

Filter on Sources that have a tag named {name} regardless of value.
{name} MUST be URL encoded where special characters are present.
If set to true then the presence of the tag is filtered for.
If set to false then its absence is.
If left out then no filtering on tag presence is performed.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[ContentFormat]` — Filter on Source format.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[str]` — Opaque string used by backend to access a specific page of results. Clients should read the next URL from the `Link` header returned with responses, or use value of the returned X-Paging-NextKey header. If not supplied, the first page is accessed. Service implementations should ensure a consistent sort order is applied to pages of results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Restrict the response to the specified number of results. Service implementations may specify their own default and maximum for the limit
    
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

<details><summary><code>client.sources.<a href="src/fern/sources/client.py">head_sources</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return Sources path headers
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sources.head_sources()

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

**label:** `typing.Optional[str]` — Filter on Sources that have the given label.
    
</dd>
</dl>

<dl>
<dd>

**tag_name:** `typing.Optional[UrlTagList]` 

Filter on Sources that have a tag named {name} with a value in the given comma-separated list of values.
The {name} and the value MUST be URL encoded where special characters are present.
Where the tag's value is a string, at least one of the given values will match.
Where the tag's value is an array, at least one value in the array will match at least one of the given values.
Partial string matches of the values are not valid.
    
</dd>
</dl>

<dl>
<dd>

**tag_exists_name:** `typing.Optional[bool]` 

Filter on Sources that have a tag named {name} regardless of value.
{name} MUST be URL encoded where special characters are present.
If set to true then the presence of the tag is filtered for.
If set to false then its absence is.
If left out then no filtering on tag presence is performed.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[ContentFormat]` — Filter on Source format.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[str]` — Opaque string used by backend to access a specific page of results. Clients should read the next URL from the `Link` header returned with responses, or use value of the returned X-Paging-NextKey header. If not supplied, the first page is accessed. Service implementations should ensure a consistent sort order is applied to pages of results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Restrict the response to the specified number of results. Service implementations may specify their own default and maximum for the limit
    
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

<details><summary><code>client.sources.<a href="src/fern/sources/client.py">get_sources_source_id</a>(...) -> Source</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns Source metadata.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sources.get_sources_source_id(
    source_id="sourceId",
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

**source_id:** `Uuid` — The Source identifier.
    
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

<details><summary><code>client.sources.<a href="src/fern/sources/client.py">head_sources_source_id</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return Source headers
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sources.head_sources_source_id(
    source_id="sourceId",
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

**source_id:** `Uuid` — The Source identifier.
    
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

<details><summary><code>client.sources.<a href="src/fern/sources/client.py">get_sources_source_id_tags</a>(...) -> Tags</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the Source tags.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sources.get_sources_source_id_tags(
    source_id="sourceId",
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

**source_id:** `Uuid` — The Source identifier.
    
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

<details><summary><code>client.sources.<a href="src/fern/sources/client.py">head_sources_source_id_tags</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return Source tags path headers
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sources.head_sources_source_id_tags(
    source_id="sourceId",
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

**source_id:** `Uuid` — The Source identifier.
    
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

<details><summary><code>client.sources.<a href="src/fern/sources/client.py">get_sources_source_id_tags_name</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return the tag value associated with the tag name.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sources.get_sources_source_id_tags_name(
    source_id="sourceId",
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

**source_id:** `Uuid` — The Source identifier.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The tag name. {name} MUST be URL encoded where special characters are present.
    
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

<details><summary><code>client.sources.<a href="src/fern/sources/client.py">put_sources_source_id_tags_name</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or update the Source tag
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sources.put_sources_source_id_tags_name(
    source_id="sourceId",
    name="name",
    request="\"new_value\"\n",
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

**source_id:** `Uuid` — The Source identifier.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The tag name. {name} MUST be URL encoded where special characters are present.
    
</dd>
</dl>

<dl>
<dd>

**request:** `str` 
    
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

<details><summary><code>client.sources.<a href="src/fern/sources/client.py">delete_sources_source_id_tags_name</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a specific tag on a Source
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sources.delete_sources_source_id_tags_name(
    source_id="sourceId",
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

**source_id:** `Uuid` — The Source identifier.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The tag name. {name} MUST be URL encoded where special characters are present.
    
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

<details><summary><code>client.sources.<a href="src/fern/sources/client.py">head_sources_source_id_tags_name</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return Source tag path headers
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sources.head_sources_source_id_tags_name(
    source_id="sourceId",
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

**source_id:** `Uuid` — The Source identifier.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The tag name. {name} MUST be URL encoded where special characters are present.
    
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

<details><summary><code>client.sources.<a href="src/fern/sources/client.py">get_sources_source_id_description</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the Source description property. This should be a human-readable description that may be showed in detailed views of Sources. The description should be longer and more detailed than `label`.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sources.get_sources_source_id_description(
    source_id="sourceId",
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

**source_id:** `Uuid` — The Source identifier.
    
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

<details><summary><code>client.sources.<a href="src/fern/sources/client.py">put_sources_source_id_description</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or update the description property. This should be a human-readable description that may be showed in detailed views of Sources. The description should be longer and more detailed than `label`.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sources.put_sources_source_id_description(
    source_id="sourceId",
    request="\"Big Buck Bunny Movie\"\n",
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

**source_id:** `Uuid` — The Source identifier.
    
</dd>
</dl>

<dl>
<dd>

**request:** `str` 
    
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

<details><summary><code>client.sources.<a href="src/fern/sources/client.py">delete_sources_source_id_description</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the description property.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sources.delete_sources_source_id_description(
    source_id="sourceId",
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

**source_id:** `Uuid` — The Source identifier.
    
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

<details><summary><code>client.sources.<a href="src/fern/sources/client.py">head_sources_source_id_description</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return Source description path headers
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sources.head_sources_source_id_description(
    source_id="sourceId",
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

**source_id:** `Uuid` — The Source identifier.
    
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

<details><summary><code>client.sources.<a href="src/fern/sources/client.py">get_sources_source_id_label</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the Source label property. This should be a very short, human-readable label that may be displayed in listings of Sources.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sources.get_sources_source_id_label(
    source_id="sourceId",
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

**source_id:** `Uuid` — The Source identifier.
    
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

<details><summary><code>client.sources.<a href="src/fern/sources/client.py">put_sources_source_id_label</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or update the label property. This should be a very short, human-readable label that may be displayed in listings of Sources.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sources.put_sources_source_id_label(
    source_id="sourceId",
    request="\"Big Buck Bunny Movie\"\n",
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

**source_id:** `Uuid` — The Source identifier.
    
</dd>
</dl>

<dl>
<dd>

**request:** `str` 
    
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

<details><summary><code>client.sources.<a href="src/fern/sources/client.py">delete_sources_source_id_label</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the label property.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sources.delete_sources_source_id_label(
    source_id="sourceId",
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

**source_id:** `Uuid` — The Source identifier.
    
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

<details><summary><code>client.sources.<a href="src/fern/sources/client.py">head_sources_source_id_label</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return Source label path headers
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sources.head_sources_source_id_label(
    source_id="sourceId",
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

**source_id:** `Uuid` — The Source identifier.
    
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

## Flows
<details><summary><code>client.flows.<a href="src/fern/flows/client.py">get_flows</a>(...) -> typing.List[Flow]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the Flows registered in the TAMS service instance.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flows.get_flows()

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

**source_id:** `typing.Optional[Uuid]` — Filter on Source identifier.
    
</dd>
</dl>

<dl>
<dd>

**timerange:** `typing.Optional[Timerange]` — Filter on Flows that overlap the given timerange. An empty timerange returns Flows with no content.
    
</dd>
</dl>

<dl>
<dd>

**include_timerange:** `typing.Optional[bool]` — Third-party compatibility extension. Include each listed Flow's computed content timerange in the response.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[ContentFormat]` — Filter on Flow format.
    
</dd>
</dl>

<dl>
<dd>

**codec:** `typing.Optional[MimeType]` — Filter on Flow codec.
    
</dd>
</dl>

<dl>
<dd>

**label:** `typing.Optional[str]` — Filter on Flows that have the given label.
    
</dd>
</dl>

<dl>
<dd>

**tag_name:** `typing.Optional[UrlTagList]` 

Filter on flows that have a tag named {name} with a value in the given comma-separated list of values.
The {name} and the value MUST be URL encoded where special characters are present.
Where the tag's value is a string, at least one of the given values will match.
Where the tag's value is an array, at least one value in the array will match at least one of the given values.
Partial string matches of the values are not valid.
    
</dd>
</dl>

<dl>
<dd>

**tag_exists_name:** `typing.Optional[bool]` 

Filter on Flows that have a tag named {name} regardless of value.
{name} MUST be URL encoded where special characters are present.
If set to true then the presence of the tag is filtered for.
If set to false then its absence is.
If left out then no filtering on tag presence is performed.
    
</dd>
</dl>

<dl>
<dd>

**frame_width:** `typing.Optional[int]` — Filter on video Flows that have the given frame width.
    
</dd>
</dl>

<dl>
<dd>

**frame_height:** `typing.Optional[int]` — Filter on video Flows that have the given frame height.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[str]` — Opaque string used by backend to access a specific page of results. Clients should read the next URL from the `Link` header returned with responses, or use value of the returned X-Paging-NextKey header. If not supplied, the first page is accessed. Service implementations should ensure a consistent sort order is applied to pages of results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Restrict the response to the specified number of results. Service implementations may specify their own default and maximum for the limit
    
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

<details><summary><code>client.flows.<a href="src/fern/flows/client.py">head_flows</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return Flows path headers
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flows.head_flows()

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

**source_id:** `typing.Optional[Uuid]` — Filter on Source identifier.
    
</dd>
</dl>

<dl>
<dd>

**timerange:** `typing.Optional[Timerange]` — Filter on Flows that overlap the given timerange.
    
</dd>
</dl>

<dl>
<dd>

**include_timerange:** `typing.Optional[bool]` — Third-party compatibility extension. Include each listed Flow's computed content timerange in the response.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[ContentFormat]` — Filter on Flow format.
    
</dd>
</dl>

<dl>
<dd>

**codec:** `typing.Optional[MimeType]` — Filter on Flow codec.
    
</dd>
</dl>

<dl>
<dd>

**label:** `typing.Optional[str]` — Filter on Flows that have the given label.
    
</dd>
</dl>

<dl>
<dd>

**tag_name:** `typing.Optional[UrlTagList]` 

Filter on flows that have a tag named {name} with a value in the given comma-separated list of values.
The {name} and the value MUST be URL encoded where special characters are present.
Where the tag's value is a string, at least one of the given values will match.
Where the tag's value is an array, at least one value in the array will match at least one of the given values.
Partial string matches of the values are not valid.
    
</dd>
</dl>

<dl>
<dd>

**tag_exists_name:** `typing.Optional[bool]` 

Filter on Flows that have a tag named {name} regardless of value.
{name} MUST be URL encoded where special characters are present.
If set to true then the presence of the tag is filtered for.
If set to false then its absence is.
If left out then no filtering on tag presence is performed.
    
</dd>
</dl>

<dl>
<dd>

**frame_width:** `typing.Optional[int]` — Filter on video Flows that have the given frame width.
    
</dd>
</dl>

<dl>
<dd>

**frame_height:** `typing.Optional[int]` — Filter on video Flows that have the given frame height.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[str]` — Opaque string used by backend to access a specific page of results. Clients should read the next URL from the `Link` header returned with responses, or use value of the returned X-Paging-NextKey header. If not supplied, the first page is accessed. Service implementations should ensure a consistent sort order is applied to pages of results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Restrict the response to the specified number of results. Service implementations may specify their own default and maximum for the limit
    
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

<details><summary><code>client.flows.<a href="src/fern/flows/client.py">get_flows_flow_id</a>(...) -> Flow</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns Flow metadata.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flows.get_flows_flow_id(
    flow_id="flowId",
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

**flow_id:** `Uuid` — The Flow identifier.
    
</dd>
</dl>

<dl>
<dd>

**include_timerange:** `typing.Optional[bool]` — Include `timerange` in the response.
    
</dd>
</dl>

<dl>
<dd>

**timerange:** `typing.Optional[Timerange]` — Limit `timerange` of the response to the time range over which Segments partially or wholly overlap with the provided timerange.
    
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

<details><summary><code>client.flows.<a href="src/fern/flows/client.py">put_flows_flow_id</a>(...) -> typing.Optional[Flow]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or replace the Flow metadata.

Clients should aim to populate as many of the Flow metadata fields as possible and practical. The fewer parameters that are set, the higher the likelihood that reading clients will have to retrieve the media to determine technical metadata to e.g. configure decoders.

Some parameters may be ignored/overridden by service implementations. This is to enable the Flow json-blob to be re-used with no/minimal editing in various use cases. Such parameters are called out in their description.

Service implementations SHOULD verify that Flow metadata is compatible with the associated Source.
Service implementations MAY accept modification/addition of parameters, and reflect such changes in the Source, where it will not bring any Flows of the Source into conflict.
Where metadata would result in any Flow of the Source coming into conflict, the request SHOULD be rejected with a 400 response.
Examples of conflicting metadata include `format` not matching, or the `role` in `source_collection` and `flow_collection` not matching.
It may also be possible for service implementations to detect some instances where multiple Flows should not be considered of the same Source, such as audio Flows with different numbers of tracks.
Further guidance on when Flows/Sources may be considered the same/different may be found in the [Practical Guidance for Media](https://specs.amwa.tv/ms-04/releases/v1.0.0/docs/3.0._Practical_Guidance_for_Media.html) section of AMWA MS-04.
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
from fern import FernApi, FlowVideo, FlowVideoFormat, FlowVideoEssenceParameters
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flows.put_flows_flow_id(
    flow_id="flowId",
    request=FlowVideo(
        id="id",
        source_id="source_id",
        format=FlowVideoFormat.URN_X_NMOS_FORMAT_VIDEO,
        essence_parameters=FlowVideoEssenceParameters(
            frame_width=1,
            frame_height=1,
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

**flow_id:** `Uuid` — The Flow identifier.
    
</dd>
</dl>

<dl>
<dd>

**request:** `Flow` 
    
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

<details><summary><code>client.flows.<a href="src/fern/flows/client.py">delete_flows_flow_id</a>(...) -> typing.Optional[DeletionRequest]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the Flow and associated Segments.
If Flow Segment deletion takes too long then this request will return 202 Accepted and the `Location` header will point to a Flow Delete Request to monitor deletion progress
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flows.delete_flows_flow_id(
    flow_id="flowId",
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

**flow_id:** `Uuid` — The Flow identifier.
    
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

<details><summary><code>client.flows.<a href="src/fern/flows/client.py">head_flows_flow_id</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return Flow path headers
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flows.head_flows_flow_id(
    flow_id="flowId",
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

**flow_id:** `Uuid` — The Flow identifier.
    
</dd>
</dl>

<dl>
<dd>

**include_timerange:** `typing.Optional[bool]` — Include `timerange` in the response.
    
</dd>
</dl>

<dl>
<dd>

**timerange:** `typing.Optional[Timerange]` — Limit `timerange` of the response to the time range over which Segments partially or wholly overlap with the provided timerange.
    
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

<details><summary><code>client.flows.<a href="src/fern/flows/client.py">get_flows_flow_id_tags</a>(...) -> Tags</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the Flow tags.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flows.get_flows_flow_id_tags(
    flow_id="flowId",
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

**flow_id:** `Uuid` — The Flow identifier.
    
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

<details><summary><code>client.flows.<a href="src/fern/flows/client.py">head_flows_flow_id_tags</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return Flow tags path headers
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flows.head_flows_flow_id_tags(
    flow_id="flowId",
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

**flow_id:** `Uuid` — The Flow identifier.
    
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

<details><summary><code>client.flows.<a href="src/fern/flows/client.py">get_flows_flow_id_tags_name</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return the tag value associated with the tag name.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flows.get_flows_flow_id_tags_name(
    flow_id="flowId",
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

**flow_id:** `Uuid` — The Flow identifier.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The tag name. {name} MUST be URL encoded where special characters are present.
    
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

<details><summary><code>client.flows.<a href="src/fern/flows/client.py">put_flows_flow_id_tags_name</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or update the tag.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flows.put_flows_flow_id_tags_name(
    flow_id="flowId",
    name="name",
    request="\"proxy\"\n",
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

**flow_id:** `Uuid` — The Flow identifier.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The tag name. {name} MUST be URL encoded where special characters are present.
    
</dd>
</dl>

<dl>
<dd>

**request:** `str` 
    
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

<details><summary><code>client.flows.<a href="src/fern/flows/client.py">delete_flows_flow_id_tags_name</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the tag.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flows.delete_flows_flow_id_tags_name(
    flow_id="flowId",
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

**flow_id:** `Uuid` — The Flow identifier.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The tag name. {name} MUST be URL encoded where special characters are present.
    
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

<details><summary><code>client.flows.<a href="src/fern/flows/client.py">head_flows_flow_id_tags_name</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return Flow tag path headers
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flows.head_flows_flow_id_tags_name(
    flow_id="flowId",
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

**flow_id:** `Uuid` — The Flow identifier.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The tag name. {name} MUST be URL encoded where special characters are present.
    
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

<details><summary><code>client.flows.<a href="src/fern/flows/client.py">get_flows_flow_id_description</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the Flow description property. This should be a human-readable description that may be showed in detailed views of Flows. The description should be longer and more detailed than `label`.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flows.get_flows_flow_id_description(
    flow_id="flowId",
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

**flow_id:** `Uuid` — The Flow identifier.
    
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

<details><summary><code>client.flows.<a href="src/fern/flows/client.py">put_flows_flow_id_description</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or update the description property. This should be a human-readable description that may be showed in detailed views of Flows. The description should be longer and more detailed than `label`.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flows.put_flows_flow_id_description(
    flow_id="flowId",
    request="\"Big Buck Bunny video-only capture\"\n",
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

**flow_id:** `Uuid` — The Flow identifier.
    
</dd>
</dl>

<dl>
<dd>

**request:** `str` 
    
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

<details><summary><code>client.flows.<a href="src/fern/flows/client.py">delete_flows_flow_id_description</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the description property.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flows.delete_flows_flow_id_description(
    flow_id="flowId",
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

**flow_id:** `Uuid` — The Flow identifier.
    
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

<details><summary><code>client.flows.<a href="src/fern/flows/client.py">head_flows_flow_id_description</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return Flow description path headers
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flows.head_flows_flow_id_description(
    flow_id="flowId",
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

**flow_id:** `Uuid` — The Flow identifier.
    
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

<details><summary><code>client.flows.<a href="src/fern/flows/client.py">get_flows_flow_id_label</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the Flow label property. This should be a very short, human-readable label that may be displayed in listings of Flows.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flows.get_flows_flow_id_label(
    flow_id="flowId",
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

**flow_id:** `Uuid` — The Flow identifier.
    
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

<details><summary><code>client.flows.<a href="src/fern/flows/client.py">put_flows_flow_id_label</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or update the label property. This should be a very short, human-readable label that may be displayed in listings of Flows.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flows.put_flows_flow_id_label(
    flow_id="flowId",
    request="\"Big Buck Bunny Movie\"\n",
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

**flow_id:** `Uuid` — The Flow identifier.
    
</dd>
</dl>

<dl>
<dd>

**request:** `str` 
    
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

<details><summary><code>client.flows.<a href="src/fern/flows/client.py">delete_flows_flow_id_label</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the label property.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flows.delete_flows_flow_id_label(
    flow_id="flowId",
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

**flow_id:** `Uuid` — The Flow identifier.
    
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

<details><summary><code>client.flows.<a href="src/fern/flows/client.py">head_flows_flow_id_label</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return Flow label path headers
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flows.head_flows_flow_id_label(
    flow_id="flowId",
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

**flow_id:** `Uuid` — The Flow identifier.
    
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

<details><summary><code>client.flows.<a href="src/fern/flows/client.py">get_flows_flow_id_read_only</a>(...) -> bool</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the Flow read_only property. If set to 'true', service implementations SHOULD reject client requests to update Flow metadata (other than the read_only property), and Flow Segments. Service implementations should also reject requests to the [`/flows/{flowId}/storage`](#/operations/POST_flows-flowId-storage) endpoint for the Flow, and requests to delete the Flow.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flows.get_flows_flow_id_read_only(
    flow_id="flowId",
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

**flow_id:** `Uuid` — The Flow identifier.
    
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

<details><summary><code>client.flows.<a href="src/fern/flows/client.py">put_flows_flow_id_read_only</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set the read-only property. If set to 'true', service implementations SHOULD reject client requests to update Flow metadata (other than the read_only property), and Flow Segments. Service implementations should also reject requests to the [`/flows/{flowId}/storage`](#/operations/POST_flows-flowId-storage) endpoint for the Flow, and requests to delete the Flow.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flows.put_flows_flow_id_read_only(
    flow_id="flowId",
    request=True,
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

**flow_id:** `Uuid` — The Flow identifier.
    
</dd>
</dl>

<dl>
<dd>

**request:** `bool` 
    
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

<details><summary><code>client.flows.<a href="src/fern/flows/client.py">head_flows_flow_id_read_only</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return Flow read_only path headers
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flows.head_flows_flow_id_read_only(
    flow_id="flowId",
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

**flow_id:** `Uuid` — The Flow identifier.
    
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

<details><summary><code>client.flows.<a href="src/fern/flows/client.py">get_flows_flow_id_flow_collection</a>(...) -> FlowCollection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the Flow collection property. A list of Flows that are collected together by this Flow.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flows.get_flows_flow_id_flow_collection(
    flow_id="flowId",
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

**flow_id:** `Uuid` — The Flow identifier.
    
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

<details><summary><code>client.flows.<a href="src/fern/flows/client.py">put_flows_flow_id_flow_collection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or update the Flow collection property. A list of Flows that are collected together by this Flow.

Service implementations SHOULD verify that Flow metadata is compatible with the associated Source.
Service implementations MAY accept modification/addition of parameters, and reflect such changes in the Source, where it will not bring any Flows of the Source into conflict.
Where metadata would result in any Flow of the Source coming into conflict, the request SHOULD be rejected with a 400 response.
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
from fern import FernApi, FlowCollectionItem
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flows.put_flows_flow_id_flow_collection(
    flow_id="flowId",
    request=[
        FlowCollectionItem(
            id="id",
            role="role",
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

**flow_id:** `Uuid` — The Flow identifier.
    
</dd>
</dl>

<dl>
<dd>

**request:** `FlowCollection` 
    
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

<details><summary><code>client.flows.<a href="src/fern/flows/client.py">delete_flows_flow_id_flow_collection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the Flow collection property.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flows.delete_flows_flow_id_flow_collection(
    flow_id="flowId",
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

**flow_id:** `Uuid` — The Flow identifier.
    
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

<details><summary><code>client.flows.<a href="src/fern/flows/client.py">head_flows_flow_id_flow_collection</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the Flow collection path headers
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flows.head_flows_flow_id_flow_collection(
    flow_id="flowId",
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

**flow_id:** `Uuid` — The Flow identifier.
    
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

<details><summary><code>client.flows.<a href="src/fern/flows/client.py">get_flows_flow_id_max_bit_rate</a>(...) -> int</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the Flow max bit rate property.

The maximum bit rate of the Flow Segments in 1000 bits/second.
A precise definition can be found in the [Setting Flow Bit Rate Properties](https://github.com/bbc/tams/blob/main/docs/appnotes/0013-setting-flow-bit-rate-properties.md) AppNote.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flows.get_flows_flow_id_max_bit_rate(
    flow_id="flowId",
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

**flow_id:** `Uuid` — The Flow identifier.
    
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

<details><summary><code>client.flows.<a href="src/fern/flows/client.py">put_flows_flow_id_max_bit_rate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or update the max bit rate property.

The maximum bit rate of the Flow Segments in 1000 bits/second.
A precise definition can be found in the [Setting Flow Bit Rate Properties](https://github.com/bbc/tams/blob/main/docs/appnotes/0013-setting-flow-bit-rate-properties.md) AppNote.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flows.put_flows_flow_id_max_bit_rate(
    flow_id="flowId",
    request=5000,
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

**flow_id:** `Uuid` — The Flow identifier.
    
</dd>
</dl>

<dl>
<dd>

**request:** `int` 
    
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

<details><summary><code>client.flows.<a href="src/fern/flows/client.py">delete_flows_flow_id_max_bit_rate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the Flow max bit rate property.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flows.delete_flows_flow_id_max_bit_rate(
    flow_id="flowId",
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

**flow_id:** `Uuid` — The Flow identifier.
    
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

<details><summary><code>client.flows.<a href="src/fern/flows/client.py">head_flows_flow_id_max_bit_rate</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the Flow max bit rate path headers
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flows.head_flows_flow_id_max_bit_rate(
    flow_id="flowId",
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

**flow_id:** `Uuid` — The Flow identifier.
    
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

<details><summary><code>client.flows.<a href="src/fern/flows/client.py">get_flows_flow_id_avg_bit_rate</a>(...) -> int</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the Flow average bit rate property.

The average bit rate of the Flow Segments in 1000 bits/second.
A precise definition can be found in the [Setting Flow Bit Rate Properties](https://github.com/bbc/tams/blob/main/docs/appnotes/0013-setting-flow-bit-rate-properties.md) AppNote.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flows.get_flows_flow_id_avg_bit_rate(
    flow_id="flowId",
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

**flow_id:** `Uuid` — The Flow identifier.
    
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

<details><summary><code>client.flows.<a href="src/fern/flows/client.py">put_flows_flow_id_avg_bit_rate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or update the average bit rate property.

The average bit rate of the Flow Segments in 1000 bits/second.
A precise definition can be found in the [Setting Flow Bit Rate Properties](https://github.com/bbc/tams/blob/main/docs/appnotes/0013-setting-flow-bit-rate-properties.md) AppNote.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flows.put_flows_flow_id_avg_bit_rate(
    flow_id="flowId",
    request=3246,
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

**flow_id:** `Uuid` — The Flow identifier.
    
</dd>
</dl>

<dl>
<dd>

**request:** `int` 
    
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

<details><summary><code>client.flows.<a href="src/fern/flows/client.py">delete_flows_flow_id_avg_bit_rate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the Flow average bit rate property.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flows.delete_flows_flow_id_avg_bit_rate(
    flow_id="flowId",
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

**flow_id:** `Uuid` — The Flow identifier.
    
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

<details><summary><code>client.flows.<a href="src/fern/flows/client.py">head_flows_flow_id_avg_bit_rate</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the Flow average bit rate path headers
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flows.head_flows_flow_id_avg_bit_rate(
    flow_id="flowId",
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

**flow_id:** `Uuid` — The Flow identifier.
    
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

## FlowSegments
<details><summary><code>client.flow_segments.<a href="src/fern/flow_segments/client.py">get_flows_flow_id_segments</a>(...) -> typing.List[FlowSegment]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the Flow Segments.

The Flow Segment provides information about the Media Object.
The Storage Backend type, which is indicated in the [/service/storage-backends](#/operations/GET_storage-backends) resource, determines the information that is included in the response to allow the Flow Segment's Media Object to be downloaded by the client.
The examples provided here are for the "http_object_store" Storage Backend type which MUST include a `get_urls` property that contains the HTTP URLs for downloading the Media Object - service implementations should generate this internally.

The Flow Segment may include timing adjustment information that the client needs to apply when extracting the samples from the Media Object.
The timestamp of a sample on the Flow Segment's timeline (`segment_ts`) is the timestamp of that sample embedded in or derived from the internal timing of the Media Object (`media_object_ts`) adjusted by `ts_offset`: `segment_ts = media_object_ts + ts_offset`.

It may also use a subset of the samples in the Media Object, and if the `include_object_timerange=true` parameter is set, the object's timerange will also be returned to aid identifying which samples to skip.

Clients should use the pagination options to limit the results to a timerange and/or count.
Service implementations may also limit the results returned.
This will be signalled via the paging headers in the response.
The list of Flow Segments can be empty.
A request for Segments from a non-existent Flow will return an empty list, not a 404.

Note that for codecs with temporal re-ordering, the timerange represents the _presentation_ timeline, and clients may need to check the `key_frame_count` property and/or read backwards from the start of the requested timerange to retrieve enough reference material to start decoding.

When making requests to the provided `get_urls`, clients should include credentials if the provided URL is on the same origin as the API itself, akin to the `same-origin` mode in the [WhatWG Fetch Standard](https://fetch.spec.whatwg.org/#concept-request-credentials-mode).
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flow_segments.get_flows_flow_id_segments(
    flow_id="flowId",
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

**flow_id:** `Uuid` — The Flow identifier.
    
</dd>
</dl>

<dl>
<dd>

**object_id:** `typing.Optional[str]` — Filter on Object identifier.
    
</dd>
</dl>

<dl>
<dd>

**timerange:** `typing.Optional[Timerange]` — Return only the results that partially or wholly overlap the timerange specified.
    
</dd>
</dl>

<dl>
<dd>

**reverse_order:** `typing.Optional[bool]` — Return Segments in reverse time order.
    
</dd>
</dl>

<dl>
<dd>

**verbose_storage:** `typing.Optional[bool]` 

Include storage metadata in `get_urls` in the response.
When `verbose_storage` is `false` only `url`, `presigned`, and `label` will be included in `get_urls`.
    
</dd>
</dl>

<dl>
<dd>

**accept_get_urls:** `typing.Optional[UrlLabelList]` 

A comma separated list of labels of Flow Segment `get_urls` to include in the response.
Omitting `accept_get_urls` will result in no filtering of `get_urls`.
An empty `accept_get_urls` results in an empty or no `get_urls` in the response.
Flow Segment `get_urls` with no label will only be returned if `accept_get_urls` is omitted.
Without `get_urls`, the response from the service could be substantially faster if it is not required to generate a large number of pre-signed URLs for example.
Where multiple filter query parameters are provided, the returned `get_urls` will match all filters.
    
</dd>
</dl>

<dl>
<dd>

**accept_storage_ids:** `typing.Optional[UuidList]` 

A comma separated list of `storage_id`s of Flow Segment `get_urls` to include in the response.
Omitting `accept_storage_ids`, or providing an empty `accept_storage_ids` will result in no filtering of `get_urls`.
Flow Segment `get_urls` with no storage ID will only be returned if `accept_storage_ids` is omitted or empty.
A full list of available `storage_id`s may be found at the [/service/storage-backends](#/operations/GET_storage-backends) endpoint.
Where multiple filter query parameters are provided, the returned `get_urls` will match all filters.
    
</dd>
</dl>

<dl>
<dd>

**presigned:** `typing.Optional[bool]` 

If set to `true`, only presigned URLs (i.e. those whos `presigned` property is `true`) will be returned in `get_urls`.
If set to `false`, only non-presigned URLs (i.e. those whos `presigned` property is `false`) will be returned in `get_urls`.
If omitted, both presigned and non-presigned URLs will be returned.
If `presigned` is set to `false`, the response from the service could be substantially faster if it is not required to generate a large number of pre-signed URLs.
Where multiple filter query parameters are provided, the returned `get_urls` will match all filters.
    
</dd>
</dl>

<dl>
<dd>

**include_object_timerange:** `typing.Optional[bool]` 

If set to `true`, the underlying object's timerange should appear in the response (if it differs from the Flow Segment's `timerange`).
Assume `false` if omitted.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[str]` — Opaque string used by backend to access a specific page of results. Clients should read the next URL from the `Link` header returned with responses, or use value of the returned X-Paging-NextKey header. If not supplied, the first page is accessed. Service implementations should ensure a consistent sort order is applied to pages of results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Restrict the response to the specified number of results. Service implementations may specify their own default and maximum for the limit
    
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

<details><summary><code>client.flow_segments.<a href="src/fern/flow_segments/client.py">post_flows_flow_id_segments</a>(...) -> FlowSegmentBulkFailure</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Register either a single new Flow Segment or an array of Segments, attaching the Object id given to a point in the Flow timeline.

The Segment may use a newly-written Media Object, or re-use an existing Media Object from another Flow.

For newly-written Media Objects, the client is responsible for ensuring that the Segment written to the TAMS service instance obeys the following restrictions:
  - All samples in the Object SHOULD be used by the Segment.
  - If the Segment does not use all samples in the Object, `object_timerange` MUST be set to the timerange of media in the object, on the Media Object's timeline
  - The timestamps of each sample in the Media Object MUST equal its position on the Flow timeline, OR `ts_offset` MUST be set such that `media_object_ts + ts_offset = segment_ts`
  - The timerange of the Segment MUST NOT overlap any other Segment in the same Flow. The behaviour is undefined if there is an overlap with existing Segments and a service may return a 400 error response.

A service instance SHOULD reject registrations of Flow Segments with a 400 error response if it references a newly created Media Object in the local TAMS storage that was not intended to be used for the Flow.
A service instance SHOULD accept Flow Segments that reference an existing Media Object in the local TAMS storage that was originally created for another Flow.

A service instance MAY support Media Objects that are held in external storage in another TAMS or other media storage system.
The Flow Segment may in that case require the `get_urls` property to provide the information needed by clients to access the Media Object.

The list of instances of an object (and associated `get_urls` entries) can be modified via the [`/objects`](#/operations/GET_objects) endpoints, which provides a mechanism to register new instances of an object.

Clients MAY modify Flow Segments, but this should only be done in exceptional circumstances to correct metadata such as `key_frame_count`, as such operations will likely break the idempotency of Segments.
If a client needs to modify a Flow Segment, then the client SHOULD first delete the existing Segment and then write a new one.
The behaviour is undefined if the Segment exists and the service may return a 400 error response.

For successful creation of all Segments in the request a 201 response should be provided.
If an error is detected when processing a list of Segments then processing should continue to try and process the remaining Segments.
A 200 response should be returned listing the failed Segments.

Clients are expected to decide how to break content into Media Objects, however those Objects SHOULD be large enough to avoid excessive round trip overheads in the underlying store (_e.g._ of the order of several megabytes) and where codecs with temporal re-ordering are used, Object SHOULD contain complete GOPs or decodable units.

For Media Objects that have been re-used from other Flows, the `timerange` MAY specify only part of the duration of the object:
  - The `timerange` field indicates the new Segment's position in the Flow
  - The timerange of the Segment MUST NOT overlap any other Segment in the same Flow.
  - The Flow Segment's `timerange` start and end, once offset by `ts_offset`, MUST be contained entirely within the Media Object's `timerange`

When re-using Media Objects, requests which change object properties (e.g. `key_frame_count` or `object_timerange`) SHOULD be rejected.
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
from fern import FernApi, FlowSegmentPost
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flow_segments.post_flows_flow_id_segments(
    flow_id="flowId",
    request=[
        FlowSegmentPost(
            object_id="object_id",
            timerange="timerange",
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

**flow_id:** `Uuid` — The Flow identifier.
    
</dd>
</dl>

<dl>
<dd>

**request:** `PostFlowsFlowIdSegmentsRequestBody` 
    
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

<details><summary><code>client.flow_segments.<a href="src/fern/flow_segments/client.py">delete_flows_flow_id_segments</a>(...) -> typing.Optional[DeletionRequest]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the Flow Segments. If the deletion takes too long then this request will return 202 Accepted and the `Location` header will point to a Flow Delete Request to monitor deletion progress
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flow_segments.delete_flows_flow_id_segments(
    flow_id="flowId",
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

**flow_id:** `Uuid` — The Flow identifier.
    
</dd>
</dl>

<dl>
<dd>

**timerange:** `typing.Optional[Timerange]` — Only delete Flow Segments that are completely covered by the given timerange.
    
</dd>
</dl>

<dl>
<dd>

**object_id:** `typing.Optional[str]` — Filter on Object identifier.
    
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

<details><summary><code>client.flow_segments.<a href="src/fern/flow_segments/client.py">head_flows_flow_id_segments</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return Flow Segments path headers
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flow_segments.head_flows_flow_id_segments(
    flow_id="flowId",
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

**flow_id:** `Uuid` — The Flow identifier.
    
</dd>
</dl>

<dl>
<dd>

**object_id:** `typing.Optional[str]` — Filter on Object identifier.
    
</dd>
</dl>

<dl>
<dd>

**timerange:** `typing.Optional[Timerange]` — Return only the results that partially or wholly overlap the timerange specified.
    
</dd>
</dl>

<dl>
<dd>

**reverse_order:** `typing.Optional[bool]` — Return Segments in reverse time order.
    
</dd>
</dl>

<dl>
<dd>

**verbose_storage:** `typing.Optional[bool]` 

Include storage metadata in `get_urls` in the response.
When `verbose_storage` is `false` only `url`, `presigned`, and `label` will be included in `get_urls`.
    
</dd>
</dl>

<dl>
<dd>

**accept_get_urls:** `typing.Optional[UrlLabelList]` 

A comma separated list of labels of Flow Segment `get_urls` to include in the response.
Omitting `accept_get_urls` will result in no filtering of `get_urls`.
An empty `accept_get_urls` results in an empty or no `get_urls` in the response.
Flow Segment `get_urls` with no label will only be returned if `accept_get_urls` is omitted.
Without `get_urls`, the response from the service could be substantially faster if it is not required to generate a large number of pre-signed URLs for example.
Where multiple filter query parameters are provided, the returned `get_urls` will match all filters.
    
</dd>
</dl>

<dl>
<dd>

**accept_storage_ids:** `typing.Optional[UuidList]` 

A comma separated list of `storage_id`s of Flow Segment `get_urls` to include in the response.
Omitting `accept_storage_ids`, or providing an empty `accept_storage_ids` will result in no filtering of `get_urls`.
Flow Segment `get_urls` with no storage ID will only be returned if `accept_storage_ids` is omitted or empty.
A full list of available `storage_id`s may be found at the [/service/storage-backends](#/operations/GET_storage-backends) endpoint.
Where multiple filter query parameters are provided, the returned `get_urls` will match all filters.
    
</dd>
</dl>

<dl>
<dd>

**presigned:** `typing.Optional[bool]` 

If set to `true`, only presigned URLs (i.e. those whos `presigned` property is `true`) will be returned in `get_urls` in the response.
If set to `false`, only non-presigned URLs (i.e. those whos `presigned` property is `false`) will be returned in `get_urls`.
If omitted, both presigned and non-presigned URLs will be returned.
If `presigned` is set to `false`, the response from the service could be substantially faster if it is not required to generate a large number of pre-signed URLs.
Where multiple filter query parameters are provided, the returned `get_urls` will match all filters.
    
</dd>
</dl>

<dl>
<dd>

**include_object_timerange:** `typing.Optional[bool]` 

If set to `true`, the underlying object's timerange should appear in the response (if it differs from the segment timerange).
Assume `false` if omitted.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[str]` — Opaque string used by backend to access a specific page of results. Clients should read the next URL from the `Link` header returned with responses, or use value of the returned X-Paging-NextKey header. If not supplied, the first page is accessed. Service implementations should ensure a consistent sort order is applied to pages of results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Restrict the response to the specified number of results. Service implementations may specify their own default and maximum for the limit
    
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

## MediaStorage
<details><summary><code>client.media_storage.<a href="src/fern/media_storage/client.py">post_flows_flow_id_storage</a>(...) -> FlowStorage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Allocate initial storage locations for writing Media Objects.

The Storage Backend type, which is indicated in the [/service](#/operations/GET_service) resource, determines the information provided in the response.
The examples and description below are for the "http_object_store" Storage Backend type.
This Storage Backend type provides HTTP URLs for uploading and downloading Media Objects in buckets.

The response will include a PUT URL that a client uses to upload the Media Object.
The client is expected to register the Flow Segment using the [/flows/{flowId}/segments](#/operations/POST_flows-flowId-segments) endpoint once the upload is complete.

Clients MAY request Objects in batches to reduce the number of HTTP requests made to the Service.
Clients are not expected to use all of the Objects they requested.
Objects will likely go unused in cases such as shutdown of ingesting clients, the end of ingested live streams, and unexpected network congestion.
Clients SHOULD, however, adapt the number of Objects they request such that they may reasonably expect to use them before the timeout advertised in [`min_object_timeout` at the `/service`](#/operations/GET_service) endpoint, which is subject to a specified minimum (see service endpoint schema).

Service implementations need to handle situations where Objects are not used, and where content was uploaded but no Flow Segment was registered successfully.
In these circumstances, Services should garbage collect Objects after the timeout advertised in [`min_object_timeout` at the `/service`](#/operations/GET_service) endpoint.

When making requests to the provided `put_url`, clients should include credentials if the provided URL is on the same origin as the API itself, akin to the `same-origin` mode in the [WhatWG Fetch Standard](https://fetch.spec.whatwg.org/#concept-request-credentials-mode).
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.media_storage.post_flows_flow_id_storage(
    flow_id="flowId",
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

**flow_id:** `Uuid` — The Flow identifier.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit the number of Media Objects in each response page. Service implementations may specify their own default and maximum for the limit
    
</dd>
</dl>

<dl>
<dd>

**object_ids:** `typing.Optional[typing.List[str]]` — Array of object_ids to use. The supplied object_ids must be new and not already in use in this TAMS service instance. A 400 response will be returned if any supplied object_id already exists.
    
</dd>
</dl>

<dl>
<dd>

**storage_id:** `typing.Optional[Uuid]` — The Storage Backend to allocate storage in. A Storage Backend identifier as advertised at the [/service/storage-backends](#/operations/GET_storage-backends) endpoint. If not set the default, as advertised at the [/service/storage-backends](#/operations/GET_storage-backends) endpoint, will be used if available. An invalid Storage Backend identifier will result in a 400 error.
    
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

## Objects
<details><summary><code>client.objects.<a href="src/fern/objects/client.py">get_objects</a>(...) -> Object</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Contains Flows that references the Media Object and other information.

The paging query parameters and headers are required for the list of Flow references in the Media Object.
Service implementations should return a complete list of Flow references within reason and API clients should expect paging to happen in some rare cases where a Media Object is used in many Flows.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.objects.get_objects(
    object_id="objectId",
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

**object_id:** `str` — The Media Object identifier. The Object ID may include special characters such as `/` which should be URL encoded.
    
</dd>
</dl>

<dl>
<dd>

**verbose_storage:** `typing.Optional[bool]` 

Include storage metadata in `get_urls`.
When `verbose_storage` is `false` only `url`, `presigned`, and `label` will be included in `get_urls`.
    
</dd>
</dl>

<dl>
<dd>

**accept_get_urls:** `typing.Optional[UrlLabelList]` 

A comma separated list of labels of Media Object `get_urls` to include in the response.
Omitting `accept_get_urls` will result in no filtering of `get_urls`.
An empty `accept_get_urls` results in an empty or no `get_urls` in the response.
Media Object `get_urls` with no label will only be returned if `accept_get_urls` is omitted.
Without `get_urls`, the response from the service could be substantially faster if it is not required to
generate a large number of pre-signed URLs for example.
Where multiple filter query parameters are provided, the returned `get_urls` will match all filters.
    
</dd>
</dl>

<dl>
<dd>

**accept_storage_ids:** `typing.Optional[str]` 

A comma separated list of `storage_id`s of Media Object `get_urls` to include in the response.
Omitting `accept_storage_ids`, or providing an empty `accept_storage_ids` will result in no filtering of `get_urls`.
Media Object `get_urls` with no storage ID will only be returned if `accept_storage_ids` is omitted or empty.
A full list of available `storage_id`s may be found at the `service/storage-backends` endpoint.
Where multiple filter query parameters are provided, the returned `get_urls` will match all filters.
    
</dd>
</dl>

<dl>
<dd>

**presigned:** `typing.Optional[bool]` 

If set to `true`, only presigned URLs (i.e. those whos `presigned` property is `true`) will be returned in `get_urls`.
If set to `false`, only non-presigned URLs (i.e. those whos `presigned` property is `false`) will be returned in `get_urls`.
If omitted, both presigned and non-presigned URLs will be returned.
If `presigned` is set to `false`, the response from the service could be substantially faster if it is not required to
generate a large number of pre-signed URLs.
Where multiple filter query parameters are provided, the returned `get_urls` will match all filters.
    
</dd>
</dl>

<dl>
<dd>

**flow_tag_name:** `typing.Optional[str]` — Filter `referenced_by_flows` on tag values. This option is the same as the `tag.{name}` query parameter on the `/flows/` API endpoint.
    
</dd>
</dl>

<dl>
<dd>

**flow_tag_exists_name:** `typing.Optional[bool]` — Filter `referenced_by_flows` on tag names. This option is the same as the `tag_exists.{name}` query parameter on the `/flows/` API endpoint.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[str]` — Opaque string used by backend to access a specific page of results. Clients should read the next URL from the `Link` header returned with responses, or use value of the returned X-Paging-NextKey header. If not supplied, the first page is accessed. Service implementations should ensure a consistent sort order is applied to pages of results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Restrict the response to the specified number of results. Service implementations may specify their own default and maximum for the limit
    
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

<details><summary><code>client.objects.<a href="src/fern/objects/client.py">head_objects</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return Flow references and other information about Media Objects.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.objects.head_objects(
    object_id="objectId",
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

**object_id:** `str` — The Media Object identifier. The Object ID may include special characters such as `/` which should be URL encoded.
    
</dd>
</dl>

<dl>
<dd>

**verbose_storage:** `typing.Optional[bool]` 

Include storage metadata in `get_urls`.
When `verbose_storage` is `false` only `url`, `presigned`, and `label` will be included in `get_urls`.
    
</dd>
</dl>

<dl>
<dd>

**accept_get_urls:** `typing.Optional[UrlLabelList]` 

A comma separated list of labels of Media Object `get_urls` to include in the response.
Omitting `accept_get_urls` will result in no filtering of `get_urls`.
An empty `accept_get_urls` results in an empty or no `get_urls` in the response.
Media Object `get_urls` with no label will only be returned if `accept_get_urls` is omitted.
Without `get_urls`, the response from the service could be substantially faster if it is not required to
generate a large number of pre-signed URLs for example.
Where multiple filter query parameters are provided, the returned `get_urls` will match all filters.
    
</dd>
</dl>

<dl>
<dd>

**accept_storage_ids:** `typing.Optional[str]` 

A comma separated list of `storage_id`s of Media Object `get_urls` to include in the response.
Omitting `accept_storage_ids`, or providing an empty `accept_storage_ids` will result in no filtering of `get_urls`.
Media Object `get_urls` with no storage ID will only be returned if `accept_storage_ids` is omitted or empty.
A full list of available `storage_id`s may be found at the `service/storage-backends` endpoint.
Where multiple filter query parameters are provided, the returned `get_urls` will match all filters.
    
</dd>
</dl>

<dl>
<dd>

**presigned:** `typing.Optional[bool]` 

If set to `true`, only presigned URLs (i.e. those whos `presigned` property is `true`) will be returned in `get_urls`.
If set to `false`, only non-presigned URLs (i.e. those whos `presigned` property is `false`) will be returned in `get_urls`.
If omitted, both presigned and non-presigned URLs will be returned.
If `presigned` is set to `false`, the response from the service could be substantially faster if it is not required to
generate a large number of pre-signed URLs.
Where multiple filter query parameters are provided, the returned `get_urls` will match all filters.
    
</dd>
</dl>

<dl>
<dd>

**flow_tag_name:** `typing.Optional[str]` — Filter `referenced_by_flows` on tag values. This option is the same as the `tag.{name}` query parameter on the `/flows/` API endpoint.
    
</dd>
</dl>

<dl>
<dd>

**flow_tag_exists_name:** `typing.Optional[bool]` — Filter `referenced_by_flows` on tag names. This option is the same as the `tag_exists.{name}` query parameter on the `/flows/` API endpoint.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[str]` — Opaque string used by backend to access a specific page of results. Clients should read the next URL from the `Link` header returned with responses, or use value of the returned X-Paging-NextKey header. If not supplied, the first page is accessed. Service implementations should ensure a consistent sort order is applied to pages of results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Restrict the response to the specified number of results. Service implementations may specify their own default and maximum for the limit
    
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

<details><summary><code>client.objects.<a href="src/fern/objects/client.py">post_objects_instances</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Request the service to create an Object instance on a new Storage Backend. Or add a new uncontrolled URL to `get_urls`.

To request the duplication of the Object to a new Storage Backend, clients POST a `storage_id` to this endpoint that does not currently have an instance of the Object. The API will then:

- Allocate storage for Media Object `objectId` on Storage Backend `storage_id`
- Copy the Media Object from an existing location to the newly allocated storage
- Start advertising the new copy in `get_urls` once ready

The API instances SHOULD be capable of handling the case where the only existant instances are uncontrolled.

Where a client has written a new uncontrolled Object instance, the client is responsible for ensuring that the Object written is complete and correct before registering it with this method.

All instances of an Object MUST be identical.
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
from fern import FernApi, ObjectsInstancesPostStorageId
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.objects.post_objects_instances(
    object_id="objectId",
    request=ObjectsInstancesPostStorageId(
        storage_id="storage_id",
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

**object_id:** `str` — The Media Object identifier. The Object ID may include special characters such as `/` which should be URL encoded.
    
</dd>
</dl>

<dl>
<dd>

**request:** `ObjectsInstancesPost` 
    
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

<details><summary><code>client.objects.<a href="src/fern/objects/client.py">delete_objects_instances</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an instance of a Media Object.

One of `storage_id` or `label` MUST be specified in the query parameters. `storage_id` SHOULD be used where `controlled` is `True` for the instance.

API instances should remove the Media Object instance from the `get_urls` list and then, if the instance is controlled, delete the Object instance from storage.

API instances SHOULD prevent clients from deleting all Object instances. Additionally, API instances MAY prevent clients from deleting all controlled Object instances. Where clients wish to remove all copies of an Object from the store, they should do so by deleting all Flows or Flow Segments which reference the Object.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.objects.delete_objects_instances(
    object_id="objectId",
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

**object_id:** `str` — The Media Object identifier. The Object ID may include special characters such as `/` which should be URL encoded.
    
</dd>
</dl>

<dl>
<dd>

**storage_id:** `typing.Optional[str]` — The storage_id identifying the Media Object instance to be deleted.
    
</dd>
</dl>

<dl>
<dd>

**label:** `typing.Optional[str]` — The label identifying the Media Object instance to be deleted.
    
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

## FlowDeleteRequests
<details><summary><code>client.flow_delete_requests.<a href="src/fern/flow_delete_requests/client.py">get_flow_delete_requests</a>() -> typing.List[DeletionRequest]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List ongoing flow deletion requests.

This will not necessarily list all requests, nor return a consistent set in any particular order, and should not be relied upon by clients. However if there are any requests in the system, it will always return at least one.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flow_delete_requests.get_flow_delete_requests()

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

<details><summary><code>client.flow_delete_requests.<a href="src/fern/flow_delete_requests/client.py">head_flow_delete_requests</a>() -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return flow-delete-requests path headers
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flow_delete_requests.head_flow_delete_requests()

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

<details><summary><code>client.flow_delete_requests.<a href="src/fern/flow_delete_requests/client.py">get_flow_delete_requests_request_id</a>(...) -> DeletionRequest</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a timerange of Flow Segments that are being deleted.

A deletion request is created when a client DELETEs a long timerange of Segments, which takes longer than a single HTTP request.
Clients will be redirected here to monitor the request's progress.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flow_delete_requests.get_flow_delete_requests_request_id(
    request_id="request-id",
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

<details><summary><code>client.flow_delete_requests.<a href="src/fern/flow_delete_requests/client.py">head_flow_delete_requests_request_id</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return Flow delete request path headers
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.flow_delete_requests.head_flow_delete_requests_request_id(
    request_id="request-id",
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

