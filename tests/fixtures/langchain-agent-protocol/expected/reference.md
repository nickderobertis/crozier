# Reference
## Agents
<details><summary><code>client.agents.<a href="src/fern/agents/client.py">search_agents</a>(...) -> typing.List[Agent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Agents available in this service.
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

client.agents.search_agents()

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

**name:** `typing.Optional[str]` — Name of the agent to search.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Metadata of the agent to search.
    
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">get_agent</a>(...) -> Agent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an agent by ID.
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

client.agents.get_agent(
    agent_id="agent_id",
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

**agent_id:** `str` — The ID of the agent.
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">get_agent_schemas</a>(...) -> AgentSchema</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an agent's schemas by ID.
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

client.agents.get_agent_schemas(
    agent_id="agent_id",
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

**agent_id:** `str` — The ID of the agent.
    
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

**status:** `typing.Optional[ThreadStatus]` — Thread status to filter on.
    
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

<details><summary><code>client.threads.<a href="src/fern/threads/client.py">copy_thread</a>(...) -> Thread</code></summary>
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

client.threads.copy_thread(
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.threads.<a href="src/fern/threads/client.py">delete_thread</a>(...)</code></summary>
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

**checkpoint:** `typing.Optional[ThreadCheckpoint]` — The identifier of the checkpoint to branch from. Ignored for metadata-only patches. If not provided, defaults to the latest checkpoint.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Metadata to merge with existing thread metadata.
    
</dd>
</dl>

<dl>
<dd>

**values:** `typing.Optional[typing.Dict[str, typing.Any]]` — Values to merge with existing thread values.
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.Optional[typing.List[Message]]` — Messages to combine with current thread messages.
    
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

## Background Runs
<details><summary><code>client.background_runs.<a href="src/fern/background_runs/client.py">search_runs</a>(...) -> typing.List[Run]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List runs for a thread, agent or status
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

client.background_runs.search_runs()

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

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Run metadata to filter on.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[RunStatus]` — Run status to filter on.
    
</dd>
</dl>

<dl>
<dd>

**thread_id:** `typing.Optional[str]` — The ID of the thread to filter on.
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `typing.Optional[str]` — The ID of the agent to filter on.
    
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.background_runs.<a href="src/fern/background_runs/client.py">get_run</a>(...) -> Run</code></summary>
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

client.background_runs.get_run(
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

<details><summary><code>client.background_runs.<a href="src/fern/background_runs/client.py">delete_run</a>(...)</code></summary>
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

client.background_runs.delete_run(
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

<details><summary><code>client.background_runs.<a href="src/fern/background_runs/client.py">wait_run</a>(...) -> RunWaitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Wait for a run to finish, return the final output. If the run already finished, returns its final output immediately.
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

client.background_runs.wait_run(
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

<details><summary><code>client.background_runs.<a href="src/fern/background_runs/client.py">stream_run</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Join the output stream of an existing run. This endpoint streams output in real-time from a run similar to the /threads/__THREAD_ID__/runs/stream endpoint. Only output produced after this endpoint is called will be streamed.
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

client.background_runs.stream_run(
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

<details><summary><code>client.background_runs.<a href="src/fern/background_runs/client.py">cancel_run</a>(...)</code></summary>
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

client.background_runs.cancel_run(
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

**action:** `typing.Optional[CancelRunRequestAction]` — Action to take when cancelling the run. Possible values are `interrupt` or `rollback`. `interrupt` will simply cancel the run. `rollback` will cancel the run and delete the run and associated checkpoints afterwards.
    
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

<details><summary><code>client.background_runs.<a href="src/fern/background_runs/client.py">create_run</a>(...) -> Run</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a run in a new thread, return the run ID immediately. Don't wait for the final run output.
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

client.background_runs.create_run()

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

**request:** `RunStream` 
    
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

## Runs
<details><summary><code>client.runs.<a href="src/fern/runs/client.py">create_and_stream_run</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a run in a new thread, stream the output.
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

client.runs.create_and_stream_run()

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

**request:** `RunStream` 
    
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

<details><summary><code>client.runs.<a href="src/fern/runs/client.py">create_and_wait_run</a>(...) -> RunWaitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a run in a new thread. Wait for the final output and then return it.
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

client.runs.create_and_wait_run()

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

**request:** `RunCreate` 
    
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
<details><summary><code>client.streaming.<a href="src/fern/streaming/client.py">open_thread_websocket_stream</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upgrade to a WebSocket connection for a thread. After the connection is upgraded, clients send streaming protocol commands in-band and receive command responses plus unsolicited events on the same connection. Use `subscription.subscribe`, `subscription.unsubscribe`, and `subscription.reconnect` to manage event filters on the WebSocket.
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

client.streaming.open_thread_websocket_stream(
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

**thread_id:** `str` — The ID of the thread to open over WebSocket.
    
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

<details><summary><code>client.streaming.<a href="src/fern/streaming/client.py">open_thread_sse_stream</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Open a connection-scoped Server-Sent Events stream for a thread. The request body selects channels, namespace prefixes, optional namespace depth, and an optional sequence number to replay buffered events after. Closing the HTTP connection unsubscribes from this stream.
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
from fern import FernApi, StreamingChannelZero

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.streaming.open_thread_sse_stream(
    thread_id="thread_id",
    channels=[
        StreamingChannelZero.VALUES
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

**thread_id:** `str` — The ID of the thread whose events should be streamed.
    
</dd>
</dl>

<dl>
<dd>

**channels:** `typing.List[StreamingChannel]` — Channels to include in this event stream.
    
</dd>
</dl>

<dl>
<dd>

**namespaces:** `typing.Optional[typing.List[StreamingNamespace]]` — Namespace prefixes to include. Omit to receive matching events from all namespaces.
    
</dd>
</dl>

<dl>
<dd>

**depth:** `typing.Optional[int]` — Maximum depth below each namespace prefix.
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[int]` — Replay buffered matching events after this monotonic sequence number, then switch to live delivery.
    
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

<details><summary><code>client.streaming.<a href="src/fern/streaming/client.py">send_thread_streaming_command</a>(...) -> StreamingCommandResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send a streaming protocol command to a thread over HTTP. This endpoint is the request/response companion to the SSE event stream and supports commands such as `run.start`, `input.respond`, `input.inject`, `state.get`, `state.listCheckpoints`, and `state.fork`.
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

client.streaming.send_thread_streaming_command(
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

**thread_id:** `str` — The ID of the thread that should receive the command.
    
</dd>
</dl>

<dl>
<dd>

**id:** `int` — Client-assigned command ID used to correlate the command response.
    
</dd>
</dl>

<dl>
<dd>

**method:** `str` — Streaming protocol command method, such as `run.start`, `subscription.subscribe`, `input.respond`, or `state.get`.
    
</dd>
</dl>

<dl>
<dd>

**params:** `typing.Optional[typing.Dict[str, typing.Any]]` — Command parameters. Shape depends on the command method.
    
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

