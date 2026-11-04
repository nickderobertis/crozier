# Reference
<details><summary><code>client.<a href="src/fern/client.py">create_response</a>(...) -> ResponseResource</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a response.
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

client.create_response()

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

**request:** `CreateResponseBody` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">compact_response</a>(...) -> CompactResource</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compact a conversation. Returns a compacted response object.
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

client.compact_response(
    model="model",
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

**model:** `str` — Model ID used to generate the response, like `gpt-5` or `o3`. OpenAI offers a wide range of models with different capabilities, performance characteristics, and price points. Refer to the [model guide](/docs/models) to browse and compare available models.
    
</dd>
</dl>

<dl>
<dd>

**input:** `typing.Optional[CompactResponseMethodPublicBodyInput]` — Text, image, or file inputs to the model, used to generate a response
    
</dd>
</dl>

<dl>
<dd>

**previous_response_id:** `typing.Optional[str]` — The unique ID of the previous response to the model. Use this to create multi-turn conversations. Learn more about [conversation state](/docs/guides/conversation-state). Cannot be used in conjunction with `conversation`.
    
</dd>
</dl>

<dl>
<dd>

**instructions:** `typing.Optional[str]` 

A system (or developer) message inserted into the model's context.
When used along with `previous_response_id`, the instructions from a previous response will not be carried over to the next response. This makes it simple to swap out system (or developer) messages in new responses.
    
</dd>
</dl>

<dl>
<dd>

**prompt_cache_key:** `typing.Optional[str]` — A key to use when reading from or writing to the prompt cache.
    
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

