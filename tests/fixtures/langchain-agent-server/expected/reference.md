# Reference
## Assistants
<details><summary><code>client.assistants.<a href="src/fern/assistants/client.py">create_assistant</a>(...) -> Assistant</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an assistant.

An initial version of the assistant will be created and the assistant is set to that version. To change versions, use the `POST /assistants/{assistant_id}/latest` endpoint.
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

client.assistants.create_assistant(
    graph_id="graph_id",
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

**graph_id:** `str` — The ID of the graph the assistant should use. The graph ID is normally set in your langgraph.json configuration.
    
</dd>
</dl>

<dl>
<dd>

**assistant_id:** `typing.Optional[str]` — The ID of the assistant. If not provided, a random UUID will be generated.
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[typing.Dict[str, typing.Any]]` — Configuration to use for the graph. Useful when graph is configurable and you want to create different assistants based on different configurations.
    
</dd>
</dl>

<dl>
<dd>

**context:** `typing.Optional[typing.Dict[str, typing.Any]]` — Static context added to the assistant.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Metadata to add to assistant.
    
</dd>
</dl>

<dl>
<dd>

**if_exists:** `typing.Optional[AssistantCreateIfExists]` — How to handle duplicate creation. Must be either 'raise' (raise error if duplicate), or 'do_nothing' (return existing assistant).
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the assistant. Defaults to 'Untitled'.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of the assistant. Defaults to null.
    
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

<details><summary><code>client.assistants.<a href="src/fern/assistants/client.py">search_assistants</a>(...) -> typing.List[Assistant]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for assistants.

This endpoint also functions as the endpoint to list all assistants.
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

client.assistants.search_assistants()

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

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Metadata to filter by. Exact match filter for each KV pair.
    
</dd>
</dl>

<dl>
<dd>

**graph_id:** `typing.Optional[str]` — The ID of the graph to filter by. The graph ID is normally set in your langgraph.json configuration.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the assistant to filter by. The filtering logic will match (case insensitive) assistants where 'name' is a substring of the assistant name.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of results to return.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of results to skip.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[AssistantSearchRequestSortBy]` — The field to sort by.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[AssistantSearchRequestSortOrder]` — The order to sort by.
    
</dd>
</dl>

<dl>
<dd>

**select:** `typing.Optional[typing.List[AssistantSearchRequestSelectItem]]` — Specify which fields to return. If not provided, all fields are returned.
    
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

<details><summary><code>client.assistants.<a href="src/fern/assistants/client.py">count_assistants</a>(...) -> int</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the count of assistants matching the specified criteria.
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

client.assistants.count_assistants()

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

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Metadata to filter by. Exact match filter for each KV pair.
    
</dd>
</dl>

<dl>
<dd>

**graph_id:** `typing.Optional[str]` — The ID of the graph to filter by. The graph ID is normally set in your langgraph.json configuration.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the assistant to filter by. The filtering logic will match (case insensitive) assistants where 'name' is a substring of the assistant name.
    
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

<details><summary><code>client.assistants.<a href="src/fern/assistants/client.py">get_assistant</a>(...) -> Assistant</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an assistant by ID.
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

client.assistants.get_assistant(
    assistant_id="assistant_id",
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

**assistant_id:** `str` — The ID of the assistant.
    
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

<details><summary><code>client.assistants.<a href="src/fern/assistants/client.py">delete_assistant</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an assistant by ID.

All versions of the assistant will be deleted as well.
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

client.assistants.delete_assistant(
    assistant_id="assistant_id",
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

**assistant_id:** `str` — The ID of the assistant.
    
</dd>
</dl>

<dl>
<dd>

**delete_threads:** `typing.Optional[bool]` — If true, delete all threads with metadata.assistant_id matching this assistant, along with runs and checkpoints belonging to those threads. Auth filters are applied, so threads not visible to the user will not be deleted.
    
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

<details><summary><code>client.assistants.<a href="src/fern/assistants/client.py">patch_assistant</a>(...) -> Assistant</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an assistant.
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

client.assistants.patch_assistant(
    assistant_id="assistant_id",
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

**assistant_id:** `str` — The ID of the assistant.
    
</dd>
</dl>

<dl>
<dd>

**graph_id:** `typing.Optional[str]` — The ID of the graph the assistant should use. The graph ID is normally set in your langgraph.json configuration. If not provided, assistant will keep pointing to same graph.
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[typing.Dict[str, typing.Any]]` — Configuration to use for the graph. Useful when graph is configurable and you want to update the assistant's configuration.
    
</dd>
</dl>

<dl>
<dd>

**context:** `typing.Optional[typing.Dict[str, typing.Any]]` — Static context added to the assistant.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Metadata to merge with existing assistant metadata.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The new name for the assistant. If not provided, assistant will keep its current name.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The new description for the assistant. If not provided, assistant will keep its current description.
    
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

<details><summary><code>client.assistants.<a href="src/fern/assistants/client.py">get_assistant_graph</a>(...) -> typing.Dict[str, typing.List[typing.Dict[str, typing.Any]]]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an assistant by ID.
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

client.assistants.get_assistant_graph(
    assistant_id="assistant_id",
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

**assistant_id:** `str` — The ID of the assistant.
    
</dd>
</dl>

<dl>
<dd>

**xray:** `typing.Optional[GetAssistantGraphAssistantsAssistantIdGraphGetRequestXray]` — Include graph representation of subgraphs. If an integer value is provided, only subgraphs with a depth less than or equal to the value will be included.
    
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

<details><summary><code>client.assistants.<a href="src/fern/assistants/client.py">get_assistant_subgraphs</a>(...) -> Subgraphs</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an assistant's subgraphs filtered by namespace.
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

client.assistants.get_assistant_subgraphs(
    assistant_id="assistant_id",
    namespace="namespace",
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

**assistant_id:** `str` — The ID of the assistant.
    
</dd>
</dl>

<dl>
<dd>

**namespace:** `str` — Namespace of the subgraph to filter by.
    
</dd>
</dl>

<dl>
<dd>

**recurse:** `typing.Optional[bool]` — Recursively retrieve subgraphs of subgraphs.
    
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

<details><summary><code>client.assistants.<a href="src/fern/assistants/client.py">get_assistant_schemas</a>(...) -> GraphSchema</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an assistant by ID.
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

client.assistants.get_assistant_schemas(
    assistant_id="assistant_id",
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

**assistant_id:** `str` — The ID of the assistant.
    
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

<details><summary><code>client.assistants.<a href="src/fern/assistants/client.py">get_assistant_versions_assistants_assistant_id_versions_get</a>(...) -> typing.List[Assistant]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all versions of an assistant.
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

client.assistants.get_assistant_versions_assistants_assistant_id_versions_get(
    assistant_id="assistant_id",
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

**assistant_id:** `str` — The ID of the assistant.
    
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

<details><summary><code>client.assistants.<a href="src/fern/assistants/client.py">set_latest_assistant_version_assistants_assistant_id_versions_post</a>(...) -> Assistant</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set the latest version for an assistant.
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

client.assistants.set_latest_assistant_version_assistants_assistant_id_versions_post(
    assistant_id="assistant_id",
    version=1,
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

**assistant_id:** `str` — The ID of the assistant.
    
</dd>
</dl>

<dl>
<dd>

**version:** `int` — The version to change to.
    
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

## Threads
<details><summary><code>client.threads.<a href="src/fern/threads/client.py">create_thread</a>(...) -> Thread</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a thread.
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

client.threads.create_thread()

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

**thread_id:** `typing.Optional[str]` — The ID of the thread. If not provided, a random UUID will be generated.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Metadata to add to thread.
    
</dd>
</dl>

<dl>
<dd>

**if_exists:** `typing.Optional[ThreadCreateIfExists]` — How to handle duplicate creation. Must be either 'raise' (raise error if duplicate), or 'do_nothing' (return existing thread).
    
</dd>
</dl>

<dl>
<dd>

**ttl:** `typing.Optional[ThreadCreateTtl]` — The time-to-live for the thread.
    
</dd>
</dl>

<dl>
<dd>

**supersteps:** `typing.Optional[typing.List[ThreadCreateSuperstepsItem]]` 
    
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

<details><summary><code>client.threads.<a href="src/fern/threads/client.py">search_threads</a>(...) -> typing.List[Thread]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for threads.

This endpoint also functions as the endpoint to list all threads.
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

client.threads.search_threads()

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

**ids:** `typing.Optional[typing.List[str]]` — List of thread IDs to include. Others are excluded.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Thread metadata to filter on.
    
</dd>
</dl>

<dl>
<dd>

**values:** `typing.Optional[typing.Dict[str, typing.Any]]` — State values to filter on.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ThreadSearchRequestStatus]` — Thread status to filter on.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number to return.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Offset to start from.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[ThreadSearchRequestSortBy]` — Sort by field.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[ThreadSearchRequestSortOrder]` — Sort order.
    
</dd>
</dl>

<dl>
<dd>

**select:** `typing.Optional[typing.List[ThreadSearchRequestSelectItem]]` — Specify which fields to return. If not provided, all fields are returned.
    
</dd>
</dl>

<dl>
<dd>

**extract:** `typing.Optional[typing.Dict[str, str]]` — Map of alias to JSONB path for extracting specific values. Paths must start with values, metadata, config, or interrupts. Example: {"last_msg": "values.messages[-1]"}.
    
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

<details><summary><code>client.threads.<a href="src/fern/threads/client.py">count_threads</a>(...) -> int</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the count of threads matching the specified criteria.
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

client.threads.count_threads()

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

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Thread metadata to filter on.
    
</dd>
</dl>

<dl>
<dd>

**values:** `typing.Optional[typing.Dict[str, typing.Any]]` — State values to filter on.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ThreadCountRequestStatus]` — Thread status to filter on.
    
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

<details><summary><code>client.threads.<a href="src/fern/threads/client.py">prune_threads</a>(...) -> ThreadPruneResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Prune threads by ID. The 'delete' strategy removes threads entirely. The 'keep_latest' strategy prunes old checkpoints but keeps threads and their latest state.
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

client.threads.prune_threads(
    thread_ids=[
        "thread_ids"
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

**thread_ids:** `typing.List[str]` — List of thread IDs to prune.
    
</dd>
</dl>

<dl>
<dd>

**strategy:** `typing.Optional[ThreadPruneRequestStrategy]` — The prune strategy. 'delete' removes threads entirely. 'keep_latest' prunes old checkpoints but keeps threads and their latest state.
    
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

<details><summary><code>client.threads.<a href="src/fern/threads/client.py">get_thread_storage</a>(...) -> ThreadStorage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Bytes the thread's checkpoints occupy in the built-in checkpointer, as stored: checkpoints, channel values (per channel) and pending writes. Returns 501 when a custom checkpointer is configured.
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

client.threads.get_thread_storage(
    thread_id="thread_id",
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

**thread_id:** `str` — The ID of the thread.
    
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

<details><summary><code>client.threads.<a href="src/fern/threads/client.py">get_latest_thread_state</a>(...) -> ThreadState</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get state for a thread.

The latest state of the thread (i.e. latest checkpoint) is returned.
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

client.threads.get_latest_thread_state(
    thread_id="thread_id",
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

**thread_id:** `str` — The ID of the thread.
    
</dd>
</dl>

<dl>
<dd>

**subgraphs:** `typing.Optional[bool]` — Whether to include subgraphs in the response.
    
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

<details><summary><code>client.threads.<a href="src/fern/threads/client.py">update_thread_state</a>(...) -> ThreadStateUpdateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add state to a thread.
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

client.threads.update_thread_state(
    thread_id="thread_id",
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

**thread_id:** `str` — The ID of the thread.
    
</dd>
</dl>

<dl>
<dd>

**values:** `typing.Optional[ThreadStateUpdateValues]` — The values to update the state with.
    
</dd>
</dl>

<dl>
<dd>

**checkpoint:** `typing.Optional[CheckpointConfig]` — The checkpoint to update the state of.
    
</dd>
</dl>

<dl>
<dd>

**as_node:** `typing.Optional[str]` — Update the state as if this node had just executed.
    
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

<details><summary><code>client.threads.<a href="src/fern/threads/client.py">get_thread_state_at_checkpoint</a>(...) -> ThreadState</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get state for a thread at a specific checkpoint.
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

client.threads.get_thread_state_at_checkpoint(
    thread_id="thread_id",
    checkpoint_id="checkpoint_id",
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

**thread_id:** `str` — The ID of the thread.
    
</dd>
</dl>

<dl>
<dd>

**checkpoint_id:** `str` — The ID of the checkpoint.
    
</dd>
</dl>

<dl>
<dd>

**subgraphs:** `typing.Optional[bool]` — Whether to include subgraphs in the response.
    
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

<details><summary><code>client.threads.<a href="src/fern/threads/client.py">post_thread_state_at_checkpoint_threads_thread_id_state_checkpoint_id_get</a>(...) -> ThreadState</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get state for a thread at a specific checkpoint.
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
from fern import FernApi, CheckpointConfig

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.threads.post_thread_state_at_checkpoint_threads_thread_id_state_checkpoint_id_get(
    thread_id="thread_id",
    checkpoint=CheckpointConfig(),
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

**thread_id:** `str` — The ID of the thread.
    
</dd>
</dl>

<dl>
<dd>

**checkpoint:** `CheckpointConfig` — The checkpoint to get the state for.
    
</dd>
</dl>

<dl>
<dd>

**subgraphs:** `typing.Optional[bool]` — Include subgraph states.
    
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

<details><summary><code>client.threads.<a href="src/fern/threads/client.py">get_thread_history</a>(...) -> typing.List[ThreadState]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all past states for a thread.
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

client.threads.get_thread_history(
    thread_id="thread_id",
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

**thread_id:** `str` — The ID of the thread.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` 
    
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

<details><summary><code>client.threads.<a href="src/fern/threads/client.py">get_thread_history_post</a>(...) -> typing.List[ThreadState]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all past states for a thread.
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

client.threads.get_thread_history_post(
    thread_id="thread_id",
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

**thread_id:** `str` — The ID of the thread.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of states to return.
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[CheckpointConfig]` — Return states before this checkpoint.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Filter states by metadata key-value pairs.
    
</dd>
</dl>

<dl>
<dd>

**checkpoint:** `typing.Optional[CheckpointConfig]` — Return states for this subgraph.
    
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

<details><summary><code>client.threads.<a href="src/fern/threads/client.py">copy_thread_post</a>(...) -> Thread</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new thread with a copy of the state and checkpoints from an existing thread.
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

client.threads.copy_thread_post(
    thread_id="thread_id",
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

**thread_id:** `str` — The ID of the thread.
    
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

<details><summary><code>client.threads.<a href="src/fern/threads/client.py">get_thread</a>(...) -> Thread</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a thread by ID.
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

client.threads.get_thread(
    thread_id="thread_id",
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

**thread_id:** `str` — The ID of the thread.
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[str]` — Comma-separated list of additional fields to include. Supported values: ttl
    
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

<details><summary><code>client.threads.<a href="src/fern/threads/client.py">delete_thread</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a thread by ID.
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

client.threads.delete_thread(
    thread_id="thread_id",
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

**thread_id:** `str` — The ID of the thread.
    
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

<details><summary><code>client.threads.<a href="src/fern/threads/client.py">patch_thread</a>(...) -> Thread</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a thread.
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

client.threads.patch_thread(
    thread_id="thread_id",
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

**thread_id:** `str` — The ID of the thread.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Metadata to merge with existing thread metadata.
    
</dd>
</dl>

<dl>
<dd>

**ttl:** `typing.Optional[ThreadPatchTtl]` — The time-to-live for the thread.
    
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

<details><summary><code>client.threads.<a href="src/fern/threads/client.py">join_thread_stream</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint streams output in real-time from a thread. The stream will include the output of each run executed sequentially on the thread and will remain open indefinitely. It is the responsibility of the calling client to close the connection.
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

client.threads.join_thread_stream(
    thread_id="thread_id",
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

**thread_id:** `str` — The ID of the thread.
    
</dd>
</dl>

<dl>
<dd>

**stream_modes:** `typing.Optional[JoinThreadStreamThreadsThreadIdStreamGetRequestStreamModes]` 
    
</dd>
</dl>

<dl>
<dd>

**last_event_id:** `typing.Optional[str]` 
    
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

## Streaming
<details><summary><code>client.streaming.<a href="src/fern/streaming/client.py">protocol_thread_events_post</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Open a connection-scoped SSE event stream for a thread. The request body is a `ProtocolEventStreamRequest` carrying channel and namespace filters; the server replies with `Content-Type: text/event-stream` and pushes matching `ProtocolEvent` frames for the lifetime of the connection. Closing the connection unsubscribes — no state is persisted server-side.

Reconnect: clients pass the last `seq` they received as `since` in the body. Buffered events with `seq > since` are replayed before the stream goes live. The endpoint is POST-only, so browser-native `EventSource` auto-resume (`Last-Event-ID`) does not apply — clients drive resume explicitly via the body.
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

client.streaming.protocol_thread_events_post(
    thread_id="thread_id",
    channels=[
        "channels"
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

**thread_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**channels:** `typing.List[ProtocolChannel]` — Channels to subscribe to for the lifetime of this connection.
    
</dd>
</dl>

<dl>
<dd>

**namespaces:** `typing.Optional[typing.List[ProtocolNamespace]]` — Prefix-match filter. An event matches if its namespace starts with any of these prefixes. Omit for all namespaces.
    
</dd>
</dl>

<dl>
<dd>

**depth:** `typing.Optional[int]` — Max depth below the namespace prefix. Omit for unbounded depth.
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[int]` — Replay events with `seq` greater than this value before streaming live events.
    
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

<details><summary><code>client.streaming.<a href="src/fern/streaming/client.py">protocol_thread_command_post</a>(...) -> ProtocolThreadCommandPostResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send a single protocol command scoped to a thread. The request body is a `ProtocolCommand` envelope with a `method` (e.g. `run.start`, `input.respond`, `agent.getTree`) and method-specific `params`. The response is either a `ProtocolSuccess` (with method-specific `result`) or a `ProtocolError`.

Commands that create runs (`run.start`, `input.respond`) leave the run executing in the background on the worker queue. Event streaming for that run is observed via a concurrent `POST /threads/{thread_id}/stream/events` connection.

WebSocket clients use the same command envelope in-band on `/threads/{thread_id}/stream/events` and additionally have access to `subscription.subscribe` / `subscription.unsubscribe` over the same connection.
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

client.streaming.protocol_thread_command_post(
    thread_id="thread_id",
    id=1,
    method="method",
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

**thread_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `int` — Client-assigned command id; echoed in the response.
    
</dd>
</dl>

<dl>
<dd>

**method:** `str` — Command method name (e.g. `run.start`).
    
</dd>
</dl>

<dl>
<dd>

**params:** `typing.Optional[typing.Dict[str, typing.Any]]` — Method-specific parameters. See the CDDL spec for per-method shapes.
    
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

## Thread Runs
<details><summary><code>client.thread_runs.<a href="src/fern/thread_runs/client.py">list_runs_http</a>(...) -> typing.List[Run]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List runs for a thread.
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

client.thread_runs.list_runs_http(
    thread_id="thread_id",
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

**thread_id:** `str` — The ID of the thread.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListRunsHttpThreadsThreadIdRunsGetRequestStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**select:** `typing.Optional[typing.Union[ListRunsHttpThreadsThreadIdRunsGetRequestSelectItem, typing.Sequence[ListRunsHttpThreadsThreadIdRunsGetRequestSelectItem]]]` 
    
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

<details><summary><code>client.thread_runs.<a href="src/fern/thread_runs/client.py">create_run</a>(...) -> Run</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a run in existing thread, return the run ID immediately. Don't wait for the final run output.
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

client.thread_runs.create_run(
    thread_id="thread_id",
    assistant_id="assistant_id",
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

**thread_id:** `str` — The ID of the thread.
    
</dd>
</dl>

<dl>
<dd>

**request:** `RunCreateStateful` 
    
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

<details><summary><code>client.thread_runs.<a href="src/fern/thread_runs/client.py">stream_run</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a run in existing thread. Stream the output.
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

client.thread_runs.stream_run(
    thread_id="thread_id",
    assistant_id="assistant_id",
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

**thread_id:** `str` — The ID of the thread.
    
</dd>
</dl>

<dl>
<dd>

**request:** `RunCreateStreamingStateful` 
    
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

<details><summary><code>client.thread_runs.<a href="src/fern/thread_runs/client.py">wait_run</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a run in existing thread. Wait for the final output and then return it.
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

client.thread_runs.wait_run(
    thread_id="thread_id",
    assistant_id="assistant_id",
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

**thread_id:** `str` — The ID of the thread.
    
</dd>
</dl>

<dl>
<dd>

**request:** `RunCreateStreamingStateful` 
    
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

<details><summary><code>client.thread_runs.<a href="src/fern/thread_runs/client.py">get_run_http</a>(...) -> Run</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a run by ID.
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

client.thread_runs.get_run_http(
    thread_id="thread_id",
    run_id="run_id",
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

**thread_id:** `str` — The ID of the thread.
    
</dd>
</dl>

<dl>
<dd>

**run_id:** `str` — The ID of the run.
    
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

<details><summary><code>client.thread_runs.<a href="src/fern/thread_runs/client.py">delete_run</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a run by ID.
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

client.thread_runs.delete_run(
    thread_id="thread_id",
    run_id="run_id",
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

**thread_id:** `str` — The ID of the thread.
    
</dd>
</dl>

<dl>
<dd>

**run_id:** `str` — The ID of the run.
    
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

<details><summary><code>client.thread_runs.<a href="src/fern/thread_runs/client.py">join_run_http</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Wait for a run to finish.
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

client.thread_runs.join_run_http(
    thread_id="thread_id",
    run_id="run_id",
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

**thread_id:** `str` — The ID of the thread.
    
</dd>
</dl>

<dl>
<dd>

**run_id:** `str` — The ID of the run.
    
</dd>
</dl>

<dl>
<dd>

**cancel_on_disconnect:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.thread_runs.<a href="src/fern/thread_runs/client.py">stream_run_http_threads_thread_id_runs_run_id_join_get</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Join a run stream. This endpoint streams output in real-time from a run similar to the /threads/__THREAD_ID__/runs/stream endpoint. If the run has been created with `stream_resumable=true`, the stream can be resumed from the last seen event ID.
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

client.thread_runs.stream_run_http_threads_thread_id_runs_run_id_join_get(
    thread_id="thread_id",
    run_id="run_id",
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

**thread_id:** `str` — The ID of the thread.
    
</dd>
</dl>

<dl>
<dd>

**run_id:** `str` — The ID of the run.
    
</dd>
</dl>

<dl>
<dd>

**stream_mode:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cancel_on_disconnect:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**last_event_id:** `typing.Optional[str]` 
    
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

<details><summary><code>client.thread_runs.<a href="src/fern/thread_runs/client.py">cancel_run_http</a>(...) -> typing.Any</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.thread_runs.cancel_run_http(
    thread_id="thread_id",
    run_id="run_id",
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

**thread_id:** `str` — The ID of the thread.
    
</dd>
</dl>

<dl>
<dd>

**run_id:** `str` — The ID of the run.
    
</dd>
</dl>

<dl>
<dd>

**wait:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**action:** `typing.Optional[CancelRunHttpThreadsThreadIdRunsRunIdCancelPostRequestAction]` — Action to take when cancelling the run. Possible values are `interrupt` or `rollback`. `interrupt` will simply cancel the run. `rollback` will cancel the run and delete the run and associated checkpoints afterwards.
    
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

<details><summary><code>client.thread_runs.<a href="src/fern/thread_runs/client.py">cancel_runs_post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel one or more runs. Can cancel runs by thread ID and run IDs, or by status filter.
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

client.thread_runs.cancel_runs_post(
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

**request:** `RunsCancel` 
    
</dd>
</dl>

<dl>
<dd>

**action:** `typing.Optional[CancelRunsPostRequestAction]` — Action to take when cancelling the run. Possible values are `interrupt` or `rollback`. `interrupt` will simply cancel the run. `rollback` will cancel the run and delete the run and associated checkpoints afterwards.
    
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

## Crons
<details><summary><code>client.crons.<a href="src/fern/crons/client.py">create_thread_cron</a>(...) -> Cron</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a cron to schedule runs on a thread.
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

client.crons.create_thread_cron(
    thread_id="thread_id",
    schedule="schedule",
    assistant_id="assistant_id",
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

**thread_id:** `str` — The ID of the thread.
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `str` — The cron schedule to execute this job on.
    
</dd>
</dl>

<dl>
<dd>

**assistant_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[str]` — IANA timezone for the cron schedule (e.g. 'America/New_York'). Defaults to null, which is treated as UTC.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[datetime.datetime]` — The end date to stop running the cron.
    
</dd>
</dl>

<dl>
<dd>

**input:** `typing.Optional[ThreadCronCreateInput]` — The input to the graph.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Metadata to assign to the cron job runs.
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[ThreadCronCreateConfig]` — The configuration for the assistant.
    
</dd>
</dl>

<dl>
<dd>

**context:** `typing.Optional[typing.Dict[str, typing.Any]]` — Static context added to the assistant.
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — Webhook to call after LangGraph API call is done.
    
</dd>
</dl>

<dl>
<dd>

**interrupt_before:** `typing.Optional[ThreadCronCreateInterruptBefore]` — Nodes to interrupt immediately before they get executed.
    
</dd>
</dl>

<dl>
<dd>

**interrupt_after:** `typing.Optional[ThreadCronCreateInterruptAfter]` — Nodes to interrupt immediately after they get executed.
    
</dd>
</dl>

<dl>
<dd>

**multitask_strategy:** `typing.Optional[ThreadCronCreateMultitaskStrategy]` — Multitask strategy to use. Must be one of 'reject', 'interrupt', 'rollback', or 'enqueue'.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether the cron job should be enabled. Disabled crons are not executed.
    
</dd>
</dl>

<dl>
<dd>

**stream_mode:** `typing.Optional[ThreadCronCreateStreamMode]` — The stream mode(s) to use.
    
</dd>
</dl>

<dl>
<dd>

**stream_subgraphs:** `typing.Optional[bool]` — Whether to stream output from subgraphs.
    
</dd>
</dl>

<dl>
<dd>

**stream_resumable:** `typing.Optional[bool]` — Whether to persist the stream chunks in order to resume the stream later.
    
</dd>
</dl>

<dl>
<dd>

**durability:** `typing.Optional[ThreadCronCreateDurability]` — Durability level for the run. Must be one of `sync`, `async`, or `exit`. See [durability modes](https://docs.langchain.com/oss/python/langgraph/durable-execution#durability-modes) for more details.
    
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

<details><summary><code>client.crons.<a href="src/fern/crons/client.py">create_cron</a>(...) -> Cron</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a cron to schedule runs on new threads.
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

client.crons.create_cron(
    schedule="schedule",
    assistant_id="assistant_id",
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

**schedule:** `str` — The cron schedule to execute this job on.
    
</dd>
</dl>

<dl>
<dd>

**assistant_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[str]` — IANA timezone for the cron schedule (e.g. 'America/New_York'). Defaults to null, which is treated as UTC.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[datetime.datetime]` — The end date to stop running the cron.
    
</dd>
</dl>

<dl>
<dd>

**input:** `typing.Optional[CronCreateInput]` — The input to the graph.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Metadata to assign to the cron job runs.
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[CronCreateConfig]` — The configuration for the assistant.
    
</dd>
</dl>

<dl>
<dd>

**context:** `typing.Optional[typing.Dict[str, typing.Any]]` — Static context added to the assistant.
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — Webhook to call after LangGraph API call is done.
    
</dd>
</dl>

<dl>
<dd>

**interrupt_before:** `typing.Optional[CronCreateInterruptBefore]` — Nodes to interrupt immediately before they get executed.
    
</dd>
</dl>

<dl>
<dd>

**interrupt_after:** `typing.Optional[CronCreateInterruptAfter]` — Nodes to interrupt immediately after they get executed.
    
</dd>
</dl>

<dl>
<dd>

**on_run_completed:** `typing.Optional[CronCreateOnRunCompleted]` — What to do with the thread after the run completes. 'delete' removes the thread after execution. 'keep' creates a new thread for each execution but does not clean them up.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether the cron job should be enabled. Disabled crons are not executed.
    
</dd>
</dl>

<dl>
<dd>

**stream_mode:** `typing.Optional[CronCreateStreamMode]` — The stream mode(s) to use.
    
</dd>
</dl>

<dl>
<dd>

**stream_subgraphs:** `typing.Optional[bool]` — Whether to stream output from subgraphs.
    
</dd>
</dl>

<dl>
<dd>

**stream_resumable:** `typing.Optional[bool]` — Whether to persist the stream chunks in order to resume the stream later.
    
</dd>
</dl>

<dl>
<dd>

**durability:** `typing.Optional[CronCreateDurability]` — Durability level for the run. Must be one of `sync`, `async`, or `exit`. See [durability modes](https://docs.langchain.com/oss/python/langgraph/durable-execution#durability-modes) for more details.
    
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

<details><summary><code>client.crons.<a href="src/fern/crons/client.py">search_crons_runs_crons_post</a>(...) -> typing.List[Cron]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search all active crons
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

client.crons.search_crons_runs_crons_post()

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

**assistant_id:** `typing.Optional[str]` — The assistant ID or graph name to filter by using exact match.
    
</dd>
</dl>

<dl>
<dd>

**thread_id:** `typing.Optional[str]` — The thread ID to search for.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Filter by enabled status. If not provided, returns both enabled and disabled crons.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Metadata to filter by. Exact match filter for each KV pair.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of results to return.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of results to skip.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[CronSearchSortBy]` — The field to sort by.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[CronSearchSortOrder]` — The order to sort by.
    
</dd>
</dl>

<dl>
<dd>

**select:** `typing.Optional[typing.List[CronSearchSelectItem]]` — Specify which fields to return. If not provided, all fields are returned.
    
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

<details><summary><code>client.crons.<a href="src/fern/crons/client.py">count_crons</a>(...) -> int</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the count of crons matching the specified criteria.
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

client.crons.count_crons()

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

**assistant_id:** `typing.Optional[str]` — The assistant ID or graph name to search for.
    
</dd>
</dl>

<dl>
<dd>

**thread_id:** `typing.Optional[str]` — The thread ID to search for.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Metadata to filter by. Exact match filter for each KV pair.
    
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

<details><summary><code>client.crons.<a href="src/fern/crons/client.py">get_cron</a>(...) -> Cron</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a cron by ID.
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

client.crons.get_cron(
    cron_id="cron_id",
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

**cron_id:** `str` 
    
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

<details><summary><code>client.crons.<a href="src/fern/crons/client.py">delete_cron</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a cron by ID.
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

client.crons.delete_cron(
    cron_id="cron_id",
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

**cron_id:** `str` 
    
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

<details><summary><code>client.crons.<a href="src/fern/crons/client.py">patch_cron</a>(...) -> Cron</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a cron job by ID.
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

client.crons.patch_cron(
    cron_id="cron_id",
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

**cron_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `typing.Optional[str]` — The cron schedule to execute this job on.
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[str]` — IANA timezone for the cron schedule (e.g. 'America/New_York'). Defaults to null, which is treated as UTC.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[datetime.datetime]` — The end date to stop running the cron. Send null to clear a previously set end time; omit this field to leave the existing value unchanged.
    
</dd>
</dl>

<dl>
<dd>

**input:** `typing.Optional[CronPatchInput]` — The input to the graph.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Metadata to merge with existing cron job metadata.
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[CronPatchConfig]` — The configuration for the assistant.
    
</dd>
</dl>

<dl>
<dd>

**context:** `typing.Optional[typing.Dict[str, typing.Any]]` — Static context added to the assistant.
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — Webhook to call after LangGraph API call is done.
    
</dd>
</dl>

<dl>
<dd>

**interrupt_before:** `typing.Optional[CronPatchInterruptBefore]` — Nodes to interrupt immediately before they get executed.
    
</dd>
</dl>

<dl>
<dd>

**interrupt_after:** `typing.Optional[CronPatchInterruptAfter]` — Nodes to interrupt immediately after they get executed.
    
</dd>
</dl>

<dl>
<dd>

**on_run_completed:** `typing.Optional[CronPatchOnRunCompleted]` — What to do with the thread after the run completes. 'delete' removes the thread after execution. 'keep' creates a new thread for each execution but does not clean them up.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Enable or disable the cron job.
    
</dd>
</dl>

<dl>
<dd>

**stream_mode:** `typing.Optional[CronPatchStreamMode]` — The stream mode(s) to use.
    
</dd>
</dl>

<dl>
<dd>

**stream_subgraphs:** `typing.Optional[bool]` — Whether to stream output from subgraphs.
    
</dd>
</dl>

<dl>
<dd>

**stream_resumable:** `typing.Optional[bool]` — Whether to persist the stream chunks in order to resume the stream later.
    
</dd>
</dl>

<dl>
<dd>

**durability:** `typing.Optional[CronPatchDurability]` — Durability level for the run. Must be one of `sync`, `async`, or `exit`. See [durability modes](https://docs.langchain.com/oss/python/langgraph/durable-execution#durability-modes) for more details.
    
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

## Stateless Runs
<details><summary><code>client.stateless_runs.<a href="src/fern/stateless_runs/client.py">stream_run_stateless</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a run and stream the output.
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

client.stateless_runs.stream_run_stateless(
    assistant_id="assistant_id",
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

**request:** `RunCreateStreamingStateless` 
    
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

<details><summary><code>client.stateless_runs.<a href="src/fern/stateless_runs/client.py">wait_run_stateless</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a run, wait for the final output and then return it.
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

client.stateless_runs.wait_run_stateless(
    assistant_id="assistant_id",
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

**request:** `RunCreateStreamingStateless` 
    
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

<details><summary><code>client.stateless_runs.<a href="src/fern/stateless_runs/client.py">run_stateless</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a run and return the run ID immediately. Don't wait for the final run output.
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

client.stateless_runs.run_stateless(
    assistant_id="assistant_id",
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

**request:** `RunCreateStateless` 
    
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

<details><summary><code>client.stateless_runs.<a href="src/fern/stateless_runs/client.py">run_batch_stateless_runs_post</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a batch of runs and return immediately.
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
from fern import FernApi, RunCreateStateless

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.stateless_runs.run_batch_stateless_runs_post(
    request=[
        RunCreateStateless(
            assistant_id="assistant_id",
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

**request:** `RunBatchCreate` 
    
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

## Store
<details><summary><code>client.store.<a href="src/fern/store/client.py">get_item</a>(...) -> Item</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.store.get_item(
    key="key",
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

**key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**namespace:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**refresh_ttl:** `typing.Optional[bool]` — Whether to refresh the TTL on this read operation. If not provided, uses the store's default behavior.
    
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

<details><summary><code>client.store.<a href="src/fern/store/client.py">put_item</a>(...)</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.store.put_item(
    namespace=[
        "namespace"
    ],
    key="key",
    value={
        "key": "value"
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

**namespace:** `typing.List[str]` — A list of strings representing the namespace path.
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — The unique identifier for the item within the namespace.
    
</dd>
</dl>

<dl>
<dd>

**value:** `typing.Dict[str, typing.Any]` — A dictionary containing the item's data.
    
</dd>
</dl>

<dl>
<dd>

**index:** `typing.Optional[StorePutRequestIndex]` — Controls search indexing - null (use defaults), false (disable), or list of field paths to index.
    
</dd>
</dl>

<dl>
<dd>

**ttl:** `typing.Optional[float]` — Optional time-to-live in minutes for the item, or null for no expiration.
    
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

<details><summary><code>client.store.<a href="src/fern/store/client.py">delete_item</a>(...)</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.store.delete_item(
    key="key",
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

**key:** `str` — The unique identifier for the item.
    
</dd>
</dl>

<dl>
<dd>

**namespace:** `typing.Optional[typing.List[str]]` — A list of strings representing the namespace path.
    
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

<details><summary><code>client.store.<a href="src/fern/store/client.py">search_items</a>(...) -> SearchItemsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists items ordered by last updated time. If a `query` is provided, performs a natural language search instead. Supports pagination via `limit` and `offset`, and filtering via `filter`.
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

client.store.search_items()

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

**namespace_prefix:** `typing.Optional[typing.List[str]]` — List of strings representing the namespace prefix.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Dict[str, typing.Any]]` — Optional dictionary of key-value pairs to filter results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of items to return (default is 10).
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of items to skip before returning results (default is 0).
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` — Optional natural language search query. If not provided, items are returned ordered by last updated time (listing mode). If provided, performs a natural language search over item contents.
    
</dd>
</dl>

<dl>
<dd>

**refresh_ttl:** `typing.Optional[bool]` — Whether to refresh the TTL on items returned by this search. If null, uses the store's default behavior.
    
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

<details><summary><code>client.store.<a href="src/fern/store/client.py">list_namespaces</a>(...) -> ListNamespaceResponse</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.store.list_namespaces()

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

**prefix:** `typing.Optional[typing.List[str]]` — Optional list of strings representing the prefix to filter namespaces.
    
</dd>
</dl>

<dl>
<dd>

**suffix:** `typing.Optional[typing.List[str]]` — Optional list of strings representing the suffix to filter namespaces.
    
</dd>
</dl>

<dl>
<dd>

**max_depth:** `typing.Optional[int]` — Optional integer specifying the maximum depth of namespaces to return.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of namespaces to return (default is 100).
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of namespaces to skip before returning results (default is 0).
    
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

## A2A
<details><summary><code>client.a2a.<a href="src/fern/a2a/client.py">post_a2a</a>(...) -> PostA2AResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Communicate with an assistant using the Agent-to-Agent (A2A) Protocol over JSON-RPC 2.0.
This endpoint accepts a JSON-RPC envelope and dispatches based on `method`.

**Supported Methods:**
- `message/send`: Send a message and wait for the final Task result.
- `message/stream`: Send a message and receive Server-Sent Events (SSE) JSON-RPC responses.
- `tasks/get`: Fetch the current state of a Task by ID.
- `tasks/cancel`: Request cancellation (currently not supported; returns an error).

**LangGraph Mapping:**
- `message.contextId` maps to LangGraph `thread_id`.

**Notes:**
- Only `text` and `data` parts are supported; `file` parts are not.
- If `message.contextId` is omitted, a new context is created.
- Text parts require the assistant input schema to include a `messages` field.
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
from fern.a2a import PostA2ARequestJsonrpc, PostA2ARequestMethod, PostA2ARequestParamsMessage, PostA2ARequestParamsMessageMessage, PostA2ARequestParamsMessageMessageRole, PostA2ARequestParamsMessageMessagePartsItem_Text, PostA2ARequestParamsMessageMessagePartsItem_Data

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.a2a.post_a2a(
    assistant_id="assistant_id",
    accept="Accept",
    jsonrpc=PostA2ARequestJsonrpc.TWO0,
    id="1",
    method=PostA2ARequestMethod.MESSAGE_SEND,
    params=PostA2ARequestParamsMessage(
        message=PostA2ARequestParamsMessageMessage(
            role=PostA2ARequestParamsMessageMessageRole.USER,
            parts=[
                PostA2ARequestParamsMessageMessagePartsItem_Text(
                    text="Hello from A2A",
                ),
                PostA2ARequestParamsMessageMessagePartsItem_Data(
                    data={
                        "locale": "en-US"
                    },
                )
            ],
            message_id="msg-1",
            context_id="f5bd2a40-74b6-4f7a-b649-ea3f09890003",
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

**assistant_id:** `str` — The ID of the assistant to communicate with
    
</dd>
</dl>

<dl>
<dd>

**accept:** `str` — For `message/stream`, must include `text/event-stream`. For all other methods, use `application/json`.
    
</dd>
</dl>

<dl>
<dd>

**jsonrpc:** `PostA2ARequestJsonrpc` — JSON-RPC version
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — Request identifier
    
</dd>
</dl>

<dl>
<dd>

**method:** `PostA2ARequestMethod` — The method to invoke
    
</dd>
</dl>

<dl>
<dd>

**params:** `typing.Optional[PostA2ARequestParams]` — Method parameters; shape depends on the method.
    
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

## MCP
<details><summary><code>client.mcp.<a href="src/fern/mcp/client.py">get_mcp</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Implemented according to the Streamable HTTP Transport specification.
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

client.mcp.get_mcp()

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

<details><summary><code>client.mcp.<a href="src/fern/mcp/client.py">post_mcp</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Implemented according to the Streamable HTTP Transport specification.
Sends a JSON-RPC 2.0 message to the server.

- **Request**: Provide an object with `jsonrpc`, `id`, `method`, and optional `params`.
- **Response**: Returns a JSON-RPC response or acknowledgment.

**Notes:**
- Stateless: Sessions are not persisted across requests.
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
from fern.mcp import PostMcpRequestAccept

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.mcp.post_mcp(
    accept=PostMcpRequestAccept.APPLICATION_JSON_TEXT_EVENT_STREAM,
    request={
        "jsonrpc": "2.0",
        "id": "1",
        "method": "initialize",
        "params": {"clientInfo": {"name": "test_client", "version": "1.0.0"}, "protocolVersion": "2024-11-05", "capabilities": {}}
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

**accept:** `PostMcpRequestAccept` — Accept header must include both 'application/json' and 'text/event-stream' media types.
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Any]` — A JSON-RPC 2.0 request, notification, or response object.
    
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

<details><summary><code>client.mcp.<a href="src/fern/mcp/client.py">delete_mcp</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Implemented according to the Streamable HTTP Transport specification.
Terminate an MCP session. The server implementation is stateless, so this is a no-op.

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

client.mcp.delete_mcp()

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

## System
<details><summary><code>client.system.<a href="src/fern/system/client.py">server_info</a>() -> ServerInfoInfoGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get server version information, feature flags, and metadata.
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

client.system.server_info()

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

<details><summary><code>client.system.<a href="src/fern/system/client.py">system_metrics</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get system metrics in Prometheus or JSON format for monitoring and observability.
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

client.system.system_metrics()

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

**format:** `typing.Optional[SystemMetricsMetricsGetRequestFormat]` 
    
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

<details><summary><code>client.system.<a href="src/fern/system/client.py">docs_get</a>() -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A local reference to the Agent Server API documentation.
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

client.system.docs_get()

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

<details><summary><code>client.system.<a href="src/fern/system/client.py">health_check</a>(...) -> HealthCheckOkGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check the health status of the server. Optionally check database connectivity.
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

client.system.health_check()

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

**check_db:** `typing.Optional[int]` 
    
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

