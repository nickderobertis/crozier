# Reference
<details><summary><code>client.<a href="src/fern/client.py">generate</a>(...) -> GenerateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generates a response for the provided prompt
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

client.generate(
    model="gemma4",
    prompt="Why is the sky blue?",
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

**model:** `str` — Model name
    
</dd>
</dl>

<dl>
<dd>

**prompt:** `typing.Optional[str]` — Text for the model to generate a response from
    
</dd>
</dl>

<dl>
<dd>

**suffix:** `typing.Optional[str]` — Used for fill-in-the-middle models, text that appears after the user prompt and before the model response
    
</dd>
</dl>

<dl>
<dd>

**images:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[GenerateRequestFormat]` — Structured output format for the model to generate a response from. Supports either the string `"json"` or a JSON schema object.
    
</dd>
</dl>

<dl>
<dd>

**system:** `typing.Optional[str]` — System prompt for the model to generate a response from
    
</dd>
</dl>

<dl>
<dd>

**stream:** `typing.Optional[bool]` — When true, returns a stream of partial responses
    
</dd>
</dl>

<dl>
<dd>

**think:** `typing.Optional[ThinkValue]` 
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — When true, returns the raw response from the model without any prompt templating
    
</dd>
</dl>

<dl>
<dd>

**keep_alive:** `typing.Optional[GenerateRequestKeepAlive]` — Model keep-alive duration (for example `5m` or `0` to unload immediately)
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[ModelOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**logprobs:** `typing.Optional[bool]` — Whether to return log probabilities of the output tokens
    
</dd>
</dl>

<dl>
<dd>

**top_logprobs:** `typing.Optional[int]` — Number of most likely tokens to return at each token position when logprobs are enabled
    
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

<details><summary><code>client.<a href="src/fern/client.py">chat</a>(...) -> ChatResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate the next chat message in a conversation between a user and an assistant.
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
from fern import FernApi, ChatMessage
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.chat(
    model="model",
    messages=[
        ChatMessage(
            role="system",
            content="content",
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

**model:** `str` — Model name
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.List[ChatMessage]` — Chat history as an array of message objects (each with a role and content)
    
</dd>
</dl>

<dl>
<dd>

**tools:** `typing.Optional[typing.List[ToolDefinition]]` — Optional list of function tools the model may call during the chat
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[ChatRequestFormat]` — Format to return a response in. Can be `json` or a JSON schema
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[ModelOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**stream:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**think:** `typing.Optional[ThinkValue]` 
    
</dd>
</dl>

<dl>
<dd>

**keep_alive:** `typing.Optional[ChatRequestKeepAlive]` — Model keep-alive duration (for example `5m` or `0` to unload immediately)
    
</dd>
</dl>

<dl>
<dd>

**logprobs:** `typing.Optional[bool]` — Whether to return log probabilities of the output tokens
    
</dd>
</dl>

<dl>
<dd>

**top_logprobs:** `typing.Optional[int]` — Number of most likely tokens to return at each token position when logprobs are enabled
    
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

<details><summary><code>client.<a href="src/fern/client.py">embed</a>(...) -> EmbedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates vector embeddings representing the input text
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

client.embed(
    model="embeddinggemma",
    input="Generate embeddings for this text",
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

**model:** `str` — Model name
    
</dd>
</dl>

<dl>
<dd>

**input:** `EmbedRequestInput` — Text or array of texts to generate embeddings for
    
</dd>
</dl>

<dl>
<dd>

**truncate:** `typing.Optional[bool]` — If true, truncate inputs that exceed the context window. If false, returns an error.
    
</dd>
</dl>

<dl>
<dd>

**dimensions:** `typing.Optional[int]` — Number of dimensions to generate embeddings for
    
</dd>
</dl>

<dl>
<dd>

**keep_alive:** `typing.Optional[str]` — Model keep-alive duration
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[ModelOptions]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">list</a>() -> ListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch a list of models and their details
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

client.list()

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

<details><summary><code>client.<a href="src/fern/client.py">ps</a>() -> PsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of models that are currently running
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

client.ps()

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

<details><summary><code>client.<a href="src/fern/client.py">show</a>(...) -> ShowResponse</code></summary>
<dl>
<dd>

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

client.show(
    model="gemma4",
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

**model:** `str` — Model name to show
    
</dd>
</dl>

<dl>
<dd>

**verbose:** `typing.Optional[bool]` — If true, includes large verbose fields in the response.
    
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

<details><summary><code>client.<a href="src/fern/client.py">create</a>(...) -> StatusResponse</code></summary>
<dl>
<dd>

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

client.create(
    model="mario",
    from_="gemma4",
    system="You are Mario from Super Mario Bros.",
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

**model:** `str` — Name for the model to create
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[str]` — Existing model to create from
    
</dd>
</dl>

<dl>
<dd>

**template:** `typing.Optional[str]` — Prompt template to use for the model
    
</dd>
</dl>

<dl>
<dd>

**renderer:** `typing.Optional[str]` — Name of the renderer for the model
    
</dd>
</dl>

<dl>
<dd>

**parser:** `typing.Optional[str]` — Name of the parser for the model
    
</dd>
</dl>

<dl>
<dd>

**files:** `typing.Optional[typing.Dict[str, str]]` — Source file names mapped to their SHA-256 digests. Split GGUF models must include each shard under its original split filename.
    
</dd>
</dl>

<dl>
<dd>

**draft_files:** `typing.Optional[typing.Dict[str, str]]` — Draft source file names mapped to their SHA-256 digests
    
</dd>
</dl>

<dl>
<dd>

**license:** `typing.Optional[CreateRequestLicense]` — License string or list of licenses for the model
    
</dd>
</dl>

<dl>
<dd>

**system:** `typing.Optional[str]` — System prompt to embed in the model
    
</dd>
</dl>

<dl>
<dd>

**parameters:** `typing.Optional[typing.Dict[str, typing.Any]]` — Key-value parameters for the model
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.Optional[typing.List[ChatMessage]]` — Message history to use for the model
    
</dd>
</dl>

<dl>
<dd>

**quantize:** `typing.Optional[str]` — Quantization level to apply during import (e.g. `nvfp4`)
    
</dd>
</dl>

<dl>
<dd>

**draft_quantize:** `typing.Optional[str]` — Quantization level to apply to draft weights during import
    
</dd>
</dl>

<dl>
<dd>

**requires:** `typing.Optional[str]` — Minimum Ollama version required by the model
    
</dd>
</dl>

<dl>
<dd>

**stream:** `typing.Optional[bool]` — Stream status updates
    
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

<details><summary><code>client.<a href="src/fern/client.py">create_blob</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.create_blob(...)
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

**digest:** `str` — SHA256 digest identifier, prefixed with `sha256:`
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">head_blob</a>(...)</code></summary>
<dl>
<dd>

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

client.head_blob(
    digest="digest",
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

**digest:** `str` — SHA256 digest identifier, prefixed with `sha256:`
    
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

<details><summary><code>client.<a href="src/fern/client.py">copy</a>(...)</code></summary>
<dl>
<dd>

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

client.copy(
    source="gemma4",
    destination="gemma4-backup",
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

**source:** `str` — Existing model name to copy from
    
</dd>
</dl>

<dl>
<dd>

**destination:** `str` — New model name to create
    
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

<details><summary><code>client.<a href="src/fern/client.py">pull</a>(...) -> StatusResponse</code></summary>
<dl>
<dd>

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

client.pull(
    model="gemma4",
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

**model:** `str` — Name of the model to download
    
</dd>
</dl>

<dl>
<dd>

**insecure:** `typing.Optional[bool]` — Allow downloading over insecure connections
    
</dd>
</dl>

<dl>
<dd>

**stream:** `typing.Optional[bool]` — Stream progress updates
    
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

<details><summary><code>client.<a href="src/fern/client.py">push</a>(...) -> StatusResponse</code></summary>
<dl>
<dd>

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

client.push(
    model="my-username/my-model",
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

**model:** `str` — Name of the model to publish
    
</dd>
</dl>

<dl>
<dd>

**insecure:** `typing.Optional[bool]` — Allow publishing over insecure connections
    
</dd>
</dl>

<dl>
<dd>

**stream:** `typing.Optional[bool]` — Stream progress updates
    
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

<details><summary><code>client.<a href="src/fern/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

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

client.delete(
    model="gemma4",
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

**model:** `str` — Model name to delete
    
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

<details><summary><code>client.<a href="src/fern/client.py">version</a>() -> VersionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the version of the Ollama
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

client.version()

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

