# Reference
## Info
<details><summary><code>client.info.<a href="src/fern/info/client.py">live</a>() -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a live message with the SeekStorm server version.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.info.live()

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

## API Key
<details><summary><code>client.api_key.<a href="src/fern/api_key/client.py">get_api_key_info</a>() -> typing.List[IndexResponseObject]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get info about all indices associated with the specified API key
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
    environment=FernApiEnvironment.DEFAULT,
)

client.api_key.get_api_key_info()

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

<details><summary><code>client.api_key.<a href="src/fern/api_key/client.py">create_api_key</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an API key and returns the Base64 encoded API key.
Expects the Base64 encoded master API key in the header.
Use the **master API key displayed** in the server console at startup.

WARNING: make sure to set the MASTER_KEY_SECRET environment variable to a secret, otherwise your generated API keys will be compromised.
For development purposes you may also use the SeekStorm server console command 'create' to create an demo API key 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA='.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.api_key.create_api_key(
    indices_max=1,
    indices_size_max=1,
    documents_max=1,
    operations_max=1,
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

**indices_max:** `int` — number of indices per API key
    
</dd>
</dl>

<dl>
<dd>

**indices_size_max:** `int` — combined index size per API key in MB
    
</dd>
</dl>

<dl>
<dd>

**documents_max:** `int` — combined number of documents in all indices per API key
    
</dd>
</dl>

<dl>
<dd>

**operations_max:** `int` — operations per month per API key: index/update/delete/query doc
    
</dd>
</dl>

<dl>
<dd>

**rate_limit:** `typing.Optional[int]` — queries per sec per API key
    
</dd>
</dl>

<dl>
<dd>

**demo:** `typing.Optional[bool]` — create fixed demo api key instead of random api key for demo purposes (default=false)
    
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

<details><summary><code>client.api_key.<a href="src/fern/api_key/client.py">delete_api_key</a>() -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an API key and returns the number of remaining API keys.
Expects the Base64 encoded master API key in the header.
WARNING: This will delete all indices and documents associated with the API key.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.api_key.delete_api_key()

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

## Index
<details><summary><code>client.index.<a href="src/fern/index/client.py">create_index</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an index within the directory associated with the specified API key and return the index_id.
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
from fern import FernApi, SchemaField
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.index.create_index(
    index_name="index_name",
    schema=[
        SchemaField(
            field="field",
            store=True,
            index_lexical=True,
            field_type="U8",
        ),
        SchemaField(
            field="field",
            store=True,
            index_lexical=True,
            field_type="U8",
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

**index_name:** `str` — Index name, used for informational purposes only.
    
</dd>
</dl>

<dl>
<dd>

**schema:** `typing.List[SchemaField]` — Schema definition for the index: field name, field type, and indexing options. The schema defines how documents are indexed and searched. It specifies the fields that are indexed, stored, and used for faceting, as well as the field types and their properties. It also defines whether lexical, hybrid, or vector search is enabled for each field.
    
</dd>
</dl>

<dl>
<dd>

**similarity:** `typing.Optional[LexicalSimilarity]` — Specify similarity measure for the index: (default=Bm25fProximity). The similarity function is used to calculate the relevance score of search results for a given search query. The choice of similarity function can affect search performance and relevance, depending on the characteristics of the text being indexed and the search queries being executed.
    
</dd>
</dl>

<dl>
<dd>

**tokenizer:** `typing.Optional[TokenizerType]` — Specify tokenizer type for the index: (default=UnicodeAlphanumeric). The tokenizer is used to split text into tokens for indexing and searching. The choice of tokenizer can affect search performance and relevance, depending on the language and characteristics of the text being indexed.
    
</dd>
</dl>

<dl>
<dd>

**stemmer:** `typing.Optional[StemmerType]` — Specify stemmer
    
</dd>
</dl>

<dl>
<dd>

**stop_words:** `typing.Optional[StopwordType]` — Specify stop words for the index. Stop words are not indexed and not searched for. This can be used to reduce index size and improve search performance by excluding high-frequency, low-information terms from the index.
    
</dd>
</dl>

<dl>
<dd>

**frequent_words:** `typing.Optional[FrequentwordType]` — Specify frequent words for the index. Frequent words are used to optimize search performance for high-frequency terms.
    
</dd>
</dl>

<dl>
<dd>

**ngram_indexing:** `typing.Optional[int]` 

Specify n-gram indexing for the index. N-gram indexing can improve search performance for certain types of queries.
The n-gram set is defined as a bitwise combination of the following values:
- NgramSet::SingleTerm = 0b00000000,,
- NgramSet::NgramFF = 0b00000001, (Ngram frequent frequent)
- NgramSet::NgramFR = 0b00000010, (Ngram frequent rare)
- NgramSet::NgramRF = 0b00000011, (Ngram rare frequent)
- NgramSet::NgramFFF = 0b00000100, (Ngram frequent frequent frequent)
- NgramSet::NgramRFF = 0b00000101, (Ngram rare frequent frequent)
- NgramSet::NgramFFR = 0b00000110, (Ngram frequent frequent rare)
- NgramSet::NgramFRF = 0b00000111, (Ngram frequent rare frequent)

For example, to enable both NgramFF and NgramFFF, set ngram_indexing to 5 (1 | 4).
Note: enabling n-gram indexing (ngram_indexing>0) will increase index size and indexing time, but improves search performance of phrase queries with frequent terms.
    
</dd>
</dl>

<dl>
<dd>

**document_compression:** `typing.Optional[DocumentCompression]` — Enable document compression for the index. This can reduce the index size on disk and in memory, but may increase indexing and search latency. Default: Snappy compression.
    
</dd>
</dl>

<dl>
<dd>

**synonyms:** `typing.Optional[typing.List[Synonym]]` — Specify synonyms for the index. Synonyms are used to expand search queries with additional terms that have the same or similar meaning, improving recall and search relevance. The multiway option specifies whether the synonym relationship is multiway (if true, all terms in the synonym set are considered synonyms of each other) or one-way (if false, only the first term in the synonym set is considered the main term, and the other terms are considered synonyms of the main term).
    
</dd>
</dl>

<dl>
<dd>

**spelling_correction:** `typing.Optional[SpellingCorrection]` 
    
</dd>
</dl>

<dl>
<dd>

**query_completion:** `typing.Optional[QueryCompletion]` 
    
</dd>
</dl>

<dl>
<dd>

**clustering:** `typing.Optional[Clustering]` — Enable clustering for vector search.
    
</dd>
</dl>

<dl>
<dd>

**inference:** `typing.Optional[Inference]` — Enable inference for search and indexing. This can be used to create vector representations of documents and queries for semantic search, e.g. by using a model like PotionBase2M.
    
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

<details><summary><code>client.index.<a href="src/fern/index/client.py">get_index_info</a>(...) -> IndexResponseObject</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get index Info from index with index_id
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
    environment=FernApiEnvironment.DEFAULT,
)

client.index.get_index_info(
    index_id=1000000,
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

**index_id:** `int` — index id
    
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

<details><summary><code>client.index.<a href="src/fern/index/client.py">delete_index</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an index within the directory associated with the specified API key and return the number of remaining indices.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.index.delete_index(
    index_id=1000000,
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

**index_id:** `int` — index id
    
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

<details><summary><code>client.index.<a href="src/fern/index/client.py">commit_index</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Commit moves indexed documents from the intermediate uncompressed data structure (array lists/HashMap, queryable by realtime search) in RAM
to the final compressed data structure (roaring bitmap) on Mmap or disk -
which is persistent, more compact, with lower query latency and allows search with realtime=false.
Commit is invoked automatically each time 64K documents are newly indexed **per shard** as well as on close_index (e.g. server quit).
There is no way to prevent this automatic commit by not manually invoking it.
But commit can also be invoked manually at any time at any number of newly indexed documents.
commit is a **hard commit** for persistence on disk. A **soft commit** for searchability
is invoked implicitly with every index_doc,
i.e. the document can immediately searched and included in the search results
if it matches the query AND the query parameter realtime=true is enabled.
**Use commit with caution, as it is an expensive operation**.
**Usually, there is no need to invoke it manually**, as it is invoked automatically every 64k documents **per shard** and when the index is closed with close_index.
Before terminating the program, always call close_index (commit), otherwise all documents indexed since last (manual or automatic) commit are lost.
There are only 2 reasons that justify a manual commit:
1. if you want to search newly indexed documents without using realtime=true for search performance reasons or
2. if after indexing new documents there won't be more documents indexed (for some time),
   so there won't be (soon) a commit invoked automatically at the next 64k threshold **per shard** or close_index,
   but you still need immediate persistence guarantees on disk to protect against data loss in the event of a crash.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.index.commit_index(
    index_id=1000000,
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

**index_id:** `int` — index id
    
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

## Iterator
<details><summary><code>client.iterator.<a href="src/fern/iterator/client.py">document_iterator_get</a>(...) -> IteratorResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Document iterator via GET and POST are identical, only the way parameters are passed differ.
The document iterator allows to iterate over all document IDs and documents in the entire index, forward or backward.
It enables efficient sequential access to every document, even in very large indexes, without running a search.
Paging through the index works without collecting document IDs to Min-heap in size-limited RAM first.
The iterator guarantees that only valid document IDs are returned, even though document IDs are not strictly continuous.
Document IDs can also be fetched in batches, reducing round trips and significantly improving performance, especially when using the REST API.
Typical use cases include index export, conversion, analytics, audits, and inspection.
Explanation of "eventually continuous" docid:
In SeekStorm, document IDs become continuous over time. In a multi-sharded index, each shard maintains its own document ID space.
Because documents are distributed across shards in a non-deterministic, load-dependent way, shard-local document IDs advance at different rates.
When these are mapped to global document IDs, temporary gaps can appear.
As a result, simply iterating from 0 to the total document count may encounter invalid IDs near the end.
The Document Iterator abstracts this complexity and reliably returns only valid document IDs.
# Parameters
- docid=None, take>0: **skip first s document IDs**, then **take next t document IDs** of an index.
- docid=None, take<0: **skip last s document IDs**, then **take previous t document IDs** of an index.
- docid=Some, take>0: **skip next s document IDs**, then **take next t document IDs** of an index, relative to a given document ID, with end-of-index indicator.
- docid=Some, take<0: **skip previous s document IDs**, then **take previous t document IDs**, relative to a given document ID, with start-of-index indicator.
- take=0: does not make sense, that defies the purpose of get_iterator.
- The sign of take indicates the direction of iteration: positive take for forward iteration, negative take for backward iteration.
- The skip parameter is always positive, indicating the number of document IDs to skip before taking document IDs. The skip direction is determined by the sign of take too.
- include_document: if true, the documents are also retrieved along with their document IDs.
Next page:     take last  docid from previous result set, skip=1, take=+page_size
Previous page: take first docid from previous result set, skip=1, take=-page_size
Returns an IteratorResult, consisting of the number of actually skipped document IDs, and a list of taken document IDs and documents, sorted ascending).
Detect end/begin of index during iteration: if returned vec.len() < requested take || if returned skip <requested skip
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
    environment=FernApiEnvironment.DEFAULT,
)

client.iterator.document_iterator_get(
    index_id=1000000,
    document_id=1000000,
    skip=1000000,
    take=1000000,
    include_deleted=True,
    include_document=True,
    fields=[
        "title",
        "body"
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

**index_id:** `int` — index id
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `int` — document id
    
</dd>
</dl>

<dl>
<dd>

**skip:** `int` — skip document IDs
    
</dd>
</dl>

<dl>
<dd>

**take:** `int` — take document IDs
    
</dd>
</dl>

<dl>
<dd>

**include_deleted:** `bool` — include deleted document IDs in results
    
</dd>
</dl>

<dl>
<dd>

**include_document:** `bool` — include documents in results
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — fields to include in document. If not specified, all fields are included
    
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

<details><summary><code>client.iterator.<a href="src/fern/iterator/client.py">document_iterator_post</a>(...) -> IteratorResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Document iterator via GET and POST are identical, only the way parameters are passed differ.
The document iterator allows to iterate over all document IDs and documents in the entire index, forward or backward.
It enables efficient sequential access to every document, even in very large indexes, without running a search.
Paging through the index works without collecting document IDs to Min-heap in size-limited RAM first.
The iterator guarantees that only valid document IDs are returned, even though document IDs are not strictly continuous.
Document IDs can also be fetched in batches, reducing round trips and significantly improving performance, especially when using the REST API.
Typical use cases include index export, conversion, analytics, audits, and inspection.
Explanation of "eventually continuous" docid:
In SeekStorm, document IDs become continuous over time. In a multi-sharded index, each shard maintains its own document ID space.
Because documents are distributed across shards in a non-deterministic, load-dependent way, shard-local document IDs advance at different rates.
When these are mapped to global document IDs, temporary gaps can appear.
As a result, simply iterating from 0 to the total document count may encounter invalid IDs near the end.
The Document Iterator abstracts this complexity and reliably returns only valid document IDs.
# Parameters
- docid=None, take>0: **skip first s document IDs**, then **take next t document IDs** of an index.
- docid=None, take<0: **skip last s document IDs**, then **take previous t document IDs** of an index.
- docid=Some, take>0: **skip next s document IDs**, then **take next t document IDs** of an index, relative to a given document ID, with end-of-index indicator.
- docid=Some, take<0: **skip previous s document IDs**, then **take previous t document IDs**, relative to a given document ID, with start-of-index indicator.
- take=0: does not make sense, that defies the purpose of get_iterator.
- The sign of take indicates the direction of iteration: positive take for forward iteration, negative take for backward iteration.
- The skip parameter is always positive, indicating the number of document IDs to skip before taking document IDs. The skip direction is determined by the sign of take too.
- include_document: if true, the documents are also retrieved along with their document IDs.
Next page:     take last  docid from previous result set, skip=1, take=+page_size
Previous page: take first docid from previous result set, skip=1, take=-page_size
Returns an IteratorResult, consisting of the number of actually skipped document IDs, and a list of taken document IDs and documents, sorted ascending).
Detect end/begin of index during iteration: if returned vec.len() < requested take || if returned skip <requested skip
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
    environment=FernApiEnvironment.DEFAULT,
)

client.iterator.document_iterator_post(
    index_id=1000000,
    skip=0,
    take=-1,
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

**index_id:** `int` — index id
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `typing.Optional[int]` 

base document ID to start the iteration from
Use None to start from the beginning (take>0) or the end (take<0) of the index
In JSON use null for None
    
</dd>
</dl>

<dl>
<dd>

**skip:** `typing.Optional[int]` — the number of document IDs to skip
    
</dd>
</dl>

<dl>
<dd>

**take:** `typing.Optional[int]` 

the number of document IDs to return
take>0: take next t document IDs, take<0: take previous t document IDs
    
</dd>
</dl>

<dl>
<dd>

**include_deleted:** `typing.Optional[bool]` — if true, also deleted document IDs are included in the result
    
</dd>
</dl>

<dl>
<dd>

**include_document:** `typing.Optional[bool]` — if true, the documents are also retrieved along with their document IDs
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.List[str]]` — which fields to return (if include_document is true, if empty then return all stored fields)
    
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

## Document
<details><summary><code>client.document.<a href="src/fern/document/client.py">index_document</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Index a JSON document or an array of JSON documents (bulk), each consisting of arbitrary key-value pairs to the index with the specified apikey and index_id, and return the number of indexed docs.
Index documents enables true real-time search (as opposed to near realtime.search):
When in query_index the parameter `realtime` is set to `true` then indexed, but uncommitted documents are immediately included in the search results, without requiring a commit or refresh.
Therefore a explicit commit_index is almost never required, as it is invoked automatically after 64k documents are indexed **per shard** or on close_index for persistence.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.document.index_document(
    index_id=1000000,
    request={
        "string": {"key": "value"}
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

**index_id:** `int` — index id
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Any]` 
    
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

<details><summary><code>client.document.<a href="src/fern/document/client.py">delete_document_by_request_object</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete document by document_id, by array of document_id (bulk), by query (SearchRequestObject) from index with index_id, or clear all documents from index.
Immediately effective, independent of commit.
Index space used by deleted documents is not reclaimed (until compaction is implemented), but result_count_total is updated.
By manually deleting the delete.bin file the deleted documents can be recovered (until compaction).
Deleted documents impact performance, especially but not limited to counting (Count, TopKCount). They also increase the size of the index (until compaction is implemented).
For minimal query latency delete index and reindexing documents is preferred over deleting documents (until compaction is implemented).
BM25 scores are not updated (until compaction is implemented), but the impact is minimal.
Document ID can by obtained by search. When deleting by query (SearchRequestObject), it is advised to perform a dry run search first, to see which documents will be deleted.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.document.delete_document_by_request_object(
    index_id=1000000,
    query="query",
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

**index_id:** `int` — index id
    
</dd>
</dl>

<dl>
<dd>

**request:** `SearchRequestObject` 
    
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

<details><summary><code>client.document.<a href="src/fern/document/client.py">update_document</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a JSON document or an array of JSON documents (bulk), each consisting of arbitrary key-value pairs to the index with the specified apikey and index_id, and return the number of indexed docs.
Update document is a combination of delete_document and index_document.
All current limitations of delete_document apply.
Update documents enables true real-time search (as opposed to near realtime.search):
When in query_index the parameter `realtime` is set to `true` then indexed, but uncommitted documents are immediately included in the search results, without requiring a commit or refresh.
Therefore a explicit commit_index is almost never required, as it is invoked automatically after 64k documents are indexed **per shard** or on close_index for persistence.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.document.update_document(
    index_id=1000000,
    request=[
        {"key": "value"},
        {"key": "value"}
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

**index_id:** `int` — index id
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[typing.Any]` 
    
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

<details><summary><code>client.document.<a href="src/fern/document/client.py">get_document</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get document from index with index_id
⚠️ Use search or get_iterator first to obtain a valid doc_id. Document IDs are not guaranteed to be continuous and gapless!
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
    environment=FernApiEnvironment.DEFAULT,
)

client.document.get_document(
    index_id=1000000,
    document_id=1000000,
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

**index_id:** `int` — index id
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `int` — document id
    
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

<details><summary><code>client.document.<a href="src/fern/document/client.py">delete_document_by_parameter</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete document by document_id from index with index_id
⚠️ Use search or get_iterator first to obtain a valid doc_id. Document IDs are not guaranteed to be continuous and gapless!
Immediately effective, independent of commit.
Index space used by deleted documents is not reclaimed (until compaction is implemented), but result_count_total is updated.
By manually deleting the delete.bin file the deleted documents can be recovered (until compaction).
Deleted documents impact performance, especially but not limited to counting (Count, TopKCount). They also increase the size of the index (until compaction is implemented).
For minimal query latency delete index and reindexing documents is preferred over deleting documents (until compaction is implemented).
BM25 scores are not updated (until compaction is implemented), but the impact is minimal.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.document.delete_document_by_parameter(
    index_id=1000000,
    document_id=1000000,
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

**index_id:** `int` — index id
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `int` — document id
    
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

## PDF File
<details><summary><code>client.pdf_file.<a href="src/fern/pdf_file/client.py">index_pdf_file</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Index PDF file (byte array) to the index with the specified apikey and index_id, and return the number of indexed docs.
- Converts PDF to a JSON document with "title", "body", "url" and "date" fields and indexes it.
- extracts title from metatag, or first line of text, or from filename
- extracts creation date from metatag, or from file creation date (Unix timestamp: the number of seconds since 1 January 1970)
- copies all ingested pdf files to "files" subdirectory in index
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
client.pdf_file.index_pdf_file(...)
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

**index_id:** `int` — index id
    
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

<details><summary><code>client.pdf_file.<a href="src/fern/pdf_file/client.py">get_pdf_file</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get PDF file from index with index_id
⚠️ Use search or get_iterator first to obtain s valid doc_id. Document IDs are not guaranteed to be continuous and gapless!
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
    environment=FernApiEnvironment.DEFAULT,
)

client.pdf_file.get_pdf_file(
    index_id=1000000,
    document_id=1000000,
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

**index_id:** `int` — index id
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `int` — document id
    
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

## Query
<details><summary><code>client.query.<a href="src/fern/query/client.py">index_get</a>(...) -> SearchResultObject</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Query results from index with index_id.
Query index via GET is a convenience function, that **offers only a limited set of parameters compared to Query Index via POST**.
Always use Query Index via POST for the full set of parameters and maximum flexibility.
Query Index via GET is provided for simple queries and quick testing, and to be easily callable from browser address bar, but it is not intended for production use.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.query.index_get(
    index_id=1000000,
    query="hello",
    offset=1000000,
    length=1000000,
    realtime=True,
    enable_empty_query=True,
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

**index_id:** `int` — index id
    
</dd>
</dl>

<dl>
<dd>

**query:** `str` — query string
    
</dd>
</dl>

<dl>
<dd>

**offset:** `int` — result offset
    
</dd>
</dl>

<dl>
<dd>

**length:** `int` — result length
    
</dd>
</dl>

<dl>
<dd>

**realtime:** `bool` — include uncommitted documents
    
</dd>
</dl>

<dl>
<dd>

**enable_empty_query:** `bool` — allow empty query
    
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

<details><summary><code>client.query.<a href="src/fern/query/client.py">index_post</a>(...) -> SearchResultObject</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Query results from index with index_id
The following parameters are supported:
- Result type
- Result sorting
- Realtime search
- Field filter
- Fields to include in search results
- Distance fields: derived fields from distance calculations
- Highlights: keyword-in-context snippets and term highlighting
- Query facets: which facets fields to calculate and return at query time
- Facet filter: filter facets by field and value
- Result sort: sort results by field and direction
- Query type default: default query type, if not specified in query
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
from fern import FernApi, Highlight, SearchModeHybrid, SearchModeHybridHybrid, AnnModeNprobe
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.query.index_post(
    index_id=1000000,
    query="detroit",
    enable_empty_query=False,
    offset=0,
    length=10,
    result_type="TopkCount",
    realtime=True,
    highlights=[
        Highlight(
            field="",
            name="",
            fragment_number=0,
            fragment_size=0,
            highlight_markup=True,
            pre_tags="",
            post_tags="",
        )
    ],
    field_filter=[
        "title"
    ],
    fields=[
        "fields"
    ],
    query_type_default="Intersection",
    query_rewriting="SearchOnly",
    search_mode=SearchModeHybrid(
        hybrid=SearchModeHybridHybrid(
            similarity_threshold=0.7,
            ann_mode=AnnModeNprobe(
                nprobe=55,
            ),
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

**index_id:** `int` — index id
    
</dd>
</dl>

<dl>
<dd>

**request:** `SearchRequestObject` 
    
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

