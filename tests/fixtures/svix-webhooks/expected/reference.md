# Reference
<details><summary><code>client.<a href="src/fern/client.py">get_api_v1health_ping</a>()</code></summary>
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

client.get_api_v1health_ping()

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

<details><summary><code>client.<a href="src/fern/client.py">head_api_v1health_ping</a>()</code></summary>
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

client.head_api_v1health_ping()

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

## Application
<details><summary><code>client.application.<a href="src/fern/application/client.py">v1application_list</a>(...) -> ListResponseApplicationOut</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of all the organization's applications.
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

client.application.v1application_list(
    iterator="app_1srOrx2ZWZBpBUvZwXKQmoEYga2",
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

**limit:** `typing.Optional[int]` — Limit the number of returned items
    
</dd>
</dl>

<dl>
<dd>

**iterator:** `typing.Optional[str]` — The iterator returned from a prior invocation
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[Ordering]` — The sorting order of the returned items
    
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

<details><summary><code>client.application.<a href="src/fern/application/client.py">v1application_create</a>(...) -> ApplicationOut</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new application.
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

client.application.v1application_create(
    name="My first application",
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

**request:** `ApplicationIn` 
    
</dd>
</dl>

<dl>
<dd>

**get_if_exists:** `typing.Optional[bool]` — Get an existing application, or create a new one if doesn't exist. It's two separate functions in the libs.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — The request's idempotency key
    
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

<details><summary><code>client.application.<a href="src/fern/application/client.py">v1application_get</a>(...) -> ApplicationOut</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an application.
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

client.application.v1application_get(
    app_id="app_id",
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

**app_id:** `str` 
    
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

<details><summary><code>client.application.<a href="src/fern/application/client.py">v1application_update</a>(...) -> ApplicationOut</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an application.
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

client.application.v1application_update(
    app_id="unique-app-identifier",
    name="My first application",
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

**app_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `ApplicationIn` 
    
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

<details><summary><code>client.application.<a href="src/fern/application/client.py">v1application_delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an application.
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

client.application.v1application_delete(
    app_id="app_id",
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

**app_id:** `str` 
    
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

<details><summary><code>client.application.<a href="src/fern/application/client.py">patch_application</a>(...) -> ApplicationOut</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Partially update an application.
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

client.application.patch_application(
    app_id="app_id",
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

**app_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, str]]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**throttle_rate:** `typing.Optional[int]` 

Maximum messages per second to send to this application's endpoints.

Outgoing messages will be throttled to this rate.
    
</dd>
</dl>

<dl>
<dd>

**uid:** `typing.Optional[str]` 
    
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

## Message Attempt
<details><summary><code>client.message_attempt.<a href="src/fern/message_attempt/client.py">v1message_attempt_list_by_endpoint</a>(...) -> ListResponseMessageAttemptOut</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List attempts by endpoint id
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

client.message_attempt.v1message_attempt_list_by_endpoint(
    app_id="unique-app-identifier",
    endpoint_id="unique-ep-identifier",
    iterator="atmpt_1srOrx2ZWZBpBUvZwXKQmoEYga2",
    channel="project_1337",
    event_types=[
        "user.signup"
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

**app_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**endpoint_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit the number of returned items
    
</dd>
</dl>

<dl>
<dd>

**iterator:** `typing.Optional[str]` — The iterator returned from a prior invocation
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[MessageStatus]` — Filter response based on the delivery status
    
</dd>
</dl>

<dl>
<dd>

**status_code_class:** `typing.Optional[StatusCodeClass]` — Filter response based on the HTTP status code
    
</dd>
</dl>

<dl>
<dd>

**channel:** `typing.Optional[str]` — Filter response based on the channel
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[datetime.datetime]` — Only include items created before a certain date
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[datetime.datetime]` — Only include items created after a certain date
    
</dd>
</dl>

<dl>
<dd>

**with_content:** `typing.Optional[bool]` — When `true` attempt content is included in the response
    
</dd>
</dl>

<dl>
<dd>

**event_types:** `typing.Optional[typing.List[str]]` — Filter response based on the event type
    
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

<details><summary><code>client.message_attempt.<a href="src/fern/message_attempt/client.py">v1message_attempt_list_by_msg</a>(...) -> ListResponseMessageAttemptOut</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List attempts by message id
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

client.message_attempt.v1message_attempt_list_by_msg(
    app_id="unique-app-identifier",
    msg_id="unique-msg-identifier",
    iterator="atmpt_1srOrx2ZWZBpBUvZwXKQmoEYga2",
    channel="project_1337",
    endpoint_id="unique-ep-identifier",
    event_types=[
        "user.signup"
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

**app_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**msg_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit the number of returned items
    
</dd>
</dl>

<dl>
<dd>

**iterator:** `typing.Optional[str]` — The iterator returned from a prior invocation
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[MessageStatus]` — Filter response based on the delivery status
    
</dd>
</dl>

<dl>
<dd>

**status_code_class:** `typing.Optional[StatusCodeClass]` — Filter response based on the HTTP status code
    
</dd>
</dl>

<dl>
<dd>

**channel:** `typing.Optional[str]` — Filter response based on the channel
    
</dd>
</dl>

<dl>
<dd>

**endpoint_id:** `typing.Optional[str]` — Filter the attempts based on the attempted endpoint
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[datetime.datetime]` — Only include items created before a certain date
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[datetime.datetime]` — Only include items created after a certain date
    
</dd>
</dl>

<dl>
<dd>

**with_content:** `typing.Optional[bool]` — When `true` attempt content is included in the response
    
</dd>
</dl>

<dl>
<dd>

**event_types:** `typing.Optional[typing.List[str]]` — Filter response based on the event type
    
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

<details><summary><code>client.message_attempt.<a href="src/fern/message_attempt/client.py">v1message_attempt_list_attempted_messages</a>(...) -> ListResponseEndpointMessageOut</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List messages for a particular endpoint. Additionally includes metadata about the latest message attempt.

The `before` parameter lets you filter all items created before a certain date and is ignored if an iterator is passed.
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

client.message_attempt.v1message_attempt_list_attempted_messages(
    app_id="unique-app-identifier",
    endpoint_id="unique-ep-identifier",
    iterator="msg_1srOrx2ZWZBpBUvZwXKQmoEYga2",
    channel="project_1337",
    event_types=[
        "user.signup"
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

**app_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**endpoint_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit the number of returned items
    
</dd>
</dl>

<dl>
<dd>

**iterator:** `typing.Optional[str]` — The iterator returned from a prior invocation
    
</dd>
</dl>

<dl>
<dd>

**channel:** `typing.Optional[str]` — Filter response based on the channel
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[MessageStatus]` — Filter response based on the delivery status
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[datetime.datetime]` — Only include items created before a certain date
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[datetime.datetime]` — Only include items created after a certain date
    
</dd>
</dl>

<dl>
<dd>

**with_content:** `typing.Optional[bool]` — When `true` message payloads are included in the response
    
</dd>
</dl>

<dl>
<dd>

**event_types:** `typing.Optional[typing.List[str]]` — Filter response based on the event type
    
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

<details><summary><code>client.message_attempt.<a href="src/fern/message_attempt/client.py">v1message_attempt_get</a>(...) -> MessageAttemptOut</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

`msg_id`: Use a message id or a message `eventId`
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

client.message_attempt.v1message_attempt_get(
    app_id="unique-app-identifier",
    msg_id="unique-msg-identifier",
    attempt_id="atmpt_1srOrx2ZWZBpBUvZwXKQmoEYga2",
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

**app_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**msg_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**attempt_id:** `str` 
    
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

<details><summary><code>client.message_attempt.<a href="src/fern/message_attempt/client.py">v1message_attempt_expunge_content</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the given attempt's response body. Useful when an endpoint accidentally returned sensitive content.
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

client.message_attempt.v1message_attempt_expunge_content(
    app_id="unique-app-identifier",
    msg_id="unique-msg-identifier",
    attempt_id="atmpt_1srOrx2ZWZBpBUvZwXKQmoEYga2",
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

**app_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**msg_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**attempt_id:** `str` 
    
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

<details><summary><code>client.message_attempt.<a href="src/fern/message_attempt/client.py">v1message_attempt_list_attempted_destinations</a>(...) -> ListResponseMessageEndpointOut</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

`msg_id`: Use a message id or a message `eventId`
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

client.message_attempt.v1message_attempt_list_attempted_destinations(
    app_id="unique-app-identifier",
    msg_id="unique-msg-identifier",
    iterator="ep_1srOrx2ZWZBpBUvZwXKQmoEYga2",
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

**app_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**msg_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit the number of returned items
    
</dd>
</dl>

<dl>
<dd>

**iterator:** `typing.Optional[str]` — The iterator returned from a prior invocation
    
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

<details><summary><code>client.message_attempt.<a href="src/fern/message_attempt/client.py">v1message_attempt_resend</a>(...) -> EmptyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Resend a message to the specified endpoint.
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

client.message_attempt.v1message_attempt_resend(
    app_id="unique-app-identifier",
    msg_id="unique-msg-identifier",
    endpoint_id="unique-ep-identifier",
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

**app_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**msg_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**endpoint_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — The request's idempotency key
    
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

## Endpoint
<details><summary><code>client.endpoint.<a href="src/fern/endpoint/client.py">v1endpoint_list</a>(...) -> ListResponseEndpointOut</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the application's endpoints.
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

client.endpoint.v1endpoint_list(
    app_id="unique-app-identifier",
    iterator="ep_1srOrx2ZWZBpBUvZwXKQmoEYga2",
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

**app_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit the number of returned items
    
</dd>
</dl>

<dl>
<dd>

**iterator:** `typing.Optional[str]` — The iterator returned from a prior invocation
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[Ordering]` — The sorting order of the returned items
    
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

<details><summary><code>client.endpoint.<a href="src/fern/endpoint/client.py">v1endpoint_create</a>(...) -> EndpointOut</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new endpoint for the application.

When `secret` is `null` the secret is automatically generated (recommended)
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

client.endpoint.v1endpoint_create(
    app_id="unique-app-identifier",
    url="https://example.com/webhook/",
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

**app_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — The request's idempotency key
    
</dd>
</dl>

<dl>
<dd>

**channels:** `typing.Optional[typing.List[str]]` — List of message channels this endpoint listens to (omit for all)
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**disabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**event_types:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, str]]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[str]` — The endpoint's verification secret. If `null` is passed, a secret is automatically generated. Format: `base64` encoded random bytes optionally prefixed with `whsec_`. Recommended size: 24.
    
</dd>
</dl>

<dl>
<dd>

**throttle_rate:** `typing.Optional[int]` 

Maximum messages per second to send to this endpoint.

Outgoing messages will be throttled to this rate.
    
</dd>
</dl>

<dl>
<dd>

**uid:** `typing.Optional[str]` — Optional unique identifier for the endpoint
    
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

<details><summary><code>client.endpoint.<a href="src/fern/endpoint/client.py">v1endpoint_get</a>(...) -> EndpointOut</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an endpoint.
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

client.endpoint.v1endpoint_get(
    app_id="unique-app-identifier",
    endpoint_id="unique-ep-identifier",
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

**app_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**endpoint_id:** `str` 
    
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

<details><summary><code>client.endpoint.<a href="src/fern/endpoint/client.py">v1endpoint_update</a>(...) -> EndpointOut</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an endpoint.
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

client.endpoint.v1endpoint_update(
    app_id="unique-app-identifier",
    endpoint_id="unique-ep-identifier",
    url="https://example.com/webhook/",
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

**app_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**endpoint_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**channels:** `typing.Optional[typing.List[str]]` — List of message channels this endpoint listens to (omit for all)
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**disabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**event_types:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, str]]` 
    
</dd>
</dl>

<dl>
<dd>

**throttle_rate:** `typing.Optional[int]` 

Maximum messages per second to send to this endpoint.

Outgoing messages will be throttled to this rate.
    
</dd>
</dl>

<dl>
<dd>

**uid:** `typing.Optional[str]` — Optional unique identifier for the endpoint
    
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

<details><summary><code>client.endpoint.<a href="src/fern/endpoint/client.py">v1endpoint_delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an endpoint.
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

client.endpoint.v1endpoint_delete(
    app_id="unique-app-identifier",
    endpoint_id="unique-ep-identifier",
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

**app_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**endpoint_id:** `str` 
    
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

<details><summary><code>client.endpoint.<a href="src/fern/endpoint/client.py">patch_endpoint</a>(...) -> EndpointOut</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Partially update an endpoint.
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

client.endpoint.patch_endpoint(
    app_id="unique-app-identifier",
    endpoint_id="unique-ep-identifier",
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

**app_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**endpoint_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**channels:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**disabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**event_types:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, str]]` 
    
</dd>
</dl>

<dl>
<dd>

**throttle_rate:** `typing.Optional[int]` 

Maximum messages per second to send to this endpoint.

Outgoing messages will be throttled to this rate.
    
</dd>
</dl>

<dl>
<dd>

**uid:** `typing.Optional[str]` 
    
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

<details><summary><code>client.endpoint.<a href="src/fern/endpoint/client.py">v1endpoint_get_headers</a>(...) -> EndpointHeadersOut</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the additional headers to be sent with the webhook
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

client.endpoint.v1endpoint_get_headers(
    app_id="unique-app-identifier",
    endpoint_id="unique-ep-identifier",
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

**app_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**endpoint_id:** `str` 
    
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

<details><summary><code>client.endpoint.<a href="src/fern/endpoint/client.py">v1endpoint_update_headers</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set the additional headers to be sent with the webhook
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

client.endpoint.v1endpoint_update_headers(
    app_id="unique-app-identifier",
    endpoint_id="unique-ep-identifier",
    headers={
        "X-Example": "123",
        "X-Foobar": "Bar"
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

**app_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**endpoint_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**headers:** `typing.Dict[str, str]` 
    
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

<details><summary><code>client.endpoint.<a href="src/fern/endpoint/client.py">v1endpoint_patch_headers</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Partially set the additional headers to be sent with the webhook
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

client.endpoint.v1endpoint_patch_headers(
    app_id="unique-app-identifier",
    endpoint_id="unique-ep-identifier",
    headers={
        "X-Example": "123",
        "X-Foobar": "Bar"
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

**app_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**endpoint_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**headers:** `typing.Dict[str, typing.Optional[str]]` 
    
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

<details><summary><code>client.endpoint.<a href="src/fern/endpoint/client.py">v1endpoint_recover</a>(...) -> RecoverOut</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Resend all failed messages since a given time.
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.endpoint.v1endpoint_recover(
    app_id="unique-app-identifier",
    endpoint_id="unique-ep-identifier",
    since=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
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

**app_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**endpoint_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**since:** `datetime.datetime` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — The request's idempotency key
    
</dd>
</dl>

<dl>
<dd>

**until:** `typing.Optional[datetime.datetime]` 
    
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

<details><summary><code>client.endpoint.<a href="src/fern/endpoint/client.py">v1endpoint_get_secret</a>(...) -> EndpointSecretOut</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the endpoint's signing secret.

This is used to verify the authenticity of the webhook.
For more information please refer to [the consuming webhooks docs](https://docs.svix.com/consuming-webhooks/).
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

client.endpoint.v1endpoint_get_secret(
    app_id="unique-app-identifier",
    endpoint_id="unique-ep-identifier",
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

**app_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**endpoint_id:** `str` 
    
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

<details><summary><code>client.endpoint.<a href="src/fern/endpoint/client.py">v1endpoint_rotate_secret</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Rotates the endpoint's signing secret.  The previous secret will be valid for the next 24 hours.
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

client.endpoint.v1endpoint_rotate_secret(
    app_id="unique-app-identifier",
    endpoint_id="unique-ep-identifier",
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

**app_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**endpoint_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — The request's idempotency key
    
</dd>
</dl>

<dl>
<dd>

**grace_period_seconds:** `typing.Optional[int]` 

How long the old secret will be valid for, in seconds.

Valid values are between 0 (immediate expiry) and 7 days. The default is 24 hours.
    
</dd>
</dl>

<dl>
<dd>

**key:** `typing.Optional[str]` — The endpoint's verification secret. If `null` is passed, a secret is automatically generated. Format: `base64` encoded random bytes optionally prefixed with `whsec_`. Recommended size: 24.
    
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

<details><summary><code>client.endpoint.<a href="src/fern/endpoint/client.py">v1endpoint_send_example</a>(...) -> MessageOut</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send an example message for an event
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

client.endpoint.v1endpoint_send_example(
    app_id="unique-app-identifier",
    endpoint_id="unique-ep-identifier",
    event_type="user.signup",
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

**app_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**endpoint_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**event_type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — The request's idempotency key
    
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

<details><summary><code>client.endpoint.<a href="src/fern/endpoint/client.py">v1endpoint_get_stats</a>(...) -> EndpointStats</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get basic statistics for the endpoint.
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

client.endpoint.v1endpoint_get_stats(
    app_id="unique-app-identifier",
    endpoint_id="unique-ep-identifier",
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

**app_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**endpoint_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**until:** `typing.Optional[datetime.datetime]` 
    
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

## Message
<details><summary><code>client.message.<a href="src/fern/message/client.py">v1message_list</a>(...) -> ListResponseMessageOut</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all of the application's messages.

The `before` parameter lets you filter all items created before a certain date and is ignored if an iterator is passed.
The `after` parameter lets you filter all items created after a certain date and is ignored if an iterator is passed.
`before` and `after` cannot be used simultaneously.
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

client.message.v1message_list(
    app_id="app_id",
    iterator="msg_1srOrx2ZWZBpBUvZwXKQmoEYga2",
    channel="project_1337",
    event_types=[
        "user.signup"
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

**app_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit the number of returned items
    
</dd>
</dl>

<dl>
<dd>

**iterator:** `typing.Optional[str]` — The iterator returned from a prior invocation
    
</dd>
</dl>

<dl>
<dd>

**channel:** `typing.Optional[str]` — Filter response based on the channel
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[datetime.datetime]` — Only include items created before a certain date
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[datetime.datetime]` — Only include items created after a certain date
    
</dd>
</dl>

<dl>
<dd>

**with_content:** `typing.Optional[bool]` — When `true` message payloads are included in the response
    
</dd>
</dl>

<dl>
<dd>

**event_types:** `typing.Optional[typing.List[str]]` — Filter response based on the event type
    
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

<details><summary><code>client.message.<a href="src/fern/message/client.py">v1message_create</a>(...) -> MessageOut</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new message and dispatches it to all of the application's endpoints.

The `eventId` is an optional custom unique ID. It's verified to be unique only up to a day, after that no verification will be made.
If a message with the same `eventId` already exists for any application in your environment, a 409 conflict error will be returned.

The `eventType` indicates the type and schema of the event. All messages of a certain `eventType` are expected to have the same schema. Endpoints can choose to only listen to specific event types.
Messages can also have `channels`, which similar to event types let endpoints filter by them. Unlike event types, messages can have multiple channels, and channels don't imply a specific message content or schema.

The `payload` property is the webhook's body (the actual webhook message). Svix supports payload sizes of up to ~350kb, though it's generally a good idea to keep webhook payloads small, probably no larger than 40kb.
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

client.message.v1message_create(
    app_id="unique-app-identifier",
    event_type="user.signup",
    payload={
        "email": "test@example.com",
        "username": "test_user"
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

**app_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**event_type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**payload:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**with_content:** `typing.Optional[bool]` — When `true` message payloads are included in the response
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — The request's idempotency key
    
</dd>
</dl>

<dl>
<dd>

**application:** `typing.Optional[ApplicationIn]` 

Optionally creates a new application alongside the message.

If the application id or uid that is used in the path already exists, this argument is ignored.
    
</dd>
</dl>

<dl>
<dd>

**channels:** `typing.Optional[typing.List[str]]` — List of free-form identifiers that endpoints can filter by
    
</dd>
</dl>

<dl>
<dd>

**event_id:** `typing.Optional[str]` — Optional unique identifier for the message
    
</dd>
</dl>

<dl>
<dd>

**payload_retention_period:** `typing.Optional[int]` 
    
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

<details><summary><code>client.message.<a href="src/fern/message/client.py">v1message_bulk_expunge_content</a>(...) -> BulkExpungeContentsOut</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the payloads from the given messages under the current application

Useful in cases when a message was accidentally sent with sensitive content.
A message can't be replayed or resent once its payload has been deleted
(or has expired).
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

client.message.v1message_bulk_expunge_content(
    app_id="unique-app-identifier",
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

**app_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — The request's idempotency key
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[typing.List[str]]` — Message ID or UID to delete
    
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

<details><summary><code>client.message.<a href="src/fern/message/client.py">v1message_get</a>(...) -> MessageOut</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a message by its ID or eventID.
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

client.message.v1message_get(
    app_id="unique-app-identifier",
    msg_id="unique-msg-identifier",
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

**app_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**msg_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**with_content:** `typing.Optional[bool]` — When `true` message payloads are included in the response
    
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

<details><summary><code>client.message.<a href="src/fern/message/client.py">v1message_expunge_content</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the given message's payload. Useful in cases when a message was accidentally sent with sensitive content.

The message can't be replayed or resent once its payload has been deleted (or has expired).
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

client.message.v1message_expunge_content(
    app_id="unique-app-identifier",
    msg_id="unique-msg-identifier",
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

**app_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**msg_id:** `str` 
    
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

## Authentication
<details><summary><code>client.authentication.<a href="src/fern/authentication/client.py">v1authentication_app_portal_access</a>(...) -> AppPortalAccessOut</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use this function to get magic links (and authentication codes) for connecting your users to the Consumer Application Portal.
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

client.authentication.v1authentication_app_portal_access(
    app_id="unique-app-identifier",
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

**app_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — The request's idempotency key
    
</dd>
</dl>

<dl>
<dd>

**application:** `typing.Optional[ApplicationIn]` 

Optionally creates a new application alongside the message.

If the application id or uid that is used in the path already exists, this argument is ignored.
    
</dd>
</dl>

<dl>
<dd>

**feature_flags:** `typing.Optional[typing.List[str]]` — The set of feature flags the created token will have access to.
    
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

<details><summary><code>client.authentication.<a href="src/fern/authentication/client.py">logout_api_v1auth_logout_post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


Logout an app token.

Trying to log out other tokens will fail.
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

client.authentication.logout_api_v1auth_logout_post()

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

**idempotency_key:** `typing.Optional[str]` — The request's idempotency key
    
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

## Event Type
<details><summary><code>client.event_type.<a href="src/fern/event_type/client.py">v1event_type_list</a>(...) -> ListResponseEventTypeOut</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return the list of event types.
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

client.event_type.v1event_type_list(
    iterator="user.signup",
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

**limit:** `typing.Optional[int]` — Limit the number of returned items
    
</dd>
</dl>

<dl>
<dd>

**iterator:** `typing.Optional[str]` — The iterator returned from a prior invocation
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[Ordering]` — The sorting order of the returned items
    
</dd>
</dl>

<dl>
<dd>

**include_archived:** `typing.Optional[bool]` — When `true` archived (deleted but not expunged) items are included in the response
    
</dd>
</dl>

<dl>
<dd>

**with_content:** `typing.Optional[bool]` — When `true` the full item (including the schema) is included in the response
    
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

<details><summary><code>client.event_type.<a href="src/fern/event_type/client.py">v1event_type_create</a>(...) -> EventTypeOut</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create new or unarchive existing event type.

Unarchiving an event type will allow endpoints to filter on it and messages to be sent with it.
Endpoints filtering on the event type before archival will continue to filter on it.
This operation does not preserve the description and schemas.
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

client.event_type.v1event_type_create(
    description="A user has signed up",
    name="user.signup",
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

**description:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — The request's idempotency key
    
</dd>
</dl>

<dl>
<dd>

**archived:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**deprecated:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**feature_flag:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**schemas:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]]` — The schema for the event type for a specific version as a JSON schema.
    
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

<details><summary><code>client.event_type.<a href="src/fern/event_type/client.py">v1event_type_get</a>(...) -> EventTypeOut</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an event type.
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

client.event_type.v1event_type_get(
    event_type_name="user.signup",
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

**event_type_name:** `str` 
    
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

<details><summary><code>client.event_type.<a href="src/fern/event_type/client.py">v1event_type_update</a>(...) -> EventTypeOut</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an event type.
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

client.event_type.v1event_type_update(
    event_type_name="user.signup",
    description="A user has signed up",
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

**event_type_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**archived:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**deprecated:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**feature_flag:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**schemas:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]]` — The schema for the event type for a specific version as a JSON schema.
    
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

<details><summary><code>client.event_type.<a href="src/fern/event_type/client.py">v1event_type_delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Archive an event type.

Endpoints already configured to filter on an event type will continue to do so after archival.
However, new messages can not be sent with it and endpoints can not filter on it.
An event type can be unarchived with the
[create operation](#operation/create_event_type_api_v1_event_type__post).
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

client.event_type.v1event_type_delete(
    event_type_name="user.signup",
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

**event_type_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**expunge:** `typing.Optional[bool]` — By default event types are archived when "deleted". Passing this to `true` deletes them entirely.
    
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

<details><summary><code>client.event_type.<a href="src/fern/event_type/client.py">patch_event_type</a>(...) -> EventTypeOut</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Partially update an event type.
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

client.event_type.patch_event_type(
    event_type_name="user.signup",
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

**event_type_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**archived:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**deprecated:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**feature_flag:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**schemas:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]]` 
    
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
<details><summary><code>client.health.<a href="src/fern/health/client.py">v1health_get</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Verify the API server is up and running.
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

client.health.v1health_get()

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

