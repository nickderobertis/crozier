# Reference
## conversations
<details><summary><code>client.conversations.<a href="src/fern/conversations/client.py">llm_create_conversation</a>(...) -> Conversation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an empty conversation for the caller in the org of the token.
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

client.conversations.llm_create_conversation(
    model="default",
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

**model:** `typing.Optional[ModelAlias]` 
    
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

<details><summary><code>client.conversations.<a href="src/fern/conversations/client.py">llm_get_conversation</a>(...) -> Conversation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The conversation with its messages, oldest first.
An unknown id and another owner's id both answer 404 with the same body.
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

client.conversations.llm_get_conversation(
    id="id",
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

**id:** `str` — Conversation id.
    
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

<details><summary><code>client.conversations.<a href="src/fern/conversations/client.py">llm_send_message</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stores the user message and streams the assistant answer as Server-Sent Events.
- Refusals before the first byte answer with a status code and `application/problem+json`.
- After the first byte the status stays 200. A failure is an `error` event, then the stream ends.
- Order of events: zero or more `delta`, then `usage`, then `done`. Or an `error` event at any point.
- Cancel: the client closes the connection. The server stops the model call and keeps the partial answer.
- Headers: `Cache-Control: no-store`, `X-Accel-Buffering: no`. A comment line (`: ping`) every 15 s keeps the connection open.
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

client.conversations.llm_send_message(
    id="id",
    content="What does pulse check?",
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

**id:** `str` — Conversation id.
    
</dd>
</dl>

<dl>
<dd>

**content:** `str` — The user message. Plain text. Above the server limit the answer is 413.
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[ModelAlias]` 
    
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

