# Reference
## ContextualCompletions
<details><summary><code>client.contextual_completions.<a href="src/fern/contextual_completions/client.py">prompt_completion_v1completions_post_stream</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

We recommend most users use our Chat completions API.

Given a prompt, the model will return one predicted completion.

Optionally include a `system_prompt` to influence the way the LLM answers.

If `use_context`
is set to `true`, the model will use context coming from the ingested documents
to create the response. The documents being used can be filtered using the
`context_filter` and passing the document IDs to be used. Ingested documents IDs
can be found using `/ingest/list` endpoint. If you want all ingested documents to
be used, remove `context_filter` altogether.

When using `'include_sources': true`, the API will return the source Chunks used
to create the response, which come from the context provided.

When using `'stream': true`, the API will return data chunks following [OpenAI's
streaming model](https://platform.openai.com/docs/api-reference/chat/streaming):
```
{"id":"12345","object":"completion.chunk","created":1694268190,
"model":"private-gpt","choices":[{"index":0,"delta":{"content":"Hello"},
"finish_reason":null}]}
```
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

client.contextual_completions.prompt_completion_v1completions_post_stream(
    prompt="How do you fry an egg?",
    system_prompt="You are a rapper. Always answer with a rap.",
    use_context=False,
    include_sources=False,
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

**prompt:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**stream:** `typing.Literal` 
    
</dd>
</dl>

<dl>
<dd>

**system_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**use_context:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**context_filter:** `typing.Optional[ContextFilter]` 
    
</dd>
</dl>

<dl>
<dd>

**include_sources:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.contextual_completions.<a href="src/fern/contextual_completions/client.py">prompt_completion</a>(...) -> OpenAiCompletion</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

We recommend most users use our Chat completions API.

Given a prompt, the model will return one predicted completion.

Optionally include a `system_prompt` to influence the way the LLM answers.

If `use_context`
is set to `true`, the model will use context coming from the ingested documents
to create the response. The documents being used can be filtered using the
`context_filter` and passing the document IDs to be used. Ingested documents IDs
can be found using `/ingest/list` endpoint. If you want all ingested documents to
be used, remove `context_filter` altogether.

When using `'include_sources': true`, the API will return the source Chunks used
to create the response, which come from the context provided.

When using `'stream': true`, the API will return data chunks following [OpenAI's
streaming model](https://platform.openai.com/docs/api-reference/chat/streaming):
```
{"id":"12345","object":"completion.chunk","created":1694268190,
"model":"private-gpt","choices":[{"index":0,"delta":{"content":"Hello"},
"finish_reason":null}]}
```
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

client.contextual_completions.prompt_completion_v1completions_post_stream(
    prompt="How do you fry an egg?",
    system_prompt="You are a rapper. Always answer with a rap.",
    use_context=False,
    include_sources=False,
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

**prompt:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**stream:** `typing.Literal` 
    
</dd>
</dl>

<dl>
<dd>

**system_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**use_context:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**context_filter:** `typing.Optional[ContextFilter]` 
    
</dd>
</dl>

<dl>
<dd>

**include_sources:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.contextual_completions.<a href="src/fern/contextual_completions/client.py">chat_completion_v1chat_completions_post_stream</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Given a list of messages comprising a conversation, return a response.

Optionally include an initial `role: system` message to influence the way
the LLM answers.

If `use_context` is set to `true`, the model will use context coming
from the ingested documents to create the response. The documents being used can
be filtered using the `context_filter` and passing the document IDs to be used.
Ingested documents IDs can be found using `/ingest/list` endpoint. If you want
all ingested documents to be used, remove `context_filter` altogether.

When using `'include_sources': true`, the API will return the source Chunks used
to create the response, which come from the context provided.

When using `'stream': true`, the API will return data chunks following [OpenAI's
streaming model](https://platform.openai.com/docs/api-reference/chat/streaming):
```
{"id":"12345","object":"completion.chunk","created":1694268190,
"model":"private-gpt","choices":[{"index":0,"delta":{"content":"Hello"},
"finish_reason":null}]}
```
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
from fern import FernApi, OpenAiMessage, OpenAiMessageRole, ContextFilter

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.contextual_completions.chat_completion_v1chat_completions_post_stream(
    messages=[
        OpenAiMessage(
            role=OpenAiMessageRole.SYSTEM,
            content="You are a rapper. Always answer with a rap.",
        ),
        OpenAiMessage(
            role=OpenAiMessageRole.USER,
            content="How do you fry an egg?",
        )
    ],
    use_context=True,
    context_filter=ContextFilter(
        docs_ids=[
            "c202d5e6-7b69-4869-81cc-dd574ee8ee11"
        ],
    ),
    include_sources=True,
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

**messages:** `typing.List[OpenAiMessage]` 
    
</dd>
</dl>

<dl>
<dd>

**stream:** `typing.Literal` 
    
</dd>
</dl>

<dl>
<dd>

**use_context:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**context_filter:** `typing.Optional[ContextFilter]` 
    
</dd>
</dl>

<dl>
<dd>

**include_sources:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.contextual_completions.<a href="src/fern/contextual_completions/client.py">chat_completion</a>(...) -> OpenAiCompletion</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Given a list of messages comprising a conversation, return a response.

Optionally include an initial `role: system` message to influence the way
the LLM answers.

If `use_context` is set to `true`, the model will use context coming
from the ingested documents to create the response. The documents being used can
be filtered using the `context_filter` and passing the document IDs to be used.
Ingested documents IDs can be found using `/ingest/list` endpoint. If you want
all ingested documents to be used, remove `context_filter` altogether.

When using `'include_sources': true`, the API will return the source Chunks used
to create the response, which come from the context provided.

When using `'stream': true`, the API will return data chunks following [OpenAI's
streaming model](https://platform.openai.com/docs/api-reference/chat/streaming):
```
{"id":"12345","object":"completion.chunk","created":1694268190,
"model":"private-gpt","choices":[{"index":0,"delta":{"content":"Hello"},
"finish_reason":null}]}
```
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
from fern import FernApi, OpenAiMessage, OpenAiMessageRole, ContextFilter

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.contextual_completions.chat_completion_v1chat_completions_post_stream(
    messages=[
        OpenAiMessage(
            role=OpenAiMessageRole.SYSTEM,
            content="You are a rapper. Always answer with a rap.",
        ),
        OpenAiMessage(
            role=OpenAiMessageRole.USER,
            content="How do you fry an egg?",
        )
    ],
    use_context=True,
    context_filter=ContextFilter(
        docs_ids=[
            "c202d5e6-7b69-4869-81cc-dd574ee8ee11"
        ],
    ),
    include_sources=True,
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

**messages:** `typing.List[OpenAiMessage]` 
    
</dd>
</dl>

<dl>
<dd>

**stream:** `typing.Literal` 
    
</dd>
</dl>

<dl>
<dd>

**use_context:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**context_filter:** `typing.Optional[ContextFilter]` 
    
</dd>
</dl>

<dl>
<dd>

**include_sources:** `typing.Optional[bool]` 
    
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

## ContextChunks
<details><summary><code>client.context_chunks.<a href="src/fern/context_chunks/client.py">chunks_retrieval</a>(...) -> ChunksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Given a `text`, returns the most relevant chunks from the ingested documents.

The returned information can be used to generate prompts that can be
passed to `/completions` or `/chat/completions` APIs. Note: it is usually a very
fast API, because only the Embeddings model is involved, not the LLM. The
returned information contains the relevant chunk `text` together with the source
`document` it is coming from. It also contains a score that can be used to
compare different results.

The max number of chunks to be returned is set using the `limit` param.

Previous and next chunks (pieces of text that appear right before or after in the
document) can be fetched by using the `prev_next_chunks` field.

The documents being used can be filtered using the `context_filter` and passing
the document IDs to be used. Ingested documents IDs can be found using
`/ingest/list` endpoint. If you want all ingested documents to be used,
remove `context_filter` altogether.
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

client.context_chunks.chunks_retrieval(
    text="Q3 2023 sales",
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

**text:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**context_filter:** `typing.Optional[ContextFilter]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**prev_next_chunks:** `typing.Optional[int]` 
    
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

## Ingestion
<details><summary><code>client.ingestion.<a href="src/fern/ingestion/client.py">ingest</a>(...) -> IngestResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Ingests and processes a file.

Deprecated. Use ingest/file instead.
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

client.ingestion.ingest(
    file="example_file",
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

**file:** `core.File` 
    
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

<details><summary><code>client.ingestion.<a href="src/fern/ingestion/client.py">ingest_file</a>(...) -> IngestResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Ingests and processes a file, storing its chunks to be used as context.

The context obtained from files is later used in
`/chat/completions`, `/completions`, and `/chunks` APIs.

Most common document
formats are supported, but you may be prompted to install an extra dependency to
manage a specific file type.

A file can generate different Documents (for example a PDF generates one Document
per page). All Documents IDs are returned in the response, together with the
extracted Metadata (which is later used to improve context retrieval). Those IDs
can be used to filter the context used to create responses in
`/chat/completions`, `/completions`, and `/chunks` APIs.
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

client.ingestion.ingest_file(
    file="example_file",
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

**file:** `core.File` 
    
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

<details><summary><code>client.ingestion.<a href="src/fern/ingestion/client.py">ingest_text</a>(...) -> IngestResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Ingests and processes a text, storing its chunks to be used as context.

The context obtained from files is later used in
`/chat/completions`, `/completions`, and `/chunks` APIs.

A Document will be generated with the given text. The Document
ID is returned in the response, together with the
extracted Metadata (which is later used to improve context retrieval). That ID
can be used to filter the context used to create responses in
`/chat/completions`, `/completions`, and `/chunks` APIs.
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

client.ingestion.ingest_text(
    file_name="Avatar: The Last Airbender",
    text="Avatar is set in an Asian and Arctic-inspired world in which some people can telekinetically manipulate one of the four elements—water, earth, fire or air—through practices known as \'bending\', inspired by Chinese martial arts.",
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

**file_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**text:** `str` 
    
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

<details><summary><code>client.ingestion.<a href="src/fern/ingestion/client.py">list_ingested</a>() -> IngestResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists already ingested Documents including their Document ID and metadata.

Those IDs can be used to filter the context used to create responses
in `/chat/completions`, `/completions`, and `/chunks` APIs.
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

client.ingestion.list_ingested()

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

<details><summary><code>client.ingestion.<a href="src/fern/ingestion/client.py">delete_ingested</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the specified ingested Document.

The `doc_id` can be obtained from the `GET /ingest/list` endpoint.
The document will be effectively deleted from your storage context.
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

client.ingestion.delete_ingested(
    doc_id="doc_id",
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

**doc_id:** `str` 
    
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

## Recipes
<details><summary><code>client.recipes.<a href="src/fern/recipes/client.py">summarize</a>(...) -> SummarizeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Given a text, the model will return a summary.

Optionally include `instructions` to influence the way the summary is generated.

If `use_context`
is set to `true`, the model will also use the content coming from the ingested
documents in the summary. The documents being used can
be filtered by their metadata using the `context_filter`.
Ingested documents metadata can be found using `/ingest/list` endpoint.
If you want all ingested documents to be used, remove `context_filter` altogether.

If `prompt` is set, it will be used as the prompt for the summarization,
otherwise the default prompt will be used.

When using `'stream': true`, the API will return data chunks following [OpenAI's
streaming model](https://platform.openai.com/docs/api-reference/chat/streaming):
```
{"id":"12345","object":"completion.chunk","created":1694268190,
"model":"private-gpt","choices":[{"index":0,"delta":{"content":"Hello"},
"finish_reason":null}]}
```
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

client.recipes.summarize()

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

**text:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**use_context:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**context_filter:** `typing.Optional[ContextFilter]` 
    
</dd>
</dl>

<dl>
<dd>

**prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**instructions:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**stream:** `typing.Optional[bool]` 
    
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

## Embeddings
<details><summary><code>client.embeddings.<a href="src/fern/embeddings/client.py">embeddings_generation</a>(...) -> EmbeddingsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a vector representation of a given input.

That vector representation can be easily consumed
by machine learning models and algorithms.
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

client.embeddings.embeddings_generation(
    input="input",
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

**input:** `EmbeddingsBodyInput` 
    
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
<details><summary><code>client.health.<a href="src/fern/health/client.py">health</a>() -> HealthResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return ok if the system is up.
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

client.health.health()

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

