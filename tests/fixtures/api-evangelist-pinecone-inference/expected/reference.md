# Reference
## Inference
<details><summary><code>client.inference.<a href="src/fern/inference/client.py#L34-L81">embed</a>(...) -> EmbeddingsList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate vector embeddings for input data. This endpoint uses Pinecone's [hosted embedding models](https://docs.pinecone.io/guides/index-data/create-an-index#embedding-models).
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
from fern.inference import EmbedRequestInputsItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.inference.embed(
    model="multilingual-e5-large",
    inputs=[
        EmbedRequestInputsItem()
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

**model:** `str` — The [model](https://docs.pinecone.io/guides/index-data/create-an-index#embedding-models) to use for embedding generation.
    
</dd>
</dl>

<dl>
<dd>

**inputs:** `typing.List[EmbedRequestInputsItem]` — List of inputs to generate embeddings for.
    
</dd>
</dl>

<dl>
<dd>

**parameters:** `typing.Optional[typing.Dict[str, typing.Any]]` — Additional model-specific parameters. Refer to the [model guide](https://docs.pinecone.io/guides/index-data/create-an-index#embedding-models) for available model parameters.
    
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

<details><summary><code>client.inference.<a href="src/fern/inference/client.py#L83-L163">rerank</a>(...) -> RerankResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Rerank results according to their relevance to a query.

For guidance and examples, see [Rerank results](https://docs.pinecone.io/guides/search/rerank-results).
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.inference.rerank(
    model="bge-reranker-v2-m3",
    query="What is the capital of France?",
    documents=[
        {
            "id": "1",
            "text": "Paris is the capital of France.",
            "title": "France",
            "url": "https://example.com"
        }
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

**model:** `str` — The [model](https://docs.pinecone.io/guides/search/rerank-results#reranking-models) to use for reranking.
    
</dd>
</dl>

<dl>
<dd>

**query:** `str` — The query to rerank documents against.
    
</dd>
</dl>

<dl>
<dd>

**documents:** `typing.List[Document]` — The documents to rerank.
    
</dd>
</dl>

<dl>
<dd>

**top_n:** `typing.Optional[int]` — The number of results to return sorted by relevance. Defaults to the number of inputs.
    
</dd>
</dl>

<dl>
<dd>

**return_documents:** `typing.Optional[bool]` — Whether to return the documents in the response.
    
</dd>
</dl>

<dl>
<dd>

**rank_fields:** `typing.Optional[typing.List[str]]` 

The field(s) to consider for reranking. If not provided, the default is `["text"]`.

The number of fields supported is [model-specific](https://docs.pinecone.io/guides/search/rerank-results#reranking-models).
    
</dd>
</dl>

<dl>
<dd>

**parameters:** `typing.Optional[typing.Dict[str, typing.Any]]` — Additional model-specific parameters. Refer to the [model guide](https://docs.pinecone.io/guides/search/rerank-results#reranking-models) for available model parameters.
    
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

<details><summary><code>client.inference.<a href="src/fern/inference/client.py#L165-L206">list_models</a>(...) -> ModelInfoList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the embedding and reranking models hosted by Pinecone. 

You can use hosted models as an integrated part of Pinecone operations or for standalone embedding and reranking. For more details, see [Vector embedding](https://docs.pinecone.io/guides/index-data/indexing-overview#vector-embedding) and [Rerank results](https://docs.pinecone.io/guides/search/rerank-results).
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.inference.list_models(
    type="embed",
    vector_type="sparse",
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

**type:** `typing.Optional[str]` — Filter models by type ('embed' or 'rerank').
    
</dd>
</dl>

<dl>
<dd>

**vector_type:** `typing.Optional[str]` — Filter embedding models by vector type ('dense' or 'sparse'). Only relevant when `type=embed`.
    
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

<details><summary><code>client.inference.<a href="src/fern/inference/client.py#L208-L239">get_model</a>(...) -> ModelInfo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a description of a model hosted by Pinecone. 

You can use hosted models as an integrated part of Pinecone operations or for standalone embedding and reranking. For more details, see [Vector embedding](https://docs.pinecone.io/guides/index-data/indexing-overview#vector-embedding) and [Rerank results](https://docs.pinecone.io/guides/search/rerank-results).
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.inference.get_model(
    model_name="multilingual-e5-large",
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

**model_name:** `str` — The name of the model to look up.
    
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

