# Reference
## Archives
<details><summary><code>client.archives.<a href="src/fern/archives/client.py">list_archives</a>(...) -> typing.List[Archive]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of all archives for the current organization with optional filters and pagination.
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

client.archives.list_archives()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**before:** `typing.Optional[str]` — Archive ID cursor for pagination. Returns archives that come before this archive ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Archive ID cursor for pagination. Returns archives that come after this archive ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of archives to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListArchivesRequestOrder]` — Sort order for archives by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[ListArchivesRequestOrderBy]` — Field to sort by
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Filter by archive name (exact match)
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `typing.Optional[str]` — Only archives attached to this agent ID
    
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

<details><summary><code>client.archives.<a href="src/fern/archives/client.py">create_archive</a>(...) -> Archive</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new archive.
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

client.archives.create_archive(
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

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**embedding_config:** `typing.Optional[EmbeddingConfig]` — Deprecated: Use `embedding` field instead. Embedding configuration for the archive
    
</dd>
</dl>

<dl>
<dd>

**embedding:** `typing.Optional[str]` — Embedding model handle for the archive
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
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

<details><summary><code>client.archives.<a href="src/fern/archives/client.py">retrieve_archive</a>(...) -> Archive</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a single archive by its ID.
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

client.archives.retrieve_archive(
    archive_id="archive-123e4567-e89b-42d3-8456-426614174000",
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

**archive_id:** `str` — The ID of the archive in the format 'archive-<uuid4>'
    
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

<details><summary><code>client.archives.<a href="src/fern/archives/client.py">delete_archive</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an archive by its ID.
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

client.archives.delete_archive(
    archive_id="archive-123e4567-e89b-42d3-8456-426614174000",
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

**archive_id:** `str` — The ID of the archive in the format 'archive-<uuid4>'
    
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

<details><summary><code>client.archives.<a href="src/fern/archives/client.py">modify_archive</a>(...) -> Archive</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing archive's name and/or description.
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

client.archives.modify_archive(
    archive_id="archive-123e4567-e89b-42d3-8456-426614174000",
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

**archive_id:** `str` — The ID of the archive in the format 'archive-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
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

<details><summary><code>client.archives.<a href="src/fern/archives/client.py">list_agents_for_archive</a>(...) -> typing.List[AgentState]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of agents that have access to an archive with pagination support.
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

client.archives.list_agents_for_archive(
    archive_id="archive-123e4567-e89b-42d3-8456-426614174000",
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

**archive_id:** `str` — The ID of the archive in the format 'archive-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Agent ID cursor for pagination. Returns agents that come before this agent ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Agent ID cursor for pagination. Returns agents that come after this agent ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of agents to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListAgentsForArchiveRequestOrder]` — Sort order for agents by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.Union[ListAgentsForArchiveRequestIncludeItem, typing.Sequence[ListAgentsForArchiveRequestIncludeItem]]]` — Specify which relational fields to include in the response. No relationships are included by default.
    
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

<details><summary><code>client.archives.<a href="src/fern/archives/client.py">create_passage_in_archive</a>(...) -> Passage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new passage in an archive.

This adds a passage to the archive and creates embeddings for vector storage.
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

client.archives.create_passage_in_archive(
    archive_id="archive-123e4567-e89b-42d3-8456-426614174000",
    text="text",
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

**archive_id:** `str` — The ID of the archive in the format 'archive-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**text:** `str` — The text content of the passage
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Optional metadata for the passage
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` — Optional tags for categorizing the passage
    
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

<details><summary><code>client.archives.<a href="src/fern/archives/client.py">delete_passage_from_archive</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a passage from an archive.

This permanently removes the passage from both the database and vector storage (if applicable).
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

client.archives.delete_passage_from_archive(
    archive_id="archive-123e4567-e89b-42d3-8456-426614174000",
    passage_id="passage-123e4567-e89b-42d3-8456-426614174000",
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

**archive_id:** `str` — The ID of the archive in the format 'archive-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**passage_id:** `str` — The ID of the passage in the format 'passage-<uuid4>'
    
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

## Tools
<details><summary><code>client.tools.<a href="src/fern/tools/client.py">retrieve_tool</a>(...) -> Tool</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a tool by ID
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

client.tools.retrieve_tool(
    tool_id="tool-123e4567-e89b-42d3-8456-426614174000",
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

**tool_id:** `str` — The ID of the tool in the format 'tool-<uuid4>'
    
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

<details><summary><code>client.tools.<a href="src/fern/tools/client.py">delete_tool</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a tool by name
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

client.tools.delete_tool(
    tool_id="tool-123e4567-e89b-42d3-8456-426614174000",
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

**tool_id:** `str` — The ID of the tool in the format 'tool-<uuid4>'
    
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

<details><summary><code>client.tools.<a href="src/fern/tools/client.py">modify_tool</a>(...) -> Tool</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing tool
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

client.tools.modify_tool(
    tool_id="tool-123e4567-e89b-42d3-8456-426614174000",
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

**tool_id:** `str` — The ID of the tool in the format 'tool-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of the tool.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` — Metadata tags.
    
</dd>
</dl>

<dl>
<dd>

**source_code:** `typing.Optional[str]` — The source code of the function.
    
</dd>
</dl>

<dl>
<dd>

**source_type:** `typing.Optional[str]` — The type of the source code.
    
</dd>
</dl>

<dl>
<dd>

**json_schema:** `typing.Optional[typing.Dict[str, typing.Any]]` — The JSON schema of the function (auto-generated from source_code if not provided)
    
</dd>
</dl>

<dl>
<dd>

**args_json_schema:** `typing.Optional[typing.Dict[str, typing.Any]]` — The args JSON schema of the function.
    
</dd>
</dl>

<dl>
<dd>

**return_char_limit:** `typing.Optional[int]` — The maximum number of characters in the response.
    
</dd>
</dl>

<dl>
<dd>

**pip_requirements:** `typing.Optional[typing.List[PipRequirement]]` — Optional list of pip packages required by this tool.
    
</dd>
</dl>

<dl>
<dd>

**npm_requirements:** `typing.Optional[typing.List[NpmRequirement]]` — Optional list of npm packages required by this tool.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — A dictionary of additional metadata for the tool.
    
</dd>
</dl>

<dl>
<dd>

**default_requires_approval:** `typing.Optional[bool]` — Whether or not to require approval before executing this tool.
    
</dd>
</dl>

<dl>
<dd>

**enable_parallel_execution:** `typing.Optional[bool]` — If set to True, then this tool will potentially be executed concurrently with other tools. Default False.
    
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

<details><summary><code>client.tools.<a href="src/fern/tools/client.py">count_tools</a>(...) -> int</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a count of all tools available to agents belonging to the org of the user.
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

client.tools.count_tools()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**names:** `typing.Optional[typing.List[str]]` — Filter by specific tool names
    
</dd>
</dl>

<dl>
<dd>

**tool_ids:** `typing.Optional[typing.List[str]]` — Filter by specific tool IDs - accepts repeated params or comma-separated values
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Search tool names (case-insensitive partial match)
    
</dd>
</dl>

<dl>
<dd>

**tool_types:** `typing.Optional[typing.List[str]]` — Filter by tool type(s) - accepts repeated params or comma-separated values
    
</dd>
</dl>

<dl>
<dd>

**exclude_tool_types:** `typing.Optional[typing.List[str]]` — Tool type(s) to exclude - accepts repeated params or comma-separated values
    
</dd>
</dl>

<dl>
<dd>

**return_only_letta_tools:** `typing.Optional[bool]` — Count only tools with tool_type starting with 'letta_'
    
</dd>
</dl>

<dl>
<dd>

**exclude_letta_tools:** `typing.Optional[bool]` — Exclude built-in Letta tools from the count
    
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

<details><summary><code>client.tools.<a href="src/fern/tools/client.py">list_tools</a>(...) -> typing.List[Tool]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of all tools available to agents.
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

client.tools.list_tools()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**before:** `typing.Optional[str]` — Tool ID cursor for pagination. Returns tools that come before this tool ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Tool ID cursor for pagination. Returns tools that come after this tool ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of tools to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListToolsRequestOrder]` — Sort order for tools by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[ListToolsRequestOrderBy]` — Field to sort by
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Filter by single tool name
    
</dd>
</dl>

<dl>
<dd>

**names:** `typing.Optional[typing.List[str]]` — Filter by specific tool names
    
</dd>
</dl>

<dl>
<dd>

**tool_ids:** `typing.Optional[typing.List[str]]` — Filter by specific tool IDs - accepts repeated params or comma-separated values
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Search tool names (case-insensitive partial match)
    
</dd>
</dl>

<dl>
<dd>

**tool_types:** `typing.Optional[typing.List[str]]` — Filter by tool type(s) - accepts repeated params or comma-separated values
    
</dd>
</dl>

<dl>
<dd>

**exclude_tool_types:** `typing.Optional[typing.List[str]]` — Tool type(s) to exclude - accepts repeated params or comma-separated values
    
</dd>
</dl>

<dl>
<dd>

**return_only_letta_tools:** `typing.Optional[bool]` — Return only tools with tool_type starting with 'letta_'
    
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

<details><summary><code>client.tools.<a href="src/fern/tools/client.py">create_tool</a>(...) -> Tool</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new tool
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

client.tools.create_tool(
    source_code="source_code",
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

**request:** `ToolCreate` 
    
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

<details><summary><code>client.tools.<a href="src/fern/tools/client.py">upsert_tool</a>(...) -> Tool</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or update a tool
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

client.tools.upsert_tool(
    source_code="source_code",
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

**request:** `ToolCreate` 
    
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

<details><summary><code>client.tools.<a href="src/fern/tools/client.py">search_tools</a>(...) -> typing.List[ToolSearchResult]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search tools using semantic search.

Requires tool embedding to be enabled (embed_tools=True). Uses vector search,
full-text search, or hybrid mode to find tools matching the query.

Returns tools ranked by relevance with their search scores.
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

client.tools.search_tools()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `typing.Optional[str]` — Text query for semantic search.
    
</dd>
</dl>

<dl>
<dd>

**search_mode:** `typing.Optional[ToolSearchRequestSearchMode]` — Search mode: vector, fts, or hybrid.
    
</dd>
</dl>

<dl>
<dd>

**tool_types:** `typing.Optional[typing.List[str]]` — Filter by tool types (e.g., 'custom', 'letta_core').
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` — Filter by tags (match any).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of results to return.
    
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

<details><summary><code>client.tools.<a href="src/fern/tools/client.py">add_base_tools</a>() -> typing.List[Tool]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upsert base tools
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

client.tools.add_base_tools()

```
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

<details><summary><code>client.tools.<a href="src/fern/tools/client.py">run_tool_from_source</a>(...) -> ToolReturnMessage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Attempt to build a tool from source, then run it on the provided arguments
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

client.tools.run_tool_from_source(
    source_code="source_code",
    args={
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

**source_code:** `str` — The source code of the function.
    
</dd>
</dl>

<dl>
<dd>

**args:** `typing.Dict[str, typing.Any]` — The arguments to pass to the tool.
    
</dd>
</dl>

<dl>
<dd>

**env_vars:** `typing.Optional[typing.Dict[str, str]]` — The environment variables to pass to the tool.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the tool to run.
    
</dd>
</dl>

<dl>
<dd>

**source_type:** `typing.Optional[str]` — The type of the source code.
    
</dd>
</dl>

<dl>
<dd>

**args_json_schema:** `typing.Optional[typing.Dict[str, typing.Any]]` — The args JSON schema of the function.
    
</dd>
</dl>

<dl>
<dd>

**json_schema:** `typing.Optional[typing.Dict[str, typing.Any]]` — The JSON schema of the function (auto-generated from source_code if not provided)
    
</dd>
</dl>

<dl>
<dd>

**pip_requirements:** `typing.Optional[typing.List[PipRequirement]]` — Optional list of pip packages required by this tool.
    
</dd>
</dl>

<dl>
<dd>

**npm_requirements:** `typing.Optional[typing.List[NpmRequirement]]` — Optional list of npm packages required by this tool.
    
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

<details><summary><code>client.tools.<a href="src/fern/tools/client.py">list_mcp_servers</a>() -> typing.Dict[str, ListMcpServersResponseValue]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of all configured MCP servers
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

client.tools.list_mcp_servers()

```
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

<details><summary><code>client.tools.<a href="src/fern/tools/client.py">add_mcp_server</a>(...) -> typing.List[AddMcpServerResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a new MCP server to the Letta MCP server config
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
from fern import FernApi, StdioServerConfig
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.tools.add_mcp_server(
    request=StdioServerConfig(
        server_name="server_name",
        command="command",
        args=[
            "args"
        ],
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

**request:** `AddMcpServerRequest` 
    
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

<details><summary><code>client.tools.<a href="src/fern/tools/client.py">list_mcp_tools_by_server</a>(...) -> typing.List[McpTool]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of all tools for a specific MCP server
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

client.tools.list_mcp_tools_by_server(
    mcp_server_name="mcp_server_name",
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

**mcp_server_name:** `str` 
    
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

<details><summary><code>client.tools.<a href="src/fern/tools/client.py">resync_mcp_server_tools</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Resync tools for an MCP server by:
1. Fetching current tools from the MCP server
2. Deleting tools that no longer exist on the server
3. Updating schemas for existing tools
4. Adding new tools from the server

Returns a summary of changes made.
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

client.tools.resync_mcp_server_tools(
    mcp_server_name="mcp_server_name",
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

**mcp_server_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `typing.Optional[str]` 
    
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

<details><summary><code>client.tools.<a href="src/fern/tools/client.py">add_mcp_tool</a>(...) -> Tool</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Register a new MCP tool as a Letta server by MCP server + tool name
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

client.tools.add_mcp_tool(
    mcp_server_name="mcp_server_name",
    mcp_tool_name="mcp_tool_name",
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

**mcp_server_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**mcp_tool_name:** `str` 
    
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

<details><summary><code>client.tools.<a href="src/fern/tools/client.py">delete_mcp_server</a>(...) -> typing.List[DeleteMcpServerResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a MCP server configuration
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

client.tools.delete_mcp_server(
    mcp_server_name="mcp_server_name",
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

**mcp_server_name:** `str` 
    
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

<details><summary><code>client.tools.<a href="src/fern/tools/client.py">update_mcp_server</a>(...) -> UpdateMcpServerResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing MCP server configuration
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
from fern import FernApi, LettaSchemasMcpUpdateStdioMcpServer
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.tools.update_mcp_server(
    mcp_server_name="mcp_server_name",
    request=LettaSchemasMcpUpdateStdioMcpServer(),
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

**mcp_server_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateMcpServerRequestBody` 
    
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

<details><summary><code>client.tools.<a href="src/fern/tools/client.py">test_mcp_server</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Test connection to an MCP server without adding it.
Returns the list of available tools if successful.
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
from fern import FernApi, StdioServerConfig
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.tools.test_mcp_server(
    request=StdioServerConfig(
        server_name="server_name",
        command="command",
        args=[
            "args"
        ],
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

**request:** `TestMcpServerRequest` 
    
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

<details><summary><code>client.tools.<a href="src/fern/tools/client.py">connect_mcp_server</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Connect to an MCP server with support for OAuth via SSE.
Returns a stream of events handling authorization state and exchange if OAuth is required.
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
from fern import FernApi, StdioServerConfig
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.tools.connect_mcp_server(
    request=StdioServerConfig(
        server_name="server_name",
        command="command",
        args=[
            "args"
        ],
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

**request:** `ConnectMcpServerRequest` 
    
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

<details><summary><code>client.tools.<a href="src/fern/tools/client.py">execute_mcp_tool</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Execute a specific MCP tool from a configured server.
Returns the tool execution result.
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

client.tools.execute_mcp_tool(
    mcp_server_name="mcp_server_name",
    tool_name="tool_name",
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

**mcp_server_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**tool_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**args:** `typing.Optional[typing.Dict[str, typing.Any]]` — Arguments to pass to the tool
    
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

<details><summary><code>client.tools.<a href="src/fern/tools/client.py">mcp_oauth_callback</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Handle OAuth callback for MCP server authentication.
Session is identified via the state parameter instead of URL path.
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

client.tools.mcp_oauth_callback()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**code:** `typing.Optional[str]` — OAuth authorization code
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[str]` — OAuth state parameter
    
</dd>
</dl>

<dl>
<dd>

**error:** `typing.Optional[str]` — OAuth error
    
</dd>
</dl>

<dl>
<dd>

**error_description:** `typing.Optional[str]` — OAuth error description
    
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
<details><summary><code>client.sources.<a href="src/fern/sources/client.py">count_sources</a>() -> int</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Count all data sources created by a user.
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

client.sources.count_sources()

```
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

<details><summary><code>client.sources.<a href="src/fern/sources/client.py">retrieve_source</a>(...) -> Source</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all sources
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

client.sources.retrieve_source(
    source_id="source-123e4567-e89b-42d3-8456-426614174000",
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

**source_id:** `str` — The ID of the source in the format 'source-<uuid4>'
    
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

<details><summary><code>client.sources.<a href="src/fern/sources/client.py">delete_source</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a data source.
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

client.sources.delete_source(
    source_id="source-123e4567-e89b-42d3-8456-426614174000",
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

**source_id:** `str` — The ID of the source in the format 'source-<uuid4>'
    
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

<details><summary><code>client.sources.<a href="src/fern/sources/client.py">modify_source</a>(...) -> Source</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the name or documentation of an existing data source.
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

client.sources.modify_source(
    source_id="source-123e4567-e89b-42d3-8456-426614174000",
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

**source_id:** `str` — The ID of the source in the format 'source-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**request:** `SourceUpdate` 
    
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

<details><summary><code>client.sources.<a href="src/fern/sources/client.py">get_source_id_by_name</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a source by name
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

client.sources.get_source_id_by_name(
    source_name="source_name",
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

**source_name:** `str` 
    
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

<details><summary><code>client.sources.<a href="src/fern/sources/client.py">get_sources_metadata</a>(...) -> OrganizationSourcesStats</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get aggregated metadata for all sources in an organization.

Returns structured metadata including:
- Total number of sources
- Total number of files across all sources
- Total size of all files
- Per-source breakdown with file details (file_name, file_size per file) if include_detailed_per_source_metadata is True
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

client.sources.get_sources_metadata()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**include_detailed_per_source_metadata:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.sources.<a href="src/fern/sources/client.py">list_sources</a>() -> typing.List[Source]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all data sources created by a user.
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

client.sources.list_sources()

```
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

<details><summary><code>client.sources.<a href="src/fern/sources/client.py">create_source</a>(...) -> Source</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new data source.
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

client.sources.create_source(
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

**request:** `SourceCreate` 
    
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

<details><summary><code>client.sources.<a href="src/fern/sources/client.py">upload_file_to_source</a>(...) -> FileMetadata</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload a file to a data source.
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

client.sources.upload_file_to_source(
    source_id="source-123e4567-e89b-42d3-8456-426614174000",
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

**source_id:** `str` — The ID of the source in the format 'source-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**file:** `core.File` 
    
</dd>
</dl>

<dl>
<dd>

**duplicate_handling:** `typing.Optional[DuplicateFileHandling]` — How to handle duplicate filenames
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Optional custom name to override the uploaded file's name
    
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

<details><summary><code>client.sources.<a href="src/fern/sources/client.py">get_agents_for_source</a>(...) -> typing.List[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all agent IDs that have the specified source attached.
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

client.sources.get_agents_for_source(
    source_id="source-123e4567-e89b-42d3-8456-426614174000",
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

**source_id:** `str` — The ID of the source in the format 'source-<uuid4>'
    
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

<details><summary><code>client.sources.<a href="src/fern/sources/client.py">list_source_passages</a>(...) -> typing.List[Passage]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all passages associated with a data source.
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

client.sources.list_source_passages(
    source_id="source-123e4567-e89b-42d3-8456-426614174000",
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

**source_id:** `str` — The ID of the source in the format 'source-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Message after which to retrieve the returned messages.
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Message before which to retrieve the returned messages.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of messages to retrieve.
    
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

<details><summary><code>client.sources.<a href="src/fern/sources/client.py">list_source_files</a>(...) -> typing.List[FileMetadata]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List paginated files associated with a data source.
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

client.sources.list_source_files(
    source_id="source-123e4567-e89b-42d3-8456-426614174000",
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

**source_id:** `str` — The ID of the source in the format 'source-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of files to return
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Pagination cursor to fetch the next set of results
    
</dd>
</dl>

<dl>
<dd>

**include_content:** `typing.Optional[bool]` — Whether to include full file content
    
</dd>
</dl>

<dl>
<dd>

**check_status_updates:** `typing.Optional[bool]` — Whether to check and update file processing status (from the vector db service). If False, will not fetch and update the status, which may lead to performance gains.
    
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

<details><summary><code>client.sources.<a href="src/fern/sources/client.py">get_file_metadata</a>(...) -> FileMetadata</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve metadata for a specific file by its ID.
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

client.sources.get_file_metadata(
    source_id="source-123e4567-e89b-42d3-8456-426614174000",
    file_id="file-123e4567-e89b-42d3-8456-426614174000",
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

**source_id:** `str` — The ID of the source in the format 'source-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `str` — The ID of the file in the format 'file-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**include_content:** `typing.Optional[bool]` — Whether to include full file content
    
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

<details><summary><code>client.sources.<a href="src/fern/sources/client.py">delete_file_from_source</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a data source.
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

client.sources.delete_file_from_source(
    source_id="source-123e4567-e89b-42d3-8456-426614174000",
    file_id="file-123e4567-e89b-42d3-8456-426614174000",
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

**source_id:** `str` — The ID of the source in the format 'source-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `str` — The ID of the file in the format 'file-<uuid4>'
    
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

## Folders
<details><summary><code>client.folders.<a href="src/fern/folders/client.py">count_folders</a>() -> int</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Count all data folders created by a user.
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

client.folders.count_folders()

```
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

<details><summary><code>client.folders.<a href="src/fern/folders/client.py">retrieve_folder</a>(...) -> Folder</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a folder by ID
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

client.folders.retrieve_folder(
    folder_id="source-123e4567-e89b-42d3-8456-426614174000",
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

**folder_id:** `str` — The ID of the source in the format 'source-<uuid4>'
    
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

<details><summary><code>client.folders.<a href="src/fern/folders/client.py">delete_folder</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a data folder.
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

client.folders.delete_folder(
    folder_id="source-123e4567-e89b-42d3-8456-426614174000",
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

**folder_id:** `str` — The ID of the source in the format 'source-<uuid4>'
    
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

<details><summary><code>client.folders.<a href="src/fern/folders/client.py">modify_folder</a>(...) -> Folder</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the name or documentation of an existing data folder.
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

client.folders.modify_folder(
    folder_id="source-123e4567-e89b-42d3-8456-426614174000",
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

**folder_id:** `str` — The ID of the source in the format 'source-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**request:** `SourceUpdate` 
    
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

<details><summary><code>client.folders.<a href="src/fern/folders/client.py">get_folder_by_name</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**Deprecated**: Please use the list endpoint `GET /v1/folders?name=` instead.


Get a folder by name.
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

client.folders.get_folder_by_name(
    folder_name="folder_name",
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

**folder_name:** `str` 
    
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

<details><summary><code>client.folders.<a href="src/fern/folders/client.py">retrieve_metadata</a>(...) -> OrganizationSourcesStats</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get aggregated metadata for all folders in an organization.

Returns structured metadata including:
- Total number of folders
- Total number of files across all folders
- Total size of all files
- Per-source breakdown with file details (file_name, file_size per file) if include_detailed_per_source_metadata is True
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

client.folders.retrieve_metadata()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**include_detailed_per_source_metadata:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.folders.<a href="src/fern/folders/client.py">list_folders</a>(...) -> typing.List[Folder]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all data folders created by a user.
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

client.folders.list_folders()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**before:** `typing.Optional[str]` — Folder ID cursor for pagination. Returns folders that come before this folder ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Folder ID cursor for pagination. Returns folders that come after this folder ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of folders to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListFoldersRequestOrder]` — Sort order for folders by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[ListFoldersRequestOrderBy]` — Field to sort by
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Folder name to filter by
    
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

<details><summary><code>client.folders.<a href="src/fern/folders/client.py">create_folder</a>(...) -> Folder</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new data folder.
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

client.folders.create_folder(
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

**request:** `SourceCreate` 
    
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

<details><summary><code>client.folders.<a href="src/fern/folders/client.py">upload_file_to_folder</a>(...) -> FileMetadata</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload a file to a data folder.
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

client.folders.upload_file_to_folder(
    folder_id="source-123e4567-e89b-42d3-8456-426614174000",
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

**folder_id:** `str` — The ID of the source in the format 'source-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**file:** `core.File` 
    
</dd>
</dl>

<dl>
<dd>

**duplicate_handling:** `typing.Optional[DuplicateFileHandling]` — How to handle duplicate filenames
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Optional custom name to override the uploaded file's name
    
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

<details><summary><code>client.folders.<a href="src/fern/folders/client.py">list_agents_for_folder</a>(...) -> typing.List[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all agent IDs that have the specified folder attached.
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

client.folders.list_agents_for_folder(
    folder_id="source-123e4567-e89b-42d3-8456-426614174000",
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

**folder_id:** `str` — The ID of the source in the format 'source-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Agent ID cursor for pagination. Returns agents that come before this agent ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Agent ID cursor for pagination. Returns agents that come after this agent ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of agents to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListAgentsForFolderRequestOrder]` — Sort order for agents by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[ListAgentsForFolderRequestOrderBy]` — Field to sort by
    
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

<details><summary><code>client.folders.<a href="src/fern/folders/client.py">list_folder_passages</a>(...) -> typing.List[Passage]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all passages associated with a data folder.
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

client.folders.list_folder_passages(
    folder_id="source-123e4567-e89b-42d3-8456-426614174000",
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

**folder_id:** `str` — The ID of the source in the format 'source-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Passage ID cursor for pagination. Returns passages that come before this passage ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Passage ID cursor for pagination. Returns passages that come after this passage ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of passages to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListFolderPassagesRequestOrder]` — Sort order for passages by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[ListFolderPassagesRequestOrderBy]` — Field to sort by
    
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

<details><summary><code>client.folders.<a href="src/fern/folders/client.py">list_files_for_folder</a>(...) -> typing.List[FileMetadata]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List paginated files associated with a data folder.
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

client.folders.list_files_for_folder(
    folder_id="source-123e4567-e89b-42d3-8456-426614174000",
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

**folder_id:** `str` — The ID of the source in the format 'source-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — File ID cursor for pagination. Returns files that come before this file ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — File ID cursor for pagination. Returns files that come after this file ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of files to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListFilesForFolderRequestOrder]` — Sort order for files by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[ListFilesForFolderRequestOrderBy]` — Field to sort by
    
</dd>
</dl>

<dl>
<dd>

**include_content:** `typing.Optional[bool]` — Whether to include full file content
    
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

<details><summary><code>client.folders.<a href="src/fern/folders/client.py">retrieve_file</a>(...) -> FileMetadata</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a file from a folder by ID.
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

client.folders.retrieve_file(
    folder_id="source-123e4567-e89b-42d3-8456-426614174000",
    file_id="file-123e4567-e89b-42d3-8456-426614174000",
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

**folder_id:** `str` — The ID of the source in the format 'source-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `str` — The ID of the file in the format 'file-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**include_content:** `typing.Optional[bool]` — Whether to include full file content
    
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

<details><summary><code>client.folders.<a href="src/fern/folders/client.py">delete_file_from_folder</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a file from a folder.
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

client.folders.delete_file_from_folder(
    folder_id="source-123e4567-e89b-42d3-8456-426614174000",
    file_id="file-123e4567-e89b-42d3-8456-426614174000",
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

**folder_id:** `str` — The ID of the source in the format 'source-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `str` — The ID of the file in the format 'file-<uuid4>'
    
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

## Agents
<details><summary><code>client.agents.<a href="src/fern/agents/client.py">list_agents</a>(...) -> typing.List[AgentState]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of all agents.
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

client.agents.list_agents()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the agent
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` — List of tags to filter agents by
    
</dd>
</dl>

<dl>
<dd>

**match_all_tags:** `typing.Optional[bool]` — If True, only returns agents that match ALL given tags. Otherwise, return agents that have ANY of the passed-in tags.
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Cursor for pagination
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Cursor for pagination
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit for pagination
    
</dd>
</dl>

<dl>
<dd>

**query_text:** `typing.Optional[str]` — Search agents by name
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — Search agents by project ID - this will default to your default project on cloud
    
</dd>
</dl>

<dl>
<dd>

**template_id:** `typing.Optional[str]` — Search agents by template ID
    
</dd>
</dl>

<dl>
<dd>

**base_template_id:** `typing.Optional[str]` — Search agents by base template ID
    
</dd>
</dl>

<dl>
<dd>

**identity_id:** `typing.Optional[str]` — Search agents by identity ID
    
</dd>
</dl>

<dl>
<dd>

**identifier_keys:** `typing.Optional[typing.List[str]]` — Search agents by identifier keys
    
</dd>
</dl>

<dl>
<dd>

**include_relationships:** `typing.Optional[typing.List[str]]` — Specify which relational fields (e.g., 'tools', 'sources', 'memory') to include in the response. If not provided, all relationships are loaded by default. Using this can optimize performance by reducing unnecessary joins.This is a legacy parameter, and no longer supported after 1.0.0 SDK versions.
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.Union[ListAgentsRequestIncludeItem, typing.Sequence[ListAgentsRequestIncludeItem]]]` — Specify which relational fields to include in the response. No relationships are included by default.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListAgentsRequestOrder]` — Sort order for agents by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[ListAgentsRequestOrderBy]` — Field to sort by
    
</dd>
</dl>

<dl>
<dd>

**ascending:** `typing.Optional[bool]` — Whether to sort agents oldest to newest (True) or newest to oldest (False, default)
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[str]` — Field to sort by. Options: 'created_at' (default), 'last_run_completion'
    
</dd>
</dl>

<dl>
<dd>

**last_stop_reason:** `typing.Optional[StopReasonType]` — Filter agents by their last stop reason.
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">create_agent</a>(...) -> AgentState</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an agent.
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

client.agents.create_agent()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**project:** `typing.Optional[str]` — The project slug to associate with the agent (cloud only).
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the agent.
    
</dd>
</dl>

<dl>
<dd>

**memory_blocks:** `typing.Optional[typing.List[CreateBlock]]` — The blocks to create in the agent's in-context memory.
    
</dd>
</dl>

<dl>
<dd>

**tools:** `typing.Optional[typing.List[str]]` — The tools used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**tool_ids:** `typing.Optional[typing.List[str]]` — The ids of the tools used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**source_ids:** `typing.Optional[typing.List[str]]` — Deprecated: Use `folder_ids` field instead. The ids of the sources used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**folder_ids:** `typing.Optional[typing.List[str]]` — The ids of the folders used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**block_ids:** `typing.Optional[typing.List[str]]` — The ids of the blocks used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**tool_rules:** `typing.Optional[typing.List[CreateAgentRequestToolRulesItem]]` — The tool rules governing the agent.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` — The tags associated with the agent.
    
</dd>
</dl>

<dl>
<dd>

**system:** `typing.Optional[str]` — The system prompt used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**agent_type:** `typing.Optional[AgentType]` — The type of agent.
    
</dd>
</dl>

<dl>
<dd>

**initial_message_sequence:** `typing.Optional[typing.List[MessageCreate]]` — The initial set of messages to put in the agent's in-context memory.
    
</dd>
</dl>

<dl>
<dd>

**include_base_tools:** `typing.Optional[bool]` — If true, attaches the Letta core tools (e.g. core_memory related functions).
    
</dd>
</dl>

<dl>
<dd>

**include_multi_agent_tools:** `typing.Optional[bool]` — If true, attaches the Letta multi-agent tools (e.g. sending a message to another agent).
    
</dd>
</dl>

<dl>
<dd>

**include_base_tool_rules:** `typing.Optional[bool]` — If true, attaches the Letta base tool rules (e.g. deny all tools not explicitly allowed).
    
</dd>
</dl>

<dl>
<dd>

**include_default_source:** `typing.Optional[bool]` — If true, automatically creates and attaches a default data source for this agent.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of the agent.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — The metadata of the agent.
    
</dd>
</dl>

<dl>
<dd>

**llm_config:** `typing.Optional[LlmConfig]` — Deprecated: Use `model` field instead. The LLM configuration used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**embedding_config:** `typing.Optional[EmbeddingConfig]` — Deprecated: Use `embedding` field instead. The embedding configuration used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` — The model handle for the agent to use (format: provider/model-name).
    
</dd>
</dl>

<dl>
<dd>

**embedding:** `typing.Optional[str]` — The embedding model handle used by the agent (format: provider/model-name).
    
</dd>
</dl>

<dl>
<dd>

**model_settings:** `typing.Optional[CreateAgentRequestModelSettings]` — The model settings for the agent.
    
</dd>
</dl>

<dl>
<dd>

**compaction_settings:** `typing.Optional[CompactionSettingsInput]` — The compaction settings configuration used for compaction.
    
</dd>
</dl>

<dl>
<dd>

**context_window_limit:** `typing.Optional[int]` — The context window limit used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**embedding_chunk_size:** `typing.Optional[int]` — Deprecated: No longer used. The embedding chunk size used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**max_tokens:** `typing.Optional[int]` — Deprecated: Use `model` field to configure max output tokens instead. The maximum number of tokens to generate, including reasoning step.
    
</dd>
</dl>

<dl>
<dd>

**max_reasoning_tokens:** `typing.Optional[int]` — Deprecated: Use `model` field to configure reasoning tokens instead. The maximum number of tokens to generate for reasoning step.
    
</dd>
</dl>

<dl>
<dd>

**enable_reasoner:** `typing.Optional[bool]` — Deprecated: Use `model` field to configure reasoning instead. Whether to enable internal extended thinking step for a reasoner model.
    
</dd>
</dl>

<dl>
<dd>

**reasoning:** `typing.Optional[bool]` — Deprecated: Use `model` field to configure reasoning instead. Whether to enable reasoning for this agent.
    
</dd>
</dl>

<dl>
<dd>

**from_template:** `typing.Optional[str]` — Deprecated: please use the 'create agents from a template' endpoint instead.
    
</dd>
</dl>

<dl>
<dd>

**template:** `typing.Optional[bool]` — Deprecated: No longer used.
    
</dd>
</dl>

<dl>
<dd>

**create_agent_request_project:** `typing.Optional[str]` — Deprecated: Project should now be passed via the X-Project header instead of in the request body. If using the SDK, this can be done via the x_project parameter.
    
</dd>
</dl>

<dl>
<dd>

**tool_exec_environment_variables:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — Deprecated: Use `secrets` field instead. Environment variables for tool execution.
    
</dd>
</dl>

<dl>
<dd>

**secrets:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — The environment variables for tool execution specific to this agent.
    
</dd>
</dl>

<dl>
<dd>

**memory_variables:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — Deprecated: Only relevant for creating agents from a template. Use the 'create agents from a template' endpoint instead.
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — Deprecated: No longer used. The id of the project the agent belongs to.
    
</dd>
</dl>

<dl>
<dd>

**template_id:** `typing.Optional[str]` — Deprecated: No longer used. The id of the template the agent belongs to.
    
</dd>
</dl>

<dl>
<dd>

**base_template_id:** `typing.Optional[str]` — Deprecated: No longer used. The base template id of the agent.
    
</dd>
</dl>

<dl>
<dd>

**identity_ids:** `typing.Optional[typing.List[str]]` — The ids of the identities associated with this agent.
    
</dd>
</dl>

<dl>
<dd>

**message_buffer_autoclear:** `typing.Optional[bool]` — If set to True, the agent will not remember previous messages (though the agent will still retain state via core memory blocks and archival/recall memory). Not recommended unless you have an advanced use case.
    
</dd>
</dl>

<dl>
<dd>

**enable_sleeptime:** `typing.Optional[bool]` — If set to True, memory management will move to a background agent thread.
    
</dd>
</dl>

<dl>
<dd>

**response_format:** `typing.Optional[CreateAgentRequestResponseFormat]` — Deprecated: Use `model_settings` field to configure response format instead. The response format for the agent.
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[str]` — The timezone of the agent (IANA format).
    
</dd>
</dl>

<dl>
<dd>

**max_files_open:** `typing.Optional[int]` — Maximum number of files that can be open at once for this agent. Setting this too high may exceed the context window, which will break the agent.
    
</dd>
</dl>

<dl>
<dd>

**per_file_view_window_char_limit:** `typing.Optional[int]` — The per-file view window character limit for this agent. Setting this too high may exceed the context window, which will break the agent.
    
</dd>
</dl>

<dl>
<dd>

**hidden:** `typing.Optional[bool]` — Deprecated: No longer used. If set to True, the agent will be hidden.
    
</dd>
</dl>

<dl>
<dd>

**parallel_tool_calls:** `typing.Optional[bool]` — Deprecated: Use `model_settings` to configure parallel tool calls instead. If set to True, enables parallel tool calling.
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">count_agents</a>(...) -> int</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the total number of agents with optional filtering.
Supports the same filters as list_agents for consistent querying.
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

client.agents.count_agents()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the agent
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` — List of tags to filter agents by
    
</dd>
</dl>

<dl>
<dd>

**match_all_tags:** `typing.Optional[bool]` — If True, only counts agents that match ALL given tags. Otherwise, counts agents that have ANY of the passed-in tags.
    
</dd>
</dl>

<dl>
<dd>

**query_text:** `typing.Optional[str]` — Search agents by name
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — Search agents by project ID - this will default to your default project on cloud
    
</dd>
</dl>

<dl>
<dd>

**template_id:** `typing.Optional[str]` — Search agents by template ID
    
</dd>
</dl>

<dl>
<dd>

**base_template_id:** `typing.Optional[str]` — Search agents by base template ID
    
</dd>
</dl>

<dl>
<dd>

**identity_id:** `typing.Optional[str]` — Search agents by identity ID
    
</dd>
</dl>

<dl>
<dd>

**identifier_keys:** `typing.Optional[typing.List[str]]` — Search agents by identifier keys
    
</dd>
</dl>

<dl>
<dd>

**last_stop_reason:** `typing.Optional[StopReasonType]` — Filter agents by their last stop reason.
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">export_agent</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Export the serialized JSON representation of an agent, formatted with indentation.
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

client.agents.export_agent(
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

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**max_steps:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**use_legacy_format:** `typing.Optional[bool]` — If True, exports using the legacy single-agent 'v1' format with inline tools/blocks. If False, exports using the new multi-entity 'v2' format, with separate agents, tools, blocks, files, etc.
    
</dd>
</dl>

<dl>
<dd>

**conversation_id:** `typing.Optional[str]` — Conversation ID to export. If provided, uses messages from this conversation instead of the agent's global message history.
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">import_agent</a>(...) -> ImportedAgentsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Import a serialized agent file and recreate the agent(s) in the system.
Returns the IDs of all imported agents.
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

client.agents.import_agent(
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

**override_embedding_model:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**override_existing_tools:** `typing.Optional[bool]` — If set to True, existing tools can get their source code overwritten by the uploaded tool definitions. Note that Letta core tools can never be updated externally.
    
</dd>
</dl>

<dl>
<dd>

**strip_messages:** `typing.Optional[bool]` — If set to True, strips all messages from the agent before importing.
    
</dd>
</dl>

<dl>
<dd>

**secrets:** `typing.Optional[str]` — Secrets as a JSON string to pass to the agent for tool execution.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — If provided, overrides the agent name with this value.
    
</dd>
</dl>

<dl>
<dd>

**embedding:** `typing.Optional[str]` — Embedding handle to override with.
    
</dd>
</dl>

<dl>
<dd>

**append_copy_suffix:** `typing.Optional[bool]` — If set to True, appends "_copy" to the end of the agent name.
    
</dd>
</dl>

<dl>
<dd>

**override_name:** `typing.Optional[str]` — If provided, overrides the agent name with this value. Use 'name' instead.
    
</dd>
</dl>

<dl>
<dd>

**override_embedding_handle:** `typing.Optional[str]` — Override import with specific embedding handle. Use 'embedding' instead.
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — The project ID to associate the uploaded agent with. This is now passed via headers.
    
</dd>
</dl>

<dl>
<dd>

**env_vars_json:** `typing.Optional[str]` — Environment variables as a JSON string to pass to the agent for tool execution. Use 'secrets' instead.
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">retrieve_agent_context_window</a>(...) -> ContextWindowOverview</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the context window of a specific agent.
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

client.agents.retrieve_agent_context_window(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**conversation_id:** `typing.Optional[str]` — Conversation ID to get context window for. If provided, uses messages from this conversation.
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">retrieve_agent</a>(...) -> AgentState</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the state of the agent.
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

client.agents.retrieve_agent(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**include_relationships:** `typing.Optional[typing.List[str]]` — Specify which relational fields (e.g., 'tools', 'sources', 'memory') to include in the response. If not provided, all relationships are loaded by default. Using this can optimize performance by reducing unnecessary joins.This is a legacy parameter, and no longer supported after 1.0.0 SDK versions.
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.Union[RetrieveAgentRequestIncludeItem, typing.Sequence[RetrieveAgentRequestIncludeItem]]]` — Specify which relational fields to include in the response. No relationships are included by default.
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">delete_agent</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an agent.
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

client.agents.delete_agent(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">modify_agent</a>(...) -> AgentState</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing agent.
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

client.agents.modify_agent(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the agent.
    
</dd>
</dl>

<dl>
<dd>

**tool_ids:** `typing.Optional[typing.List[str]]` — The ids of the tools used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**source_ids:** `typing.Optional[typing.List[str]]` — Deprecated: Use `folder_ids` field instead. The ids of the sources used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**folder_ids:** `typing.Optional[typing.List[str]]` — The ids of the folders used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**block_ids:** `typing.Optional[typing.List[str]]` — The ids of the blocks used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` — The tags associated with the agent.
    
</dd>
</dl>

<dl>
<dd>

**system:** `typing.Optional[str]` — The system prompt used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**tool_rules:** `typing.Optional[typing.List[UpdateAgentToolRulesItem]]` — The tool rules governing the agent.
    
</dd>
</dl>

<dl>
<dd>

**message_ids:** `typing.Optional[typing.List[str]]` — The ids of the messages in the agent's in-context memory.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of the agent.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — The metadata of the agent.
    
</dd>
</dl>

<dl>
<dd>

**tool_exec_environment_variables:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — Deprecated: use `secrets` field instead
    
</dd>
</dl>

<dl>
<dd>

**secrets:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — The environment variables for tool execution specific to this agent.
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — The id of the project the agent belongs to.
    
</dd>
</dl>

<dl>
<dd>

**template_id:** `typing.Optional[str]` — The id of the template the agent belongs to.
    
</dd>
</dl>

<dl>
<dd>

**base_template_id:** `typing.Optional[str]` — The base template id of the agent.
    
</dd>
</dl>

<dl>
<dd>

**identity_ids:** `typing.Optional[typing.List[str]]` — The ids of the identities associated with this agent.
    
</dd>
</dl>

<dl>
<dd>

**message_buffer_autoclear:** `typing.Optional[bool]` — If set to True, the agent will not remember previous messages (though the agent will still retain state via core memory blocks and archival/recall memory). Not recommended unless you have an advanced use case.
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` — The model handle used by the agent (format: provider/model-name).
    
</dd>
</dl>

<dl>
<dd>

**embedding:** `typing.Optional[str]` — The embedding model handle used by the agent (format: provider/model-name).
    
</dd>
</dl>

<dl>
<dd>

**model_settings:** `typing.Optional[UpdateAgentModelSettings]` — The model settings for the agent.
    
</dd>
</dl>

<dl>
<dd>

**compaction_settings:** `typing.Optional[CompactionSettingsInput]` — The compaction settings configuration used for compaction.
    
</dd>
</dl>

<dl>
<dd>

**context_window_limit:** `typing.Optional[int]` — The context window limit used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**reasoning:** `typing.Optional[bool]` — Deprecated: Use `model` field to configure reasoning instead. Whether to enable reasoning for this agent.
    
</dd>
</dl>

<dl>
<dd>

**llm_config:** `typing.Optional[LlmConfig]` — Deprecated: Use `model` field instead. The LLM configuration used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**embedding_config:** `typing.Optional[EmbeddingConfig]` — The embedding configuration used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**parallel_tool_calls:** `typing.Optional[bool]` — Deprecated: Use `model_settings` to configure parallel tool calls instead. If set to True, enables parallel tool calling.
    
</dd>
</dl>

<dl>
<dd>

**response_format:** `typing.Optional[UpdateAgentResponseFormat]` — Deprecated: Use `model_settings` field to configure response format instead. The response format for the agent.
    
</dd>
</dl>

<dl>
<dd>

**max_tokens:** `typing.Optional[int]` — Deprecated: Use `model` field to configure max output tokens instead. The maximum number of tokens to generate, including reasoning step.
    
</dd>
</dl>

<dl>
<dd>

**enable_sleeptime:** `typing.Optional[bool]` — If set to True, memory management will move to a background agent thread.
    
</dd>
</dl>

<dl>
<dd>

**last_run_completion:** `typing.Optional[datetime.datetime]` — The timestamp when the agent last completed a run.
    
</dd>
</dl>

<dl>
<dd>

**last_run_duration_ms:** `typing.Optional[int]` — The duration in milliseconds of the agent's last run.
    
</dd>
</dl>

<dl>
<dd>

**last_stop_reason:** `typing.Optional[StopReasonType]` — The stop reason from the agent's last run.
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[str]` — The timezone of the agent (IANA format).
    
</dd>
</dl>

<dl>
<dd>

**max_files_open:** `typing.Optional[int]` — Maximum number of files that can be open at once for this agent. Setting this too high may exceed the context window, which will break the agent.
    
</dd>
</dl>

<dl>
<dd>

**per_file_view_window_char_limit:** `typing.Optional[int]` — The per-file view window character limit for this agent. Setting this too high may exceed the context window, which will break the agent.
    
</dd>
</dl>

<dl>
<dd>

**hidden:** `typing.Optional[bool]` — If set to True, the agent will be hidden.
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">list_tools_for_agent</a>(...) -> typing.List[Tool]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get tools from an existing agent.
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

client.agents.list_tools_for_agent(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Tool ID cursor for pagination. Returns tools that come before this tool ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Tool ID cursor for pagination. Returns tools that come after this tool ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of tools to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListToolsForAgentRequestOrder]` — Sort order for tools by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[ListToolsForAgentRequestOrderBy]` — Field to sort by
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">attach_tool_to_agent</a>(...) -> typing.Optional[AgentState]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Attach a tool to an agent.
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

client.agents.attach_tool_to_agent(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
    tool_id="tool-123e4567-e89b-42d3-8456-426614174000",
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**tool_id:** `str` — The ID of the tool in the format 'tool-<uuid4>'
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">detach_tool_from_agent</a>(...) -> typing.Optional[AgentState]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Detach a tool from an agent.
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

client.agents.detach_tool_from_agent(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
    tool_id="tool-123e4567-e89b-42d3-8456-426614174000",
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**tool_id:** `str` — The ID of the tool in the format 'tool-<uuid4>'
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">modify_approval_for_tool</a>(...) -> typing.Optional[AgentState]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Modify the approval requirement for a tool attached to an agent.

Accepts requires_approval via request body (preferred) or query parameter (deprecated).
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
from fern import FernApi, ModifyApprovalRequest
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.agents.modify_approval_for_tool(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
    tool_name="tool_name",
    request=ModifyApprovalRequest(
        requires_approval=True,
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**tool_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**requires_approval:** `typing.Optional[bool]` — Whether the tool requires approval before execution
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Optional[ModifyApprovalRequest]` 
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">run_tool_for_agent</a>(...) -> ToolExecutionResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Trigger a tool by name on a specific agent, providing the necessary arguments.

This endpoint executes a tool that is attached to the agent, using the agent's
state and environment variables for execution context.
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

client.agents.run_tool_for_agent(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
    tool_name="tool_name",
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**tool_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `LettaSchemasMcpServerToolExecuteRequest` 
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">attach_source_to_agent</a>(...) -> AgentState</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Attach a source to an agent.
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

client.agents.attach_source_to_agent(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
    source_id="source-123e4567-e89b-42d3-8456-426614174000",
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**source_id:** `str` — The ID of the source in the format 'source-<uuid4>'
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">attach_folder_to_agent</a>(...) -> typing.Optional[AgentState]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Attach a folder to an agent.
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

client.agents.attach_folder_to_agent(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
    folder_id="source-123e4567-e89b-42d3-8456-426614174000",
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `str` — The ID of the source in the format 'source-<uuid4>'
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">detach_source_from_agent</a>(...) -> AgentState</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Detach a source from an agent.
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

client.agents.detach_source_from_agent(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
    source_id="source-123e4567-e89b-42d3-8456-426614174000",
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**source_id:** `str` — The ID of the source in the format 'source-<uuid4>'
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">detach_folder_from_agent</a>(...) -> typing.Optional[AgentState]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Detach a folder from an agent.
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

client.agents.detach_folder_from_agent(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
    folder_id="source-123e4567-e89b-42d3-8456-426614174000",
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `str` — The ID of the source in the format 'source-<uuid4>'
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">close_all_files_for_agent</a>(...) -> typing.List[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Closes all currently open files for a given agent.

This endpoint updates the file state for the agent so that no files are marked as open.
Typically used to reset the working memory view for the agent.
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

client.agents.close_all_files_for_agent(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">open_file_for_agent</a>(...) -> typing.List[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Opens a specific file for a given agent.

This endpoint marks a specific file as open in the agent's file state.
The file will be included in the agent's working memory view.
Returns a list of file names that were closed due to LRU eviction.
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

client.agents.open_file_for_agent(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
    file_id="file-123e4567-e89b-42d3-8456-426614174000",
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `str` — The ID of the file in the format 'file-<uuid4>'
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">close_file_for_agent</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Closes a specific file for a given agent.

This endpoint marks a specific file as closed in the agent's file state.
The file will be removed from the agent's working memory view.
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

client.agents.close_file_for_agent(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
    file_id="file-123e4567-e89b-42d3-8456-426614174000",
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `str` — The ID of the file in the format 'file-<uuid4>'
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">list_agent_sources</a>(...) -> typing.List[Source]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the sources associated with an agent.
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

client.agents.list_agent_sources(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Source ID cursor for pagination. Returns sources that come before this source ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Source ID cursor for pagination. Returns sources that come after this source ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of sources to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListAgentSourcesRequestOrder]` — Sort order for sources by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[ListAgentSourcesRequestOrderBy]` — Field to sort by
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">list_folders_for_agent</a>(...) -> typing.List[Source]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the folders associated with an agent.
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

client.agents.list_folders_for_agent(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Source ID cursor for pagination. Returns sources that come before this source ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Source ID cursor for pagination. Returns sources that come after this source ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of sources to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListFoldersForAgentRequestOrder]` — Sort order for sources by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[ListFoldersForAgentRequestOrderBy]` — Field to sort by
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">list_files_for_agent</a>(...) -> PaginatedAgentFiles</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the files attached to an agent with their open/closed status.
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

client.agents.list_files_for_agent(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — File ID cursor for pagination. Returns files that come before this file ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — File ID cursor for pagination. Returns files that come after this file ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of files to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListFilesForAgentRequestOrder]` — Sort order for files by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[ListFilesForAgentRequestOrderBy]` — Field to sort by
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Pagination cursor from previous response (deprecated, use before/after)
    
</dd>
</dl>

<dl>
<dd>

**is_open:** `typing.Optional[bool]` — Filter by open status (true for open files, false for closed files)
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">retrieve_agent_memory</a>(...) -> Memory</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the memory state of a specific agent.
This endpoint fetches the current memory state of the agent identified by the user ID and agent ID.
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

client.agents.retrieve_agent_memory(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">retrieve_core_memory_block</a>(...) -> BlockResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a core memory block from an agent.
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

client.agents.retrieve_core_memory_block(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
    block_label="block_label",
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**block_label:** `str` 
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">modify_core_memory_block</a>(...) -> BlockResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a core memory block of an agent.
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

client.agents.modify_core_memory_block(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
    block_label="block_label",
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**block_label:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `BlockUpdate` 
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">list_core_memory_blocks</a>(...) -> typing.List[BlockResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the core memory blocks of a specific agent.
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

client.agents.list_core_memory_blocks(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Block ID cursor for pagination. Returns blocks that come before this block ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Block ID cursor for pagination. Returns blocks that come after this block ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of blocks to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListCoreMemoryBlocksRequestOrder]` — Sort order for blocks by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[ListCoreMemoryBlocksRequestOrderBy]` — Field to sort by
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">attach_core_memory_block</a>(...) -> AgentState</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Attach a core memory block to an agent.
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

client.agents.attach_core_memory_block(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
    block_id="block-123e4567-e89b-42d3-8456-426614174000",
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**block_id:** `str` — The ID of the block in the format 'block-<uuid4>'
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">detach_core_memory_block</a>(...) -> AgentState</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Detach a core memory block from an agent.
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

client.agents.detach_core_memory_block(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
    block_id="block-123e4567-e89b-42d3-8456-426614174000",
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**block_id:** `str` — The ID of the block in the format 'block-<uuid4>'
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">attach_archive_to_agent</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Attach an archive to an agent.
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

client.agents.attach_archive_to_agent(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
    archive_id="archive_id",
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**archive_id:** `str` 
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">detach_archive_from_agent</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Detach an archive from an agent.
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

client.agents.detach_archive_from_agent(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
    archive_id="archive_id",
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**archive_id:** `str` 
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">attach_identity_to_agent</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Attach an identity to an agent.
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

client.agents.attach_identity_to_agent(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
    identity_id="identity_id",
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**identity_id:** `str` 
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">detach_identity_from_agent</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Detach an identity from an agent.
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

client.agents.detach_identity_from_agent(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
    identity_id="identity_id",
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**identity_id:** `str` 
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">list_passages</a>(...) -> typing.List[Passage]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the memories in an agent's archival memory store (paginated query).
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

client.agents.list_passages(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Unique ID of the memory to start the query range at.
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Unique ID of the memory to end the query range at.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — How many results to include in the response.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Search passages by text
    
</dd>
</dl>

<dl>
<dd>

**ascending:** `typing.Optional[bool]` — Whether to sort passages oldest to newest (True, default) or newest to oldest (False)
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">create_passage</a>(...) -> typing.List[Passage]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Insert a memory into an agent's archival memory store.
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

client.agents.create_passage(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
    text="text",
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**text:** `str` — Text to write to archival memory.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` — Optional list of tags to attach to the memory.
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[datetime.datetime]` — Optional timestamp for the memory (defaults to current UTC time).
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">search_archival_memory</a>(...) -> ArchivalMemorySearchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search archival memory using semantic (embedding-based) search with optional temporal filtering.

This endpoint allows manual triggering of archival memory searches, enabling users to query
an agent's archival memory store directly via the API. The search uses the same functionality
as the agent's archival_memory_search tool but is accessible for external API usage.
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

client.agents.search_archival_memory(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**query:** `str` — String to search for using semantic similarity
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` — Optional list of tags to filter search results
    
</dd>
</dl>

<dl>
<dd>

**tag_match_mode:** `typing.Optional[SearchArchivalMemoryRequestTagMatchMode]` — How to match tags - 'any' to match passages with any of the tags, 'all' to match only passages with all tags
    
</dd>
</dl>

<dl>
<dd>

**top_k:** `typing.Optional[int]` — Maximum number of results to return. Uses system default if not specified
    
</dd>
</dl>

<dl>
<dd>

**start_datetime:** `typing.Optional[datetime.datetime]` — Filter results to passages created after this datetime
    
</dd>
</dl>

<dl>
<dd>

**end_datetime:** `typing.Optional[datetime.datetime]` — Filter results to passages created before this datetime
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">delete_passage</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a memory from an agent's archival memory store.
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

client.agents.delete_passage(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
    memory_id="memory_id",
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**memory_id:** `str` 
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">list_messages</a>(...) -> typing.List[LettaMessageUnion]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve message history for an agent.
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

client.agents.list_messages(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Message ID cursor for pagination. Returns messages that come before this message ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Message ID cursor for pagination. Returns messages that come after this message ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of messages to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListMessagesRequestOrder]` — Sort order for messages by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[ListMessagesRequestOrderBy]` — Field to sort by
    
</dd>
</dl>

<dl>
<dd>

**group_id:** `typing.Optional[str]` — Group ID to filter messages by.
    
</dd>
</dl>

<dl>
<dd>

**conversation_id:** `typing.Optional[str]` — Conversation ID to filter messages by.
    
</dd>
</dl>

<dl>
<dd>

**use_assistant_message:** `typing.Optional[bool]` — Whether to use assistant messages
    
</dd>
</dl>

<dl>
<dd>

**assistant_message_tool_name:** `typing.Optional[str]` — The name of the designated message tool.
    
</dd>
</dl>

<dl>
<dd>

**assistant_message_tool_kwarg:** `typing.Optional[str]` — The name of the message argument.
    
</dd>
</dl>

<dl>
<dd>

**include_err:** `typing.Optional[bool]` — Whether to include error messages and error statuses. For debugging purposes only.
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">send_message</a>(...) -> LettaResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Process a user message and return the agent's response.
This endpoint accepts a message from a user and processes it through the agent.

The response format is controlled by the `streaming` field in the request body:
- If `streaming=false` (default): Returns a complete LettaResponse with all messages
- If `streaming=true`: Returns a Server-Sent Events (SSE) stream

Additional streaming options (only used when streaming=true):
- `stream_tokens`: Stream individual tokens instead of complete steps
- `include_pings`: Include keepalive pings to prevent connection timeouts
- `background`: Process the request in the background
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

client.agents.send_message(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**request:** `LettaStreamingRequest` 
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">modify_message</a>(...) -> ModifyMessageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the details of a message associated with an agent.
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
from fern.agents import ModifyMessageRequestBody_SystemMessage

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.agents.modify_message(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
    message_id="message-123e4567-e89b-42d3-8456-426614174000",
    request=ModifyMessageRequestBody_SystemMessage(
        content="content",
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**message_id:** `str` — The ID of the message in the format 'message-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**request:** `ModifyMessageRequestBody` 
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">create_agent_message_stream</a>(...) -> LettaStreamingResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Process a user message and return the agent's response.

Deprecated: Use the `POST /{agent_id}/messages` endpoint with `streaming=true` in the request body instead.

This endpoint accepts a message from a user and processes it through the agent.
It will stream the steps of the response always, and stream the tokens if 'stream_tokens' is set to True.
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

client.agents.create_agent_message_stream(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**request:** `LettaStreamingRequest` 
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">cancel_message</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel runs associated with an agent. If run_ids are passed in, cancel those in particular.

Note to cancel active runs associated with an agent, redis is required.
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

client.agents.cancel_message(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**run_ids:** `typing.Optional[typing.List[str]]` — Optional list of run IDs to cancel
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">search_messages</a>(...) -> typing.List[MessageSearchResult]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search messages across the entire organization with optional project and template filtering. Returns messages with FTS/vector ranks and total RRF score.

This is a cloud-only feature.
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

client.agents.search_messages()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `typing.Optional[str]` — Text query for full-text search
    
</dd>
</dl>

<dl>
<dd>

**search_mode:** `typing.Optional[MessageSearchRequestSearchMode]` — Search mode to use
    
</dd>
</dl>

<dl>
<dd>

**roles:** `typing.Optional[typing.List[MessageRole]]` — Filter messages by role
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `typing.Optional[str]` — Filter messages by agent ID
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — Filter messages by project ID
    
</dd>
</dl>

<dl>
<dd>

**template_id:** `typing.Optional[str]` — Filter messages by template ID
    
</dd>
</dl>

<dl>
<dd>

**conversation_id:** `typing.Optional[str]` — Filter messages by conversation ID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of results to return
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.datetime]` — Filter messages created after this date
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.datetime]` — Filter messages created on or before this date
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">create_agent_message_async</a>(...) -> Run</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Asynchronously process a user message and return a run object.
The actual processing happens in the background, and the status can be checked using the run ID.

This is "asynchronous" in the sense that it's a background run and explicitly must be fetched by the run ID.
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

client.agents.create_agent_message_async(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.Optional[typing.List[LettaAsyncRequestMessagesItem]]` — The messages to be sent to the agent.
    
</dd>
</dl>

<dl>
<dd>

**input:** `typing.Optional[LettaAsyncRequestInput]` — Syntactic sugar for a single user message. Equivalent to messages=[{'role': 'user', 'content': input}].
    
</dd>
</dl>

<dl>
<dd>

**max_steps:** `typing.Optional[int]` — Maximum number of steps the agent should take to process the request.
    
</dd>
</dl>

<dl>
<dd>

**use_assistant_message:** `typing.Optional[bool]` — Whether the server should parse specific tool call arguments (default `send_message`) as `AssistantMessage` objects. Still supported for legacy agent types, but deprecated for letta_v1_agent onward.
    
</dd>
</dl>

<dl>
<dd>

**assistant_message_tool_name:** `typing.Optional[str]` — The name of the designated message tool. Still supported for legacy agent types, but deprecated for letta_v1_agent onward.
    
</dd>
</dl>

<dl>
<dd>

**assistant_message_tool_kwarg:** `typing.Optional[str]` — The name of the message argument in the designated message tool. Still supported for legacy agent types, but deprecated for letta_v1_agent onward.
    
</dd>
</dl>

<dl>
<dd>

**include_return_message_types:** `typing.Optional[typing.List[MessageType]]` — Only return specified message types in the response. If `None` (default) returns all messages.
    
</dd>
</dl>

<dl>
<dd>

**enable_thinking:** `typing.Optional[str]` — If set to True, enables reasoning before responses or tool calls from the agent.
    
</dd>
</dl>

<dl>
<dd>

**client_tools:** `typing.Optional[typing.List[ClientToolSchema]]` — Client-side tools that the agent can call. When the agent calls a client-side tool, execution pauses and returns control to the client to execute the tool and provide the result via a ToolReturn.
    
</dd>
</dl>

<dl>
<dd>

**override_model:** `typing.Optional[str]` — Model handle to use for this request instead of the agent's default model. This allows sending a message to a different model without changing the agent's configuration.
    
</dd>
</dl>

<dl>
<dd>

**callback_url:** `typing.Optional[str]` — Optional callback URL to POST to when the job completes
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">reset_messages</a>(...) -> typing.Optional[AgentState]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Resets the messages for an agent
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

client.agents.reset_messages(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**add_default_initial_messages:** `typing.Optional[bool]` — If true, adds the default initial messages after resetting.
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">list_groups_for_agent</a>(...) -> typing.List[Group]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists the groups for an agent.
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

client.agents.list_groups_for_agent(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**manager_type:** `typing.Optional[str]` — Manager type to filter groups by
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Group ID cursor for pagination. Returns groups that come before this group ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Group ID cursor for pagination. Returns groups that come after this group ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of groups to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListGroupsForAgentRequestOrder]` — Sort order for groups by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[ListGroupsForAgentRequestOrderBy]` — Field to sort by
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">preview_model_request</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Inspect the raw LLM request payload without sending it.

This endpoint processes the message through the agent loop up until
the LLM request, then returns the raw request payload that would
be sent to the LLM provider. Useful for debugging and inspection.
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
from fern import FernApi, LettaRequest
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.agents.preview_model_request(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
    request=LettaRequest(),
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**request:** `PreviewModelRequestRequestBody` 
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">summarize_messages</a>(...) -> CompactionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Summarize an agent's conversation history.
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
from fern import FernApi, CompactionRequest
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.agents.summarize_messages(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
    request=CompactionRequest(),
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Optional[CompactionRequest]` 
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">searchdeployedagents</a>(...) -> AgentsSearchDeployedAgentsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search deployed agents
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

client.agents.searchdeployedagents()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search:** `typing.Optional[typing.List[AgentsSearchDeployedAgentsRequestSearchItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**combinator:** `typing.Optional[AgentsSearchDeployedAgentsRequestCombinator]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[AgentsSearchDeployedAgentsRequestSortBy]` 
    
</dd>
</dl>

<dl>
<dd>

**ascending:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">getagentvariables</a>(...) -> AgentsGetAgentVariablesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the variables associated with an agent
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

client.agents.getagentvariables(
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

**agent_id:** `str` 
    
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

## Conversations
<details><summary><code>client.conversations.<a href="src/fern/conversations/client.py">list_conversations</a>(...) -> typing.List[Conversation]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all conversations for an agent.
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

client.conversations.list_conversations(
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

**agent_id:** `str` — The agent ID to list conversations for
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of conversations to return
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Cursor for pagination (conversation ID)
    
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

<details><summary><code>client.conversations.<a href="src/fern/conversations/client.py">create_conversation</a>(...) -> Conversation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new conversation for an agent.
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

client.conversations.create_conversation(
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

**agent_id:** `str` — The agent ID to create a conversation for
    
</dd>
</dl>

<dl>
<dd>

**summary:** `typing.Optional[str]` — A summary of the conversation.
    
</dd>
</dl>

<dl>
<dd>

**isolated_block_labels:** `typing.Optional[typing.List[str]]` — List of block labels that should be isolated (conversation-specific) rather than shared across conversations. New blocks will be created as copies of the agent's blocks with these labels.
    
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

<details><summary><code>client.conversations.<a href="src/fern/conversations/client.py">retrieve_conversation</a>(...) -> Conversation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a specific conversation.
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

client.conversations.retrieve_conversation(
    conversation_id="conv-123e4567-e89b-42d3-8456-426614174000",
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

**conversation_id:** `str` — The ID of the conv in the format 'conv-<uuid4>'
    
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

<details><summary><code>client.conversations.<a href="src/fern/conversations/client.py">update_conversation</a>(...) -> Conversation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a conversation.
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

client.conversations.update_conversation(
    conversation_id="conv-123e4567-e89b-42d3-8456-426614174000",
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

**conversation_id:** `str` — The ID of the conv in the format 'conv-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**summary:** `typing.Optional[str]` — A summary of the conversation.
    
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

<details><summary><code>client.conversations.<a href="src/fern/conversations/client.py">list_conversation_messages</a>(...) -> typing.List[LettaMessageUnion]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all messages in a conversation.

Returns LettaMessage objects (UserMessage, AssistantMessage, etc.) for all
messages in the conversation, with support for cursor-based pagination.
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

client.conversations.list_conversation_messages(
    conversation_id="conv-123e4567-e89b-42d3-8456-426614174000",
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

**conversation_id:** `str` — The ID of the conv in the format 'conv-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Message ID cursor for pagination. Returns messages that come before this message ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Message ID cursor for pagination. Returns messages that come after this message ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of messages to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListConversationMessagesRequestOrder]` — Sort order for messages by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[ListConversationMessagesRequestOrderBy]` — Field to sort by
    
</dd>
</dl>

<dl>
<dd>

**group_id:** `typing.Optional[str]` — Group ID to filter messages by.
    
</dd>
</dl>

<dl>
<dd>

**include_err:** `typing.Optional[bool]` — Whether to include error messages and error statuses. For debugging purposes only.
    
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

<details><summary><code>client.conversations.<a href="src/fern/conversations/client.py">send_conversation_message</a>(...) -> LettaStreamingResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send a message to a conversation and get a streaming response.

This endpoint sends a message to an existing conversation and streams
the agent's response back.
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

client.conversations.send_conversation_message(
    conversation_id="conv-123e4567-e89b-42d3-8456-426614174000",
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

**conversation_id:** `str` — The ID of the conv in the format 'conv-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**request:** `LettaStreamingRequest` 
    
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

<details><summary><code>client.conversations.<a href="src/fern/conversations/client.py">retrieve_conversation_stream</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Resume the stream for the most recent active run in a conversation.

This endpoint allows you to reconnect to an active background stream
for a conversation, enabling recovery from network interruptions.
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

client.conversations.retrieve_conversation_stream(
    conversation_id="conv-123e4567-e89b-42d3-8456-426614174000",
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

**conversation_id:** `str` — The ID of the conv in the format 'conv-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**request:** `RetrieveStreamRequest` 
    
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

<details><summary><code>client.conversations.<a href="src/fern/conversations/client.py">cancel_conversation</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel runs associated with a conversation.

Note: To cancel active runs, Redis is required.
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

client.conversations.cancel_conversation(
    conversation_id="conv-123e4567-e89b-42d3-8456-426614174000",
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

**conversation_id:** `str` — The ID of the conv in the format 'conv-<uuid4>'
    
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

<details><summary><code>client.conversations.<a href="src/fern/conversations/client.py">compact_conversation</a>(...) -> CompactionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compact (summarize) a conversation's message history.

This endpoint summarizes the in-context messages for a specific conversation,
reducing the message count while preserving important context.
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
from fern import FernApi, CompactionRequest
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.conversations.compact_conversation(
    conversation_id="conv-123e4567-e89b-42d3-8456-426614174000",
    request=CompactionRequest(),
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

**conversation_id:** `str` — The ID of the conv in the format 'conv-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Optional[CompactionRequest]` 
    
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

## Chat
<details><summary><code>client.chat.<a href="src/fern/chat/client.py">create_chat_completion</a>(...) -> ChatCompletion</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a chat completion using a Letta agent (OpenAI-compatible).

This endpoint provides full OpenAI API compatibility. The agent is selected based on:
- The 'model' parameter in the request (should contain an agent ID in format 'agent-...')

When streaming is enabled (stream=true), the response will be Server-Sent Events
with ChatCompletionChunk objects.
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
from fern.chat import ChatCompletionRequestMessagesItem_Developer

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.chat.create_chat_completion(
    model="model",
    messages=[
        ChatCompletionRequestMessagesItem_Developer(
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

**model:** `str` — ID of the model to use
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.List[ChatCompletionRequestMessagesItem]` — Messages comprising the conversation so far
    
</dd>
</dl>

<dl>
<dd>

**temperature:** `typing.Optional[float]` — Sampling temperature
    
</dd>
</dl>

<dl>
<dd>

**top_p:** `typing.Optional[float]` — Nucleus sampling parameter
    
</dd>
</dl>

<dl>
<dd>

**n:** `typing.Optional[int]` — Number of chat completion choices to generate
    
</dd>
</dl>

<dl>
<dd>

**stream:** `typing.Optional[bool]` — Whether to stream back partial progress
    
</dd>
</dl>

<dl>
<dd>

**stop:** `typing.Optional[ChatCompletionRequestStop]` — Sequences where the API will stop generating
    
</dd>
</dl>

<dl>
<dd>

**max_tokens:** `typing.Optional[int]` — Maximum number of tokens to generate
    
</dd>
</dl>

<dl>
<dd>

**presence_penalty:** `typing.Optional[float]` — Presence penalty
    
</dd>
</dl>

<dl>
<dd>

**frequency_penalty:** `typing.Optional[float]` — Frequency penalty
    
</dd>
</dl>

<dl>
<dd>

**user:** `typing.Optional[str]` — A unique identifier representing your end-user
    
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

## Groups
<details><summary><code>client.groups.<a href="src/fern/groups/client.py">list_groups</a>(...) -> typing.List[Group]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch all multi-agent groups matching query.
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

client.groups.list_groups()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**manager_type:** `typing.Optional[ManagerType]` — Search groups by manager type
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Group ID cursor for pagination. Returns groups that come before this group ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Group ID cursor for pagination. Returns groups that come after this group ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of groups to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListGroupsRequestOrder]` — Sort order for groups by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[ListGroupsRequestOrderBy]` — Field to sort by
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — Search groups by project id
    
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

<details><summary><code>client.groups.<a href="src/fern/groups/client.py">create_group</a>(...) -> Group</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new multi-agent group with the specified configuration.
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

client.groups.create_group(
    agent_ids=[
        "agent_ids"
    ],
    description="description",
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

**agent_ids:** `typing.List[str]` — 
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` — 
    
</dd>
</dl>

<dl>
<dd>

**project:** `typing.Optional[str]` — The project slug to associate with the group (cloud only).
    
</dd>
</dl>

<dl>
<dd>

**manager_config:** `typing.Optional[GroupCreateManagerConfig]` — 
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — The associated project id.
    
</dd>
</dl>

<dl>
<dd>

**shared_block_ids:** `typing.Optional[typing.List[str]]` — 
    
</dd>
</dl>

<dl>
<dd>

**hidden:** `typing.Optional[bool]` — If set to True, the group will be hidden.
    
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

<details><summary><code>client.groups.<a href="src/fern/groups/client.py">count_groups</a>() -> int</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the count of all groups associated with a given user.
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

client.groups.count_groups()

```
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

<details><summary><code>client.groups.<a href="src/fern/groups/client.py">retrieve_group</a>(...) -> Group</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the group by id.
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

client.groups.retrieve_group(
    group_id="group-123e4567-e89b-42d3-8456-426614174000",
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

**group_id:** `str` — The ID of the group in the format 'group-<uuid4>'
    
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

<details><summary><code>client.groups.<a href="src/fern/groups/client.py">delete_group</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a multi-agent group.
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

client.groups.delete_group(
    group_id="group-123e4567-e89b-42d3-8456-426614174000",
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

**group_id:** `str` — The ID of the group in the format 'group-<uuid4>'
    
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

<details><summary><code>client.groups.<a href="src/fern/groups/client.py">modify_group</a>(...) -> Group</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new multi-agent group with the specified configuration.
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

client.groups.modify_group(
    group_id="group-123e4567-e89b-42d3-8456-426614174000",
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

**group_id:** `str` — The ID of the group in the format 'group-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**project:** `typing.Optional[str]` — The project slug to associate with the group (cloud only).
    
</dd>
</dl>

<dl>
<dd>

**agent_ids:** `typing.Optional[typing.List[str]]` — 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — 
    
</dd>
</dl>

<dl>
<dd>

**manager_config:** `typing.Optional[GroupUpdateManagerConfig]` — 
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — The associated project id.
    
</dd>
</dl>

<dl>
<dd>

**shared_block_ids:** `typing.Optional[typing.List[str]]` — 
    
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

<details><summary><code>client.groups.<a href="src/fern/groups/client.py">list_group_messages</a>(...) -> typing.List[LettaMessageUnion]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve message history for an agent.
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

client.groups.list_group_messages(
    group_id="group-123e4567-e89b-42d3-8456-426614174000",
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

**group_id:** `str` — The ID of the group in the format 'group-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Message ID cursor for pagination. Returns messages that come before this message ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Message ID cursor for pagination. Returns messages that come after this message ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of messages to retrieve
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListGroupMessagesRequestOrder]` — Sort order for messages by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[ListGroupMessagesRequestOrderBy]` — Field to sort by
    
</dd>
</dl>

<dl>
<dd>

**use_assistant_message:** `typing.Optional[bool]` — Whether to use assistant messages
    
</dd>
</dl>

<dl>
<dd>

**assistant_message_tool_name:** `typing.Optional[str]` — The name of the designated message tool.
    
</dd>
</dl>

<dl>
<dd>

**assistant_message_tool_kwarg:** `typing.Optional[str]` — The name of the message argument.
    
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

<details><summary><code>client.groups.<a href="src/fern/groups/client.py">send_group_message</a>(...) -> LettaResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Process a user message and return the group's response.
This endpoint accepts a message from a user and processes it through through agents in the group based on the specified pattern
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

client.groups.send_group_message(
    group_id="group-123e4567-e89b-42d3-8456-426614174000",
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

**group_id:** `str` — The ID of the group in the format 'group-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**request:** `LettaRequest` 
    
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

<details><summary><code>client.groups.<a href="src/fern/groups/client.py">send_group_message_streaming</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Process a user message and return the group's responses.
This endpoint accepts a message from a user and processes it through agents in the group based on the specified pattern.
It will stream the steps of the response always, and stream the tokens if 'stream_tokens' is set to True.
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

client.groups.send_group_message_streaming(
    group_id="group-123e4567-e89b-42d3-8456-426614174000",
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

**group_id:** `str` — The ID of the group in the format 'group-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**request:** `LettaStreamingRequest` 
    
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

<details><summary><code>client.groups.<a href="src/fern/groups/client.py">modify_group_message</a>(...) -> ModifyGroupMessageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the details of a message associated with an agent.
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
from fern.groups import ModifyGroupMessageRequestBody_SystemMessage

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.groups.modify_group_message(
    group_id="group-123e4567-e89b-42d3-8456-426614174000",
    message_id="message-123e4567-e89b-42d3-8456-426614174000",
    request=ModifyGroupMessageRequestBody_SystemMessage(
        content="content",
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

**group_id:** `str` — The ID of the group in the format 'group-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**message_id:** `str` — The ID of the message in the format 'message-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**request:** `ModifyGroupMessageRequestBody` 
    
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

<details><summary><code>client.groups.<a href="src/fern/groups/client.py">reset_group_messages</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the group messages for all agents that are part of the multi-agent group.
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

client.groups.reset_group_messages(
    group_id="group-123e4567-e89b-42d3-8456-426614174000",
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

**group_id:** `str` — The ID of the group in the format 'group-<uuid4>'
    
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

<details><summary><code>client.groups.<a href="src/fern/groups/client.py">attach_block_to_group</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Attach a block to a group.
This will add the block to the group and all agents within the group.
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

client.groups.attach_block_to_group(
    group_id="group-123e4567-e89b-42d3-8456-426614174000",
    block_id="block_id",
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

**group_id:** `str` — The ID of the group in the format 'group-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**block_id:** `str` 
    
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

<details><summary><code>client.groups.<a href="src/fern/groups/client.py">detach_block_from_group</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Detach a block from a group.
This will remove the block from the group and all agents within the group.
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

client.groups.detach_block_from_group(
    group_id="group-123e4567-e89b-42d3-8456-426614174000",
    block_id="block_id",
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

**group_id:** `str` — The ID of the group in the format 'group-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**block_id:** `str` 
    
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

## Identities
<details><summary><code>client.identities.<a href="src/fern/identities/client.py">list_identities</a>(...) -> typing.List[Identity]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of all identities in the database
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

client.identities.list_identities()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — [DEPRECATED: Use X-Project-Id header instead] Filter identities by project ID
    
</dd>
</dl>

<dl>
<dd>

**identifier_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**identity_type:** `typing.Optional[IdentityType]` 
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Identity ID cursor for pagination. Returns identities that come before this identity ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Identity ID cursor for pagination. Returns identities that come after this identity ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of identities to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListIdentitiesRequestOrder]` — Sort order for identities by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[ListIdentitiesRequestOrderBy]` — Field to sort by
    
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

<details><summary><code>client.identities.<a href="src/fern/identities/client.py">create_identity</a>(...) -> Identity</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, IdentityType
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.identities.create_identity(
    identifier_key="identifier_key",
    name="name",
    identity_type=IdentityType.ORG,
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

**identifier_key:** `str` — External, user-generated identifier key of the identity.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the identity.
    
</dd>
</dl>

<dl>
<dd>

**identity_type:** `IdentityType` — The type of the identity.
    
</dd>
</dl>

<dl>
<dd>

**project:** `typing.Optional[str]` — The project slug to associate with the identity (cloud only).
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — The project id of the identity, if applicable.
    
</dd>
</dl>

<dl>
<dd>

**agent_ids:** `typing.Optional[typing.List[str]]` — The agent ids that are associated with the identity.
    
</dd>
</dl>

<dl>
<dd>

**block_ids:** `typing.Optional[typing.List[str]]` — The IDs of the blocks associated with the identity.
    
</dd>
</dl>

<dl>
<dd>

**properties:** `typing.Optional[typing.List[IdentityProperty]]` — List of properties associated with the identity.
    
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

<details><summary><code>client.identities.<a href="src/fern/identities/client.py">upsert_identity</a>(...) -> Identity</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, IdentityType
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.identities.upsert_identity(
    identifier_key="identifier_key",
    name="name",
    identity_type=IdentityType.ORG,
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

**identifier_key:** `str` — External, user-generated identifier key of the identity.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the identity.
    
</dd>
</dl>

<dl>
<dd>

**identity_type:** `IdentityType` — The type of the identity.
    
</dd>
</dl>

<dl>
<dd>

**project:** `typing.Optional[str]` — The project slug to associate with the identity (cloud only).
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — The project id of the identity, if applicable.
    
</dd>
</dl>

<dl>
<dd>

**agent_ids:** `typing.Optional[typing.List[str]]` — The agent ids that are associated with the identity.
    
</dd>
</dl>

<dl>
<dd>

**block_ids:** `typing.Optional[typing.List[str]]` — The IDs of the blocks associated with the identity.
    
</dd>
</dl>

<dl>
<dd>

**properties:** `typing.Optional[typing.List[IdentityProperty]]` — List of properties associated with the identity.
    
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

<details><summary><code>client.identities.<a href="src/fern/identities/client.py">count_identities</a>() -> int</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get count of all identities for a user
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

client.identities.count_identities()

```
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

<details><summary><code>client.identities.<a href="src/fern/identities/client.py">retrieve_identity</a>(...) -> Identity</code></summary>
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

client.identities.retrieve_identity(
    identity_id="identity-123e4567-e89b-42d3-8456-426614174000",
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

**identity_id:** `str` — The ID of the identity in the format 'identity-<uuid4>'
    
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

<details><summary><code>client.identities.<a href="src/fern/identities/client.py">delete_identity</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an identity by its identifier key
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

client.identities.delete_identity(
    identity_id="identity-123e4567-e89b-42d3-8456-426614174000",
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

**identity_id:** `str` — The ID of the identity in the format 'identity-<uuid4>'
    
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

<details><summary><code>client.identities.<a href="src/fern/identities/client.py">update_identity</a>(...) -> Identity</code></summary>
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

client.identities.update_identity(
    identity_id="identity-123e4567-e89b-42d3-8456-426614174000",
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

**identity_id:** `str` — The ID of the identity in the format 'identity-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**identifier_key:** `typing.Optional[str]` — External, user-generated identifier key of the identity.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the identity.
    
</dd>
</dl>

<dl>
<dd>

**identity_type:** `typing.Optional[IdentityType]` — The type of the identity.
    
</dd>
</dl>

<dl>
<dd>

**agent_ids:** `typing.Optional[typing.List[str]]` — The agent ids that are associated with the identity.
    
</dd>
</dl>

<dl>
<dd>

**block_ids:** `typing.Optional[typing.List[str]]` — The IDs of the blocks associated with the identity.
    
</dd>
</dl>

<dl>
<dd>

**properties:** `typing.Optional[typing.List[IdentityProperty]]` — List of properties associated with the identity.
    
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

<details><summary><code>client.identities.<a href="src/fern/identities/client.py">upsert_properties_for_identity</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, IdentityProperty, IdentityPropertyType
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.identities.upsert_properties_for_identity(
    identity_id="identity-123e4567-e89b-42d3-8456-426614174000",
    request=[
        IdentityProperty(
            key="key",
            value="value",
            type=IdentityPropertyType.STRING,
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

**identity_id:** `str` — The ID of the identity in the format 'identity-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[IdentityProperty]` 
    
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

<details><summary><code>client.identities.<a href="src/fern/identities/client.py">list_agents_for_identity</a>(...) -> typing.List[AgentState]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all agents associated with the specified identity.
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

client.identities.list_agents_for_identity(
    identity_id="identity-123e4567-e89b-42d3-8456-426614174000",
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

**identity_id:** `str` — The ID of the identity in the format 'identity-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Agent ID cursor for pagination. Returns agents that come before this agent ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Agent ID cursor for pagination. Returns agents that come after this agent ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of agents to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListAgentsForIdentityRequestOrder]` — Sort order for agents by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[ListAgentsForIdentityRequestOrderBy]` — Field to sort by
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.Union[ListAgentsForIdentityRequestIncludeItem, typing.Sequence[ListAgentsForIdentityRequestIncludeItem]]]` — Specify which relational fields to include in the response. No relationships are included by default.
    
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

<details><summary><code>client.identities.<a href="src/fern/identities/client.py">list_blocks_for_identity</a>(...) -> typing.List[BlockResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all blocks associated with the specified identity.
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

client.identities.list_blocks_for_identity(
    identity_id="identity-123e4567-e89b-42d3-8456-426614174000",
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

**identity_id:** `str` — The ID of the identity in the format 'identity-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Block ID cursor for pagination. Returns blocks that come before this block ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Block ID cursor for pagination. Returns blocks that come after this block ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of blocks to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListBlocksForIdentityRequestOrder]` — Sort order for blocks by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[ListBlocksForIdentityRequestOrderBy]` — Field to sort by
    
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

## InternalAgents
<details><summary><code>client.internal_agents.<a href="src/fern/internal_agents/client.py">count_internal_agents</a>(...) -> int</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the total number of agents for a user, with option to exclude hidden agents.
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

client.internal_agents.count_internal_agents()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**exclude_hidden:** `typing.Optional[bool]` — If True, excludes hidden agents from the count. If False, includes all agents.
    
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

<details><summary><code>client.internal_agents.<a href="src/fern/internal_agents/client.py">modify_internal_core_memory_block</a>(...) -> Block</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a core memory block of an agent.
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

client.internal_agents.modify_internal_core_memory_block(
    agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
    block_label="block_label",
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

**agent_id:** `str` — The ID of the agent in the format 'agent-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**block_label:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `BlockUpdate` 
    
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

## InternalBlocks
<details><summary><code>client.internal_blocks.<a href="src/fern/internal_blocks/client.py">list_internal_blocks</a>(...) -> typing.List[Block]</code></summary>
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

client.internal_blocks.list_internal_blocks()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**label:** `typing.Optional[str]` — Label to include (alphanumeric, hyphens, underscores, forward slashes)
    
</dd>
</dl>

<dl>
<dd>

**templates_only:** `typing.Optional[bool]` — Whether to include only templates
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name filter (alphanumeric, spaces, hyphens, underscores)
    
</dd>
</dl>

<dl>
<dd>

**identity_id:** `typing.Optional[str]` — The ID of the identity in the format 'identity-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**identifier_keys:** `typing.Optional[typing.List[str]]` — Search agents by identifier keys
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — Search blocks by project id
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of blocks to return
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Block ID cursor for pagination. Returns blocks that come before this block ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Block ID cursor for pagination. Returns blocks that come after this block ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListInternalBlocksRequestOrder]` — Sort order for blocks by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[ListInternalBlocksRequestOrderBy]` — Field to sort by
    
</dd>
</dl>

<dl>
<dd>

**label_search:** `typing.Optional[str]` — Search blocks by label. If provided, returns blocks whose label matches the search query. This is a full-text search on block labels.
    
</dd>
</dl>

<dl>
<dd>

**description_search:** `typing.Optional[str]` — Search blocks by description. If provided, returns blocks whose description matches the search query. This is a full-text search on block descriptions.
    
</dd>
</dl>

<dl>
<dd>

**value_search:** `typing.Optional[str]` — Search blocks by value. If provided, returns blocks whose value matches the search query. This is a full-text search on block values.
    
</dd>
</dl>

<dl>
<dd>

**connected_to_agents_count_gt:** `typing.Optional[int]` — Filter blocks by the number of connected agents. If provided, returns blocks that have more than this number of connected agents.
    
</dd>
</dl>

<dl>
<dd>

**connected_to_agents_count_lt:** `typing.Optional[int]` — Filter blocks by the number of connected agents. If provided, returns blocks that have less than this number of connected agents.
    
</dd>
</dl>

<dl>
<dd>

**connected_to_agents_count_eq:** `typing.Optional[typing.List[int]]` — Filter blocks by the exact number of connected agents. If provided, returns blocks that have exactly this number of connected agents.
    
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

<details><summary><code>client.internal_blocks.<a href="src/fern/internal_blocks/client.py">create_internal_block</a>(...) -> Block</code></summary>
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

client.internal_blocks.create_internal_block(
    value="value",
    label="label",
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

**request:** `CreateBlock` 
    
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

<details><summary><code>client.internal_blocks.<a href="src/fern/internal_blocks/client.py">delete_internal_block</a>(...) -> typing.Any</code></summary>
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

client.internal_blocks.delete_internal_block(
    block_id="block-123e4567-e89b-42d3-8456-426614174000",
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

**block_id:** `str` — The ID of the block in the format 'block-<uuid4>'
    
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

<details><summary><code>client.internal_blocks.<a href="src/fern/internal_blocks/client.py">list_agents_for_internal_block</a>(...) -> typing.List[AgentState]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves all agents associated with the specified block.
Raises a 404 if the block does not exist.
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

client.internal_blocks.list_agents_for_internal_block(
    block_id="block-123e4567-e89b-42d3-8456-426614174000",
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

**block_id:** `str` — The ID of the block in the format 'block-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Agent ID cursor for pagination. Returns agents that come before this agent ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Agent ID cursor for pagination. Returns agents that come after this agent ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of agents to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListAgentsForInternalBlockRequestOrder]` — Sort order for agents by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[ListAgentsForInternalBlockRequestOrderBy]` — Field to sort by
    
</dd>
</dl>

<dl>
<dd>

**include_relationships:** `typing.Optional[typing.List[str]]` — Specify which relational fields (e.g., 'tools', 'sources', 'memory') to include in the response. If not provided, all relationships are loaded by default. Using this can optimize performance by reducing unnecessary joins.This is a legacy parameter, and no longer supported after 1.0.0 SDK versions.
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Specify which relational fields to include in the response. No relationships are included by default.
    
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

## InternalRuns
<details><summary><code>client.internal_runs.<a href="src/fern/internal_runs/client.py">list_internal_runs</a>(...) -> typing.List[Run]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all runs.
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

client.internal_runs.list_internal_runs()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `typing.Optional[str]` — Filter by a specific run ID.
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `typing.Optional[str]` — The unique identifier of the agent associated with the run.
    
</dd>
</dl>

<dl>
<dd>

**agent_ids:** `typing.Optional[typing.List[str]]` — The unique identifiers of the agents associated with the run. Deprecated in favor of agent_id field.
    
</dd>
</dl>

<dl>
<dd>

**statuses:** `typing.Optional[typing.List[str]]` — Filter runs by status. Can specify multiple statuses.
    
</dd>
</dl>

<dl>
<dd>

**background:** `typing.Optional[bool]` — If True, filters for runs that were created in background mode.
    
</dd>
</dl>

<dl>
<dd>

**stop_reason:** `typing.Optional[StopReasonType]` — Filter runs by stop reason.
    
</dd>
</dl>

<dl>
<dd>

**template_family:** `typing.Optional[str]` — Filter runs by template family (base_template_id).
    
</dd>
</dl>

<dl>
<dd>

**step_count:** `typing.Optional[int]` — Filter runs by step count. Must be provided with step_count_operator.
    
</dd>
</dl>

<dl>
<dd>

**step_count_operator:** `typing.Optional[ComparisonOperator]` — Operator for step_count filter: 'eq' for equals, 'gte' for greater than or equal, 'lte' for less than or equal.
    
</dd>
</dl>

<dl>
<dd>

**tools_used:** `typing.Optional[typing.List[str]]` — Filter runs that used any of the specified tools.
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Run ID cursor for pagination. Returns runs that come before this run ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Run ID cursor for pagination. Returns runs that come after this run ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of runs to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListInternalRunsRequestOrder]` — Sort order for runs by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[ListInternalRunsRequestOrderBy]` — Field to sort by
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[bool]` — Filter for active runs.
    
</dd>
</dl>

<dl>
<dd>

**ascending:** `typing.Optional[bool]` — Whether to sort agents oldest to newest (True) or newest to oldest (False, default). Deprecated in favor of order field.
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — Filter runs by project ID.
    
</dd>
</dl>

<dl>
<dd>

**conversation_id:** `typing.Optional[str]` — Filter runs by conversation ID.
    
</dd>
</dl>

<dl>
<dd>

**duration_percentile:** `typing.Optional[int]` — Filter runs by duration percentile (1-100). Returns runs slower than this percentile.
    
</dd>
</dl>

<dl>
<dd>

**duration_value:** `typing.Optional[int]` — Duration value in nanoseconds for filtering. Must be used with duration_operator.
    
</dd>
</dl>

<dl>
<dd>

**duration_operator:** `typing.Optional[ListInternalRunsRequestDurationOperator]` — Comparison operator for duration filter: 'gt' (greater than), 'lt' (less than), 'eq' (equals).
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.datetime]` — Filter runs created on or after this date (ISO 8601 format).
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.datetime]` — Filter runs created on or before this date (ISO 8601 format).
    
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

## InternalTemplates
<details><summary><code>client.internal_templates.<a href="src/fern/internal_templates/client.py">create_internal_template_group</a>(...) -> Group</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new multi-agent group with the specified configuration.
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

client.internal_templates.create_internal_template_group(
    agent_ids=[
        "agent_ids"
    ],
    description="description",
    base_template_id="base_template_id",
    template_id="template_id",
    deployment_id="deployment_id",
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

**agent_ids:** `typing.List[str]` — 
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` — 
    
</dd>
</dl>

<dl>
<dd>

**base_template_id:** `str` — The id of the base template.
    
</dd>
</dl>

<dl>
<dd>

**template_id:** `str` — The id of the template.
    
</dd>
</dl>

<dl>
<dd>

**deployment_id:** `str` — The id of the deployment.
    
</dd>
</dl>

<dl>
<dd>

**manager_config:** `typing.Optional[InternalTemplateGroupCreateManagerConfig]` — 
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — The associated project id.
    
</dd>
</dl>

<dl>
<dd>

**shared_block_ids:** `typing.Optional[typing.List[str]]` — 
    
</dd>
</dl>

<dl>
<dd>

**hidden:** `typing.Optional[bool]` — If set to True, the group will be hidden.
    
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

<details><summary><code>client.internal_templates.<a href="src/fern/internal_templates/client.py">create_internal_template_agent</a>(...) -> AgentState</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new agent with template-related fields.
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

client.internal_templates.create_internal_template_agent(
    template_id="template_id",
    base_template_id="base_template_id",
    deployment_id="deployment_id",
    entity_id="entity_id",
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

**template_id:** `str` — The id of the template.
    
</dd>
</dl>

<dl>
<dd>

**base_template_id:** `str` — The id of the base template.
    
</dd>
</dl>

<dl>
<dd>

**deployment_id:** `str` — The id of the deployment.
    
</dd>
</dl>

<dl>
<dd>

**entity_id:** `str` — The id of the entity within the template.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the agent.
    
</dd>
</dl>

<dl>
<dd>

**memory_blocks:** `typing.Optional[typing.List[CreateBlock]]` — The blocks to create in the agent's in-context memory.
    
</dd>
</dl>

<dl>
<dd>

**tools:** `typing.Optional[typing.List[str]]` — The tools used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**tool_ids:** `typing.Optional[typing.List[str]]` — The ids of the tools used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**source_ids:** `typing.Optional[typing.List[str]]` — Deprecated: Use `folder_ids` field instead. The ids of the sources used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**folder_ids:** `typing.Optional[typing.List[str]]` — The ids of the folders used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**block_ids:** `typing.Optional[typing.List[str]]` — The ids of the blocks used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**tool_rules:** `typing.Optional[typing.List[InternalTemplateAgentCreateToolRulesItem]]` — The tool rules governing the agent.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` — The tags associated with the agent.
    
</dd>
</dl>

<dl>
<dd>

**system:** `typing.Optional[str]` — The system prompt used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**agent_type:** `typing.Optional[AgentType]` — The type of agent.
    
</dd>
</dl>

<dl>
<dd>

**initial_message_sequence:** `typing.Optional[typing.List[MessageCreate]]` — The initial set of messages to put in the agent's in-context memory.
    
</dd>
</dl>

<dl>
<dd>

**include_base_tools:** `typing.Optional[bool]` — If true, attaches the Letta core tools (e.g. core_memory related functions).
    
</dd>
</dl>

<dl>
<dd>

**include_multi_agent_tools:** `typing.Optional[bool]` — If true, attaches the Letta multi-agent tools (e.g. sending a message to another agent).
    
</dd>
</dl>

<dl>
<dd>

**include_base_tool_rules:** `typing.Optional[bool]` — If true, attaches the Letta base tool rules (e.g. deny all tools not explicitly allowed).
    
</dd>
</dl>

<dl>
<dd>

**include_default_source:** `typing.Optional[bool]` — If true, automatically creates and attaches a default data source for this agent.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of the agent.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — The metadata of the agent.
    
</dd>
</dl>

<dl>
<dd>

**llm_config:** `typing.Optional[LlmConfig]` — Deprecated: Use `model` field instead. The LLM configuration used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**embedding_config:** `typing.Optional[EmbeddingConfig]` — Deprecated: Use `embedding` field instead. The embedding configuration used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` — The model handle for the agent to use (format: provider/model-name).
    
</dd>
</dl>

<dl>
<dd>

**embedding:** `typing.Optional[str]` — The embedding model handle used by the agent (format: provider/model-name).
    
</dd>
</dl>

<dl>
<dd>

**model_settings:** `typing.Optional[InternalTemplateAgentCreateModelSettings]` — The model settings for the agent.
    
</dd>
</dl>

<dl>
<dd>

**compaction_settings:** `typing.Optional[CompactionSettingsInput]` — The compaction settings configuration used for compaction.
    
</dd>
</dl>

<dl>
<dd>

**context_window_limit:** `typing.Optional[int]` — The context window limit used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**embedding_chunk_size:** `typing.Optional[int]` — Deprecated: No longer used. The embedding chunk size used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**max_tokens:** `typing.Optional[int]` — Deprecated: Use `model` field to configure max output tokens instead. The maximum number of tokens to generate, including reasoning step.
    
</dd>
</dl>

<dl>
<dd>

**max_reasoning_tokens:** `typing.Optional[int]` — Deprecated: Use `model` field to configure reasoning tokens instead. The maximum number of tokens to generate for reasoning step.
    
</dd>
</dl>

<dl>
<dd>

**enable_reasoner:** `typing.Optional[bool]` — Deprecated: Use `model` field to configure reasoning instead. Whether to enable internal extended thinking step for a reasoner model.
    
</dd>
</dl>

<dl>
<dd>

**reasoning:** `typing.Optional[bool]` — Deprecated: Use `model` field to configure reasoning instead. Whether to enable reasoning for this agent.
    
</dd>
</dl>

<dl>
<dd>

**from_template:** `typing.Optional[str]` — Deprecated: please use the 'create agents from a template' endpoint instead.
    
</dd>
</dl>

<dl>
<dd>

**template:** `typing.Optional[bool]` — Deprecated: No longer used.
    
</dd>
</dl>

<dl>
<dd>

**project:** `typing.Optional[str]` — Deprecated: Project should now be passed via the X-Project header instead of in the request body. If using the SDK, this can be done via the x_project parameter.
    
</dd>
</dl>

<dl>
<dd>

**tool_exec_environment_variables:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — Deprecated: Use `secrets` field instead. Environment variables for tool execution.
    
</dd>
</dl>

<dl>
<dd>

**secrets:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — The environment variables for tool execution specific to this agent.
    
</dd>
</dl>

<dl>
<dd>

**memory_variables:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — Deprecated: Only relevant for creating agents from a template. Use the 'create agents from a template' endpoint instead.
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — Deprecated: No longer used. The id of the project the agent belongs to.
    
</dd>
</dl>

<dl>
<dd>

**identity_ids:** `typing.Optional[typing.List[str]]` — The ids of the identities associated with this agent.
    
</dd>
</dl>

<dl>
<dd>

**message_buffer_autoclear:** `typing.Optional[bool]` — If set to True, the agent will not remember previous messages (though the agent will still retain state via core memory blocks and archival/recall memory). Not recommended unless you have an advanced use case.
    
</dd>
</dl>

<dl>
<dd>

**enable_sleeptime:** `typing.Optional[bool]` — If set to True, memory management will move to a background agent thread.
    
</dd>
</dl>

<dl>
<dd>

**response_format:** `typing.Optional[InternalTemplateAgentCreateResponseFormat]` — Deprecated: Use `model_settings` field to configure response format instead. The response format for the agent.
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[str]` — The timezone of the agent (IANA format).
    
</dd>
</dl>

<dl>
<dd>

**max_files_open:** `typing.Optional[int]` — Maximum number of files that can be open at once for this agent. Setting this too high may exceed the context window, which will break the agent.
    
</dd>
</dl>

<dl>
<dd>

**per_file_view_window_char_limit:** `typing.Optional[int]` — The per-file view window character limit for this agent. Setting this too high may exceed the context window, which will break the agent.
    
</dd>
</dl>

<dl>
<dd>

**hidden:** `typing.Optional[bool]` — Deprecated: No longer used. If set to True, the agent will be hidden.
    
</dd>
</dl>

<dl>
<dd>

**parallel_tool_calls:** `typing.Optional[bool]` — Deprecated: Use `model_settings` to configure parallel tool calls instead. If set to True, enables parallel tool calling.
    
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

<details><summary><code>client.internal_templates.<a href="src/fern/internal_templates/client.py">create_internal_template_block</a>(...) -> Block</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new block with template-related fields.
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

client.internal_templates.create_internal_template_block(
    value="value",
    template_id="template_id",
    base_template_id="base_template_id",
    deployment_id="deployment_id",
    entity_id="entity_id",
    label="label",
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

**request:** `InternalTemplateBlockCreate` 
    
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

<details><summary><code>client.internal_templates.<a href="src/fern/internal_templates/client.py">create_internal_template_blocks_batch</a>(...) -> typing.List[Block]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create multiple blocks with template-related fields.
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
from fern import FernApi, InternalTemplateBlockCreate
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.internal_templates.create_internal_template_blocks_batch(
    request=[
        InternalTemplateBlockCreate(
            value="value",
            template_id="template_id",
            base_template_id="base_template_id",
            deployment_id="deployment_id",
            entity_id="entity_id",
            label="label",
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

**request:** `typing.List[InternalTemplateBlockCreate]` 
    
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

<details><summary><code>client.internal_templates.<a href="src/fern/internal_templates/client.py">list_deployment_entities</a>(...) -> ListDeploymentEntitiesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all entities (blocks, agents, groups) with the specified deployment_id.
Optionally filter by entity types.
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

client.internal_templates.list_deployment_entities(
    deployment_id="deployment_id",
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

**deployment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**entity_types:** `typing.Optional[typing.List[str]]` — Filter by entity types (block, agent, group)
    
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

<details><summary><code>client.internal_templates.<a href="src/fern/internal_templates/client.py">delete_deployment</a>(...) -> DeleteDeploymentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete all entities (blocks, agents, groups) with the specified deployment_id.
Deletion order: blocks -> agents -> groups to maintain referential integrity.
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

client.internal_templates.delete_deployment(
    deployment_id="deployment_id",
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

**deployment_id:** `str` 
    
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

## Models
<details><summary><code>client.models.<a href="src/fern/models/client.py">list_models</a>(...) -> typing.List[Model]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List available LLM models using the asynchronous implementation for improved performance.

Returns Model format which extends LLMConfig with additional metadata fields.
Legacy LLMConfig fields are marked as deprecated but still available for backward compatibility.
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

client.models.list_models()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**provider_category:** `typing.Optional[typing.List[ProviderCategory]]` 
    
</dd>
</dl>

<dl>
<dd>

**provider_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**provider_type:** `typing.Optional[ProviderType]` 
    
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

<details><summary><code>client.models.<a href="src/fern/models/client.py">list_embedding_models</a>() -> typing.List[EmbeddingModel]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List available embedding models using the asynchronous implementation for improved performance.

Returns EmbeddingModel format which extends EmbeddingConfig with additional metadata fields.
Legacy EmbeddingConfig fields are marked as deprecated but still available for backward compatibility.
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

client.models.list_embedding_models()

```
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

<details><summary><code>client.models.<a href="src/fern/models/client.py">listembeddingmodels</a>()</code></summary>
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

client.models.listembeddingmodels()

```
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

## McpServers
<details><summary><code>client.mcp_servers.<a href="src/fern/mcp_servers/client.py">mcp_list_mcp_servers</a>() -> typing.List[McpListMcpServersResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of all configured MCP servers
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

client.mcp_servers.mcp_list_mcp_servers()

```
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

<details><summary><code>client.mcp_servers.<a href="src/fern/mcp_servers/client.py">mcp_create_mcp_server</a>(...) -> McpCreateMcpServerResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a new MCP server to the Letta MCP server config
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
from fern.mcp_servers import CreateMcpServerRequestConfig_Sse

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.mcp_servers.mcp_create_mcp_server(
    server_name="server_name",
    config=CreateMcpServerRequestConfig_Sse(
        server_url="server_url",
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

**server_name:** `str` — The name of the MCP server
    
</dd>
</dl>

<dl>
<dd>

**config:** `CreateMcpServerRequestConfig` — The MCP server configuration (Stdio, SSE, or Streamable HTTP)
    
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

<details><summary><code>client.mcp_servers.<a href="src/fern/mcp_servers/client.py">mcp_retrieve_mcp_server</a>(...) -> McpRetrieveMcpServerResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific MCP server
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

client.mcp_servers.mcp_retrieve_mcp_server(
    mcp_server_id="mcp_server_id",
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

**mcp_server_id:** `str` 
    
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

<details><summary><code>client.mcp_servers.<a href="src/fern/mcp_servers/client.py">mcp_delete_mcp_server</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an MCP server by its ID
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

client.mcp_servers.mcp_delete_mcp_server(
    mcp_server_id="mcp_server_id",
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

**mcp_server_id:** `str` 
    
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

<details><summary><code>client.mcp_servers.<a href="src/fern/mcp_servers/client.py">mcp_update_mcp_server</a>(...) -> McpUpdateMcpServerResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing MCP server configuration
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
from fern.mcp_servers import UpdateMcpServerRequestConfig_Sse

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.mcp_servers.mcp_update_mcp_server(
    mcp_server_id="mcp_server_id",
    config=UpdateMcpServerRequestConfig_Sse(),
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

**mcp_server_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**config:** `UpdateMcpServerRequestConfig` — The MCP server configuration updates (Stdio, SSE, or Streamable HTTP)
    
</dd>
</dl>

<dl>
<dd>

**server_name:** `typing.Optional[str]` — The name of the MCP server
    
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

<details><summary><code>client.mcp_servers.<a href="src/fern/mcp_servers/client.py">mcp_list_tools_for_mcp_server</a>(...) -> typing.List[Tool]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of all tools for a specific MCP server
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

client.mcp_servers.mcp_list_tools_for_mcp_server(
    mcp_server_id="mcp_server_id",
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

**mcp_server_id:** `str` 
    
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

<details><summary><code>client.mcp_servers.<a href="src/fern/mcp_servers/client.py">mcp_retrieve_mcp_tool</a>(...) -> Tool</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific MCP tool by its ID
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

client.mcp_servers.mcp_retrieve_mcp_tool(
    mcp_server_id="mcp_server_id",
    tool_id="tool_id",
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

**mcp_server_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**tool_id:** `str` 
    
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

<details><summary><code>client.mcp_servers.<a href="src/fern/mcp_servers/client.py">mcp_run_tool</a>(...) -> ToolExecutionResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Execute a specific MCP tool

The request body should contain the tool arguments in the ToolExecuteRequest format.
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

client.mcp_servers.mcp_run_tool(
    mcp_server_id="mcp_server_id",
    tool_id="tool_id",
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

**mcp_server_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**tool_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `LettaSchemasMcpServerToolExecuteRequest` 
    
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

<details><summary><code>client.mcp_servers.<a href="src/fern/mcp_servers/client.py">mcp_refresh_mcp_server_tools</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Refresh tools for an MCP server by:
1. Fetching current tools from the MCP server
2. Deleting tools that no longer exist on the server
3. Updating schemas for existing tools
4. Adding new tools from the server

Returns a summary of changes made.
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

client.mcp_servers.mcp_refresh_mcp_server_tools(
    mcp_server_id="mcp_server_id",
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

**mcp_server_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `typing.Optional[str]` 
    
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

<details><summary><code>client.mcp_servers.<a href="src/fern/mcp_servers/client.py">mcp_connect_mcp_server</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Connect to an MCP server with support for OAuth via SSE.
Returns a stream of events handling authorization state and exchange if OAuth is required.
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

client.mcp_servers.mcp_connect_mcp_server(
    mcp_server_id="mcp_server_id",
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

**mcp_server_id:** `str` 
    
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

## Blocks
<details><summary><code>client.blocks.<a href="src/fern/blocks/client.py">list_blocks</a>(...) -> typing.List[BlockResponse]</code></summary>
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

client.blocks.list_blocks()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**label:** `typing.Optional[str]` — Label to include (alphanumeric, hyphens, underscores, forward slashes)
    
</dd>
</dl>

<dl>
<dd>

**templates_only:** `typing.Optional[bool]` — Whether to include only templates
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name filter (alphanumeric, spaces, hyphens, underscores)
    
</dd>
</dl>

<dl>
<dd>

**identity_id:** `typing.Optional[str]` — The ID of the identity in the format 'identity-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**identifier_keys:** `typing.Optional[typing.List[str]]` — Search agents by identifier keys
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — Search blocks by project id
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` — List of tags to filter blocks by
    
</dd>
</dl>

<dl>
<dd>

**match_all_tags:** `typing.Optional[bool]` — If True, only returns blocks that match ALL given tags. Otherwise, return blocks that have ANY of the passed-in tags.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of blocks to return
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Block ID cursor for pagination. Returns blocks that come before this block ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Block ID cursor for pagination. Returns blocks that come after this block ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListBlocksRequestOrder]` — Sort order for blocks by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[ListBlocksRequestOrderBy]` — Field to sort by
    
</dd>
</dl>

<dl>
<dd>

**label_search:** `typing.Optional[str]` — Search blocks by label. If provided, returns blocks whose label matches the search query. This is a full-text search on block labels.
    
</dd>
</dl>

<dl>
<dd>

**description_search:** `typing.Optional[str]` — Search blocks by description. If provided, returns blocks whose description matches the search query. This is a full-text search on block descriptions.
    
</dd>
</dl>

<dl>
<dd>

**value_search:** `typing.Optional[str]` — Search blocks by value. If provided, returns blocks whose value matches the search query. This is a full-text search on block values.
    
</dd>
</dl>

<dl>
<dd>

**connected_to_agents_count_gt:** `typing.Optional[int]` — Filter blocks by the number of connected agents. If provided, returns blocks that have more than this number of connected agents.
    
</dd>
</dl>

<dl>
<dd>

**connected_to_agents_count_lt:** `typing.Optional[int]` — Filter blocks by the number of connected agents. If provided, returns blocks that have less than this number of connected agents.
    
</dd>
</dl>

<dl>
<dd>

**connected_to_agents_count_eq:** `typing.Optional[typing.List[int]]` — Filter blocks by the exact number of connected agents. If provided, returns blocks that have exactly this number of connected agents.
    
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

<details><summary><code>client.blocks.<a href="src/fern/blocks/client.py">create_block</a>(...) -> BlockResponse</code></summary>
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

client.blocks.create_block(
    value="value",
    label="label",
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

**request:** `CreateBlock` 
    
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

<details><summary><code>client.blocks.<a href="src/fern/blocks/client.py">count_blocks</a>(...) -> int</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Count all blocks with optional filtering.
Supports the same filters as list_blocks for consistent querying.
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

client.blocks.count_blocks()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**label:** `typing.Optional[str]` — Label to include (alphanumeric, hyphens, underscores, forward slashes)
    
</dd>
</dl>

<dl>
<dd>

**templates_only:** `typing.Optional[bool]` — Whether to include only templates
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name filter (alphanumeric, spaces, hyphens, underscores)
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` — List of tags to filter blocks by
    
</dd>
</dl>

<dl>
<dd>

**match_all_tags:** `typing.Optional[bool]` — If True, only counts blocks that match ALL given tags. Otherwise, counts blocks that have ANY of the passed-in tags.
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — Search blocks by project id
    
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

<details><summary><code>client.blocks.<a href="src/fern/blocks/client.py">retrieve_block</a>(...) -> BlockResponse</code></summary>
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

client.blocks.retrieve_block(
    block_id="block-123e4567-e89b-42d3-8456-426614174000",
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

**block_id:** `str` — The ID of the block in the format 'block-<uuid4>'
    
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

<details><summary><code>client.blocks.<a href="src/fern/blocks/client.py">delete_block</a>(...) -> typing.Any</code></summary>
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

client.blocks.delete_block(
    block_id="block-123e4567-e89b-42d3-8456-426614174000",
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

**block_id:** `str` — The ID of the block in the format 'block-<uuid4>'
    
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

<details><summary><code>client.blocks.<a href="src/fern/blocks/client.py">modify_block</a>(...) -> BlockResponse</code></summary>
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

client.blocks.modify_block(
    block_id="block-123e4567-e89b-42d3-8456-426614174000",
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

**block_id:** `str` — The ID of the block in the format 'block-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**request:** `BlockUpdate` 
    
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

<details><summary><code>client.blocks.<a href="src/fern/blocks/client.py">list_agents_for_block</a>(...) -> typing.List[AgentState]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves all agents associated with the specified block.
Raises a 404 if the block does not exist.
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

client.blocks.list_agents_for_block(
    block_id="block-123e4567-e89b-42d3-8456-426614174000",
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

**block_id:** `str` — The ID of the block in the format 'block-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Agent ID cursor for pagination. Returns agents that come before this agent ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Agent ID cursor for pagination. Returns agents that come after this agent ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of agents to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListAgentsForBlockRequestOrder]` — Sort order for agents by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[ListAgentsForBlockRequestOrderBy]` — Field to sort by
    
</dd>
</dl>

<dl>
<dd>

**include_relationships:** `typing.Optional[typing.List[str]]` — Specify which relational fields (e.g., 'tools', 'sources', 'memory') to include in the response. If not provided, all relationships are loaded by default. Using this can optimize performance by reducing unnecessary joins.This is a legacy parameter, and no longer supported after 1.0.0 SDK versions.
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.Union[ListAgentsForBlockRequestIncludeItem, typing.Sequence[ListAgentsForBlockRequestIncludeItem]]]` — Specify which relational fields to include in the response. No relationships are included by default.
    
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

<details><summary><code>client.blocks.<a href="src/fern/blocks/client.py">attach_identity_to_block</a>(...) -> BlockResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Attach an identity to a block.
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

client.blocks.attach_identity_to_block(
    block_id="block-123e4567-e89b-42d3-8456-426614174000",
    identity_id="identity_id",
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

**block_id:** `str` — The ID of the block in the format 'block-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**identity_id:** `str` 
    
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

<details><summary><code>client.blocks.<a href="src/fern/blocks/client.py">detach_identity_from_block</a>(...) -> BlockResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Detach an identity from a block.
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

client.blocks.detach_identity_from_block(
    block_id="block-123e4567-e89b-42d3-8456-426614174000",
    identity_id="identity_id",
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

**block_id:** `str` — The ID of the block in the format 'block-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**identity_id:** `str` 
    
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

## Jobs
<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">list_jobs</a>(...) -> typing.List[Job]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all jobs.
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

client.jobs.list_jobs()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_id:** `typing.Optional[str]` — Deprecated: Use `folder_id` parameter instead. Only list jobs associated with the source.
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Job ID cursor for pagination. Returns jobs that come before this job ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Job ID cursor for pagination. Returns jobs that come after this job ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of jobs to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListJobsRequestOrder]` — Sort order for jobs by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[ListJobsRequestOrderBy]` — Field to sort by
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[bool]` — Filter for active jobs.
    
</dd>
</dl>

<dl>
<dd>

**ascending:** `typing.Optional[bool]` — Whether to sort jobs oldest to newest (True, default) or newest to oldest (False). Deprecated in favor of order field.
    
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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">list_active_jobs</a>(...) -> typing.List[Job]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all active jobs.
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

client.jobs.list_active_jobs()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_id:** `typing.Optional[str]` — Deprecated: Use `folder_id` parameter instead. Only list jobs associated with the source.
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Cursor for pagination
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Cursor for pagination
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit for pagination
    
</dd>
</dl>

<dl>
<dd>

**ascending:** `typing.Optional[bool]` — Whether to sort jobs oldest to newest (True, default) or newest to oldest (False)
    
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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">retrieve_job</a>(...) -> Job</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the status of a job.
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

client.jobs.retrieve_job(
    job_id="job-123e4567-e89b-42d3-8456-426614174000",
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

**job_id:** `str` — The ID of the job in the format 'job-<uuid4>'
    
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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">delete_job</a>(...) -> Job</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a job by its job_id.
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

client.jobs.delete_job(
    job_id="job-123e4567-e89b-42d3-8456-426614174000",
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

**job_id:** `str` — The ID of the job in the format 'job-<uuid4>'
    
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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">cancel_job</a>(...) -> Job</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel a job by its job_id.

This endpoint marks a job as cancelled, which will cause any associated
agent execution to terminate as soon as possible.
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

client.jobs.cancel_job(
    job_id="job-123e4567-e89b-42d3-8456-426614174000",
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

**job_id:** `str` — The ID of the job in the format 'job-<uuid4>'
    
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
<details><summary><code>client.health.<a href="src/fern/health/client.py">check_health</a>() -> Health</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Async health check endpoint.
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

client.health.check_health()

```
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

## Providers
<details><summary><code>client.providers.<a href="src/fern/providers/client.py">list_providers</a>(...) -> typing.List[Provider]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of all custom providers.
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

client.providers.list_providers()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**before:** `typing.Optional[str]` — Provider ID cursor for pagination. Returns providers that come before this provider ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Provider ID cursor for pagination. Returns providers that come after this provider ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of providers to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListProvidersRequestOrder]` — Sort order for providers by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[ListProvidersRequestOrderBy]` — Field to sort by
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Filter providers by name
    
</dd>
</dl>

<dl>
<dd>

**provider_type:** `typing.Optional[ProviderType]` — Filter providers by type
    
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

<details><summary><code>client.providers.<a href="src/fern/providers/client.py">create_provider</a>(...) -> Provider</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new custom provider.
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
from fern import FernApi, ProviderType
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.providers.create_provider(
    name="name",
    provider_type=ProviderType.ANTHROPIC,
    api_key="api_key",
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

**name:** `str` — The name of the provider.
    
</dd>
</dl>

<dl>
<dd>

**provider_type:** `ProviderType` — The type of the provider.
    
</dd>
</dl>

<dl>
<dd>

**api_key:** `str` — API key or secret key used for requests to the provider.
    
</dd>
</dl>

<dl>
<dd>

**access_key:** `typing.Optional[str]` — Access key used for requests to the provider.
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` — Region used for requests to the provider.
    
</dd>
</dl>

<dl>
<dd>

**base_url:** `typing.Optional[str]` — Base URL used for requests to the provider.
    
</dd>
</dl>

<dl>
<dd>

**api_version:** `typing.Optional[str]` — API version used for requests to the provider.
    
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

<details><summary><code>client.providers.<a href="src/fern/providers/client.py">retrieve_provider</a>(...) -> Provider</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a provider by ID.
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

client.providers.retrieve_provider(
    provider_id="provider-123e4567-e89b-42d3-8456-426614174000",
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

**provider_id:** `str` — The ID of the provider in the format 'provider-<uuid4>'
    
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

<details><summary><code>client.providers.<a href="src/fern/providers/client.py">delete_provider</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an existing custom provider.
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

client.providers.delete_provider(
    provider_id="provider-123e4567-e89b-42d3-8456-426614174000",
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

**provider_id:** `str` — The ID of the provider in the format 'provider-<uuid4>'
    
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

<details><summary><code>client.providers.<a href="src/fern/providers/client.py">modify_provider</a>(...) -> Provider</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing custom provider.
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

client.providers.modify_provider(
    provider_id="provider-123e4567-e89b-42d3-8456-426614174000",
    api_key="api_key",
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

**provider_id:** `str` — The ID of the provider in the format 'provider-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**api_key:** `str` — API key or secret key used for requests to the provider.
    
</dd>
</dl>

<dl>
<dd>

**access_key:** `typing.Optional[str]` — Access key used for requests to the provider.
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` — Region used for requests to the provider.
    
</dd>
</dl>

<dl>
<dd>

**base_url:** `typing.Optional[str]` — Base URL used for requests to the provider.
    
</dd>
</dl>

<dl>
<dd>

**api_version:** `typing.Optional[str]` — API version used for requests to the provider.
    
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

<details><summary><code>client.providers.<a href="src/fern/providers/client.py">check_provider</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Verify the API key and additional parameters for a provider.
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
from fern import FernApi, ProviderType
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.providers.check_provider(
    provider_type=ProviderType.ANTHROPIC,
    api_key="api_key",
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

**provider_type:** `ProviderType` — The type of the provider.
    
</dd>
</dl>

<dl>
<dd>

**api_key:** `str` — API key or secret key used for requests to the provider.
    
</dd>
</dl>

<dl>
<dd>

**access_key:** `typing.Optional[str]` — Access key used for requests to the provider.
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` — Region used for requests to the provider.
    
</dd>
</dl>

<dl>
<dd>

**base_url:** `typing.Optional[str]` — Base URL used for requests to the provider.
    
</dd>
</dl>

<dl>
<dd>

**api_version:** `typing.Optional[str]` — API version used for requests to the provider.
    
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

<details><summary><code>client.providers.<a href="src/fern/providers/client.py">check_existing_provider</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Verify the API key and additional parameters for an existing provider.
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

client.providers.check_existing_provider(
    provider_id="provider-123e4567-e89b-42d3-8456-426614174000",
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

**provider_id:** `str` — The ID of the provider in the format 'provider-<uuid4>'
    
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

<details><summary><code>client.providers.<a href="src/fern/providers/client.py">refresh_provider_models</a>(...) -> Provider</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Refresh models for a BYOK provider by querying the provider's API.
Adds new models and removes ones no longer available.
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

client.providers.refresh_provider_models(
    provider_id="provider-123e4567-e89b-42d3-8456-426614174000",
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

**provider_id:** `str` — The ID of the provider in the format 'provider-<uuid4>'
    
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
<details><summary><code>client.runs.<a href="src/fern/runs/client.py">list_runs</a>(...) -> typing.List[Run]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all runs.
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

client.runs.list_runs()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `typing.Optional[str]` — The unique identifier of the agent associated with the run.
    
</dd>
</dl>

<dl>
<dd>

**agent_ids:** `typing.Optional[typing.List[str]]` — The unique identifiers of the agents associated with the run. Deprecated in favor of agent_id field.
    
</dd>
</dl>

<dl>
<dd>

**statuses:** `typing.Optional[typing.List[str]]` — Filter runs by status. Can specify multiple statuses.
    
</dd>
</dl>

<dl>
<dd>

**background:** `typing.Optional[bool]` — If True, filters for runs that were created in background mode.
    
</dd>
</dl>

<dl>
<dd>

**stop_reason:** `typing.Optional[StopReasonType]` — Filter runs by stop reason.
    
</dd>
</dl>

<dl>
<dd>

**conversation_id:** `typing.Optional[str]` — Filter runs by conversation ID.
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Run ID cursor for pagination. Returns runs that come before this run ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Run ID cursor for pagination. Returns runs that come after this run ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of runs to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListRunsRequestOrder]` — Sort order for runs by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[ListRunsRequestOrderBy]` — Field to sort by
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[bool]` — Filter for active runs.
    
</dd>
</dl>

<dl>
<dd>

**ascending:** `typing.Optional[bool]` — Whether to sort agents oldest to newest (True) or newest to oldest (False, default). Deprecated in favor of order field.
    
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

<details><summary><code>client.runs.<a href="src/fern/runs/client.py">list_active_runs</a>(...) -> typing.List[Run]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all active runs.
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

client.runs.list_active_runs()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `typing.Optional[str]` — The unique identifier of the agent associated with the run.
    
</dd>
</dl>

<dl>
<dd>

**background:** `typing.Optional[bool]` — If True, filters for runs that were created in background mode.
    
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

<details><summary><code>client.runs.<a href="src/fern/runs/client.py">retrieve_run</a>(...) -> Run</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the status of a run.
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

client.runs.retrieve_run(
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

**run_id:** `str` 
    
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

<details><summary><code>client.runs.<a href="src/fern/runs/client.py">delete_run</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a run by its run_id.
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

client.runs.delete_run(
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

**run_id:** `str` 
    
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

<details><summary><code>client.runs.<a href="src/fern/runs/client.py">list_messages_for_run</a>(...) -> typing.List[LettaMessageUnion]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get response messages associated with a run.
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

client.runs.list_messages_for_run(
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

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Message ID cursor for pagination. Returns messages that come before this message ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Message ID cursor for pagination. Returns messages that come after this message ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of messages to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListMessagesForRunRequestOrder]` — Sort order for messages by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[ListMessagesForRunRequestOrderBy]` — Field to sort by
    
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

<details><summary><code>client.runs.<a href="src/fern/runs/client.py">retrieve_usage_for_run</a>(...) -> UsageStatistics</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get usage statistics for a run.
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

client.runs.retrieve_usage_for_run(
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

**run_id:** `str` 
    
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

<details><summary><code>client.runs.<a href="src/fern/runs/client.py">retrieve_metrics_for_run</a>(...) -> RunMetrics</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get run metrics by run ID.
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

client.runs.retrieve_metrics_for_run(
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

**run_id:** `str` 
    
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

<details><summary><code>client.runs.<a href="src/fern/runs/client.py">list_steps_for_run</a>(...) -> typing.List[Step]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get steps associated with a run with filtering options.
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

client.runs.list_steps_for_run(
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

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Cursor for pagination
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Cursor for pagination
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of messages to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListStepsForRunRequestOrder]` — Sort order for steps by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[ListStepsForRunRequestOrderBy]` — Field to sort by
    
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

<details><summary><code>client.runs.<a href="src/fern/runs/client.py">retrieve_trace_for_run</a>(...) -> typing.List[typing.Dict[str, typing.Any]]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve OTEL trace spans for a run.

Returns a filtered set of spans relevant for observability:
- agent_step: Individual agent reasoning steps
- tool executions: Tool call spans
- Root span: The top-level request span
- time_to_first_token: TTFT measurement span

Requires ClickHouse to be configured for trace storage.
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

client.runs.retrieve_trace_for_run(
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

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of spans to return
    
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

<details><summary><code>client.runs.<a href="src/fern/runs/client.py">retrieve_stream_for_run</a>(...) -> typing.Any</code></summary>
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

client.runs.retrieve_stream_for_run(
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

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `RetrieveStreamRequest` 
    
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

## Steps
<details><summary><code>client.steps.<a href="src/fern/steps/client.py">list_steps</a>(...) -> typing.List[Step]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List steps with optional pagination and date filters.
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

client.steps.list_steps()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**before:** `typing.Optional[str]` — Return steps before this step ID
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Return steps after this step ID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of steps to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListStepsRequestOrder]` — Sort order for steps by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[ListStepsRequestOrderBy]` — Field to sort by
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — Return steps after this ISO datetime (e.g. "2025-01-29T15:01:19-08:00")
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Return steps before this ISO datetime (e.g. "2025-01-29T15:01:19-08:00")
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` — Filter by the name of the model used for the step
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `typing.Optional[str]` — Filter by the ID of the agent that performed the step
    
</dd>
</dl>

<dl>
<dd>

**trace_ids:** `typing.Optional[typing.List[str]]` — Filter by trace ids returned by the server
    
</dd>
</dl>

<dl>
<dd>

**feedback:** `typing.Optional[ListStepsRequestFeedback]` — Filter by feedback
    
</dd>
</dl>

<dl>
<dd>

**has_feedback:** `typing.Optional[bool]` — Filter by whether steps have feedback (true) or not (false)
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` — Filter by tags
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — Filter by the project ID that is associated with the step (cloud only).
    
</dd>
</dl>

<dl>
<dd>

**project:** `typing.Optional[str]` — Filter by project slug to associate with the group (cloud only).
    
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

<details><summary><code>client.steps.<a href="src/fern/steps/client.py">retrieve_step</a>(...) -> Step</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a step by ID.
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

client.steps.retrieve_step(
    step_id="step-123e4567-e89b-42d3-8456-426614174000",
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

**step_id:** `str` — The ID of the step in the format 'step-<uuid4>'
    
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

<details><summary><code>client.steps.<a href="src/fern/steps/client.py">retrieve_metrics_for_step</a>(...) -> StepMetrics</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get step metrics by step ID.
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

client.steps.retrieve_metrics_for_step(
    step_id="step-123e4567-e89b-42d3-8456-426614174000",
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

**step_id:** `str` — The ID of the step in the format 'step-<uuid4>'
    
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

<details><summary><code>client.steps.<a href="src/fern/steps/client.py">retrieve_trace_for_step</a>(...) -> typing.Optional[ProviderTrace]</code></summary>
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

client.steps.retrieve_trace_for_step(
    step_id="step-123e4567-e89b-42d3-8456-426614174000",
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

**step_id:** `str` — The ID of the step in the format 'step-<uuid4>'
    
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

<details><summary><code>client.steps.<a href="src/fern/steps/client.py">modify_feedback_for_step</a>(...) -> Step</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Modify feedback for a given step.
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

client.steps.modify_feedback_for_step(
    step_id="step-123e4567-e89b-42d3-8456-426614174000",
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

**step_id:** `str` — The ID of the step in the format 'step-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**feedback:** `typing.Optional[FeedbackType]` — Whether this feedback is positive or negative
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` — Feedback tags to add to the step
    
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

<details><summary><code>client.steps.<a href="src/fern/steps/client.py">list_messages_for_step</a>(...) -> typing.List[ListMessagesForStepResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List messages for a given step.
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

client.steps.list_messages_for_step(
    step_id="step-123e4567-e89b-42d3-8456-426614174000",
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

**step_id:** `str` — The ID of the step in the format 'step-<uuid4>'
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Message ID cursor for pagination. Returns messages that come before this message ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Message ID cursor for pagination. Returns messages that come after this message ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of messages to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListMessagesForStepRequestOrder]` — Sort order for messages by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[ListMessagesForStepRequestOrderBy]` — Sort by field
    
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

## Tag
<details><summary><code>client.tag.<a href="src/fern/tag/client.py">list_tags</a>(...) -> typing.List[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the list of all tags (from agents and blocks) that have been created.
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

client.tag.list_tags()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**before:** `typing.Optional[str]` — Tag cursor for pagination. Returns tags that come before this tag in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Tag cursor for pagination. Returns tags that come after this tag in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of tags to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListTagsRequestOrder]` — Sort order for tags. 'asc' for alphabetical order, 'desc' for reverse alphabetical order
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[ListTagsRequestOrderBy]` — Field to sort by
    
</dd>
</dl>

<dl>
<dd>

**query_text:** `typing.Optional[str]` — Filter tags by text search. Deprecated, please use name field instead
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Filter tags by name
    
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

## Telemetry
<details><summary><code>client.telemetry.<a href="src/fern/telemetry/client.py">retrieve_provider_trace</a>(...) -> typing.Optional[ProviderTrace]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**DEPRECATED**: Use `GET /steps/{step_id}/trace` instead.

Retrieve provider trace by step ID.
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

client.telemetry.retrieve_provider_trace(
    step_id="step_id",
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

**step_id:** `str` 
    
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

## Messages
<details><summary><code>client.messages.<a href="src/fern/messages/client.py">list_all_messages</a>(...) -> typing.List[LettaMessageUnion]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List messages across all agents for the current user.
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

client.messages.list_all_messages()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**before:** `typing.Optional[str]` — Message ID cursor for pagination. Returns messages that come before this message ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Message ID cursor for pagination. Returns messages that come after this message ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of messages to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListAllMessagesRequestOrder]` — Sort order for messages by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**conversation_id:** `typing.Optional[str]` — Conversation ID to filter messages by
    
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

<details><summary><code>client.messages.<a href="src/fern/messages/client.py">search_all_messages</a>(...) -> typing.List[SearchAllMessagesResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search messages across the organization with optional agent filtering.
Returns messages with FTS/vector ranks and total RRF score.

This is a cloud-only feature.
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

client.messages.search_all_messages(
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

**query:** `str` — Text query for full-text search
    
</dd>
</dl>

<dl>
<dd>

**search_mode:** `typing.Optional[SearchAllMessagesRequestSearchMode]` — Search mode to use
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `typing.Optional[str]` — Filter messages by agent ID
    
</dd>
</dl>

<dl>
<dd>

**conversation_id:** `typing.Optional[str]` — Filter messages by conversation ID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of results to return
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.datetime]` — Filter messages created after this date
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.datetime]` — Filter messages created on or before this date
    
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

<details><summary><code>client.messages.<a href="src/fern/messages/client.py">list_batches</a>(...) -> typing.List[BatchJob]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all batch runs.
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

client.messages.list_batches()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**before:** `typing.Optional[str]` — Job ID cursor for pagination. Returns jobs that come before this job ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Job ID cursor for pagination. Returns jobs that come after this job ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of jobs to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListBatchesRequestOrder]` — Sort order for jobs by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[ListBatchesRequestOrderBy]` — Field to sort by
    
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

<details><summary><code>client.messages.<a href="src/fern/messages/client.py">create_batch</a>(...) -> BatchJob</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submit a batch of agent runs for asynchronous processing.

Creates a job that will fan out messages to all listed agents and process them in parallel.
The request will be rejected if it exceeds 256MB.
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
from fern import FernApi, LettaBatchRequest
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.messages.create_batch(
    requests=[
        LettaBatchRequest(
            agent_id="agent_id",
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

**requests:** `typing.List[LettaBatchRequest]` — List of requests to be processed in batch.
    
</dd>
</dl>

<dl>
<dd>

**callback_url:** `typing.Optional[str]` — Optional URL to call via POST when the batch completes. The callback payload will be a JSON object with the following fields: {'job_id': string, 'status': string, 'completed_at': string}. Where 'job_id' is the unique batch job identifier, 'status' is the final batch status (e.g., 'completed', 'failed'), and 'completed_at' is an ISO 8601 timestamp indicating when the batch job completed.
    
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

<details><summary><code>client.messages.<a href="src/fern/messages/client.py">retrieve_batch</a>(...) -> BatchJob</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the status and details of a batch run.
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

client.messages.retrieve_batch(
    batch_id="batch_id",
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

**batch_id:** `str` 
    
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

<details><summary><code>client.messages.<a href="src/fern/messages/client.py">list_messages_for_batch</a>(...) -> LettaBatchMessages</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get response messages for a specific batch job.
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

client.messages.list_messages_for_batch(
    batch_id="batch_id",
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

**batch_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Message ID cursor for pagination. Returns messages that come before this message ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Message ID cursor for pagination. Returns messages that come after this message ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of messages to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListMessagesForBatchRequestOrder]` — Sort order for messages by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[ListMessagesForBatchRequestOrderBy]` — Field to sort by
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `typing.Optional[str]` — Filter messages by agent ID
    
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

<details><summary><code>client.messages.<a href="src/fern/messages/client.py">cancel_batch</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel a batch run.
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

client.messages.cancel_batch(
    batch_id="batch_id",
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

**batch_id:** `str` 
    
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

<details><summary><code>client.messages.<a href="src/fern/messages/client.py">retrieve_message</a>(...) -> typing.List[LettaMessageUnion]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a message by ID.
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

client.messages.retrieve_message(
    message_id="message-123e4567-e89b-42d3-8456-426614174000",
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

**message_id:** `str` — The ID of the message in the format 'message-<uuid4>'
    
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

## Passages
<details><summary><code>client.passages.<a href="src/fern/passages/client.py">search_passages</a>(...) -> typing.List[PassageSearchResult]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search passages across the organization with optional agent and archive filtering.
Returns passages with relevance scores.

This endpoint supports semantic search through passages:
- If neither agent_id nor archive_id is provided, searches ALL passages in the organization
- If agent_id is provided, searches passages across all archives attached to that agent
- If archive_id is provided, searches passages within that specific archive
- If both are provided, agent_id takes precedence
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

client.passages.search_passages(
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

**query:** `str` — Text query for semantic search
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `typing.Optional[str]` — Filter passages by agent ID
    
</dd>
</dl>

<dl>
<dd>

**archive_id:** `typing.Optional[str]` — Filter passages by archive ID
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` — Optional list of tags to filter search results
    
</dd>
</dl>

<dl>
<dd>

**tag_match_mode:** `typing.Optional[PassageSearchRequestTagMatchMode]` — How to match tags - 'any' to match passages with any of the tags, 'all' to match only passages with all tags
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of results to return
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.datetime]` — Filter results to passages created after this datetime
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.datetime]` — Filter results to passages created before this datetime
    
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

## Voice
<details><summary><code>client.voice.<a href="src/fern/voice/client.py">create_voice_chat_completions</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

DEPRECATED: This voice-beta endpoint has been deprecated.

The voice functionality has been integrated into the main chat completions endpoint.
Please use the standard /v1/agents/{agent_id}/messages endpoint instead.

This endpoint will be removed in a future version.
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

client.voice.create_voice_chat_completions(
    agent_id="agent_id",
    request={
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

**agent_id:** `str` 
    
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

## Embeddings
<details><summary><code>client.embeddings.<a href="src/fern/embeddings/client.py">get_total_storage_size</a>(...) -> float</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the total size of all embeddings in the database for a user in the storage unit given.
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

client.embeddings.get_total_storage_size()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**storage_unit:** `typing.Literal` 
    
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

## Templates
<details><summary><code>client.templates.<a href="src/fern/templates/client.py">createagentsfromtemplate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an Agent or multiple Agents from a template
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

client.templates.createagentsfromtemplate(
    project_id="project_id",
    template_version="template_version",
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

**project_id:** `str` — The project id
    
</dd>
</dl>

<dl>
<dd>

**template_version:** `str` — The template version, formatted as {template-name}:{version-number} or {template-name}:latest. This endpoint is not available for self-hosted Letta.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` — The tags to assign to the agent
    
</dd>
</dl>

<dl>
<dd>

**agent_name:** `typing.Optional[str]` — The name of the agent, optional otherwise a random one will be assigned
    
</dd>
</dl>

<dl>
<dd>

**initial_message_sequence:** `typing.Optional[typing.List[TemplatesCreateAgentsFromTemplateRequestInitialMessageSequenceItem]]` — Set an initial sequence of messages, if not provided, the agent will start with the default message sequence, if an empty array is provided, the agent will start with no messages
    
</dd>
</dl>

<dl>
<dd>

**memory_variables:** `typing.Optional[typing.Dict[str, str]]` — The memory variables to assign to the agent
    
</dd>
</dl>

<dl>
<dd>

**tool_variables:** `typing.Optional[typing.Dict[str, str]]` — The tool variables to assign to the agent
    
</dd>
</dl>

<dl>
<dd>

**identity_ids:** `typing.Optional[typing.List[str]]` — The identity ids to assign to the agent
    
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

<details><summary><code>client.templates.<a href="src/fern/templates/client.py">createagentsfromtemplatenoproject</a>(...) -> TemplatesCreateAgentsFromTemplateNoProjectResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an Agent or multiple Agents from a template
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

client.templates.createagentsfromtemplatenoproject(
    template_version="template_version",
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

**template_version:** `str` — The template version, formatted as {template-name}:{version-number} or {template-name}:latest. This endpoint is not available for self-hosted Letta.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` — The tags to assign to the agent
    
</dd>
</dl>

<dl>
<dd>

**agent_name:** `typing.Optional[str]` — The name of the agent, optional otherwise a random one will be assigned
    
</dd>
</dl>

<dl>
<dd>

**initial_message_sequence:** `typing.Optional[typing.List[TemplatesCreateAgentsFromTemplateNoProjectRequestInitialMessageSequenceItem]]` — Set an initial sequence of messages, if not provided, the agent will start with the default message sequence, if an empty array is provided, the agent will start with no messages
    
</dd>
</dl>

<dl>
<dd>

**memory_variables:** `typing.Optional[typing.Dict[str, str]]` — The memory variables to assign to the agent
    
</dd>
</dl>

<dl>
<dd>

**tool_variables:** `typing.Optional[typing.Dict[str, str]]` — The tool variables to assign to the agent
    
</dd>
</dl>

<dl>
<dd>

**identity_ids:** `typing.Optional[typing.List[str]]` — The identity ids to assign to the agent
    
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

<details><summary><code>client.templates.<a href="src/fern/templates/client.py">listtemplates</a>(...) -> TemplatesListTemplatesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all templates
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

client.templates.listtemplates()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**offset:** `typing.Optional[TemplatesListTemplatesRequestOffset]` 
    
</dd>
</dl>

<dl>
<dd>

**exact:** `typing.Optional[str]` — Whether to search for an exact name match
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[str]` — Specify the version you want to return, otherwise will return the latest version
    
</dd>
</dl>

<dl>
<dd>

**template_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**project_slug:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[TemplatesListTemplatesRequestSortBy]` 
    
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

<details><summary><code>client.templates.<a href="src/fern/templates/client.py">createtemplatenoproject</a>(...) -> TemplatesCreateTemplateNoProjectResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new template from an existing agent or agent file
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
from fern.templates import TemplatesCreateTemplateNoProjectRequest_Agent

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.templates.createtemplatenoproject(
    request=TemplatesCreateTemplateNoProjectRequest_Agent(
        agent_id="agent_id",
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

**request:** `TemplatesCreateTemplateNoProjectRequest` — The type of template to create, currently only agent templates are supported
    
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

<details><summary><code>client.templates.<a href="src/fern/templates/client.py">savetemplateversion</a>(...) -> TemplatesSaveTemplateVersionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Saves the current version of the template as a new version
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

client.templates.savetemplateversion(
    project_id="project_id",
    template_name="template_name",
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

**project_id:** `str` — The project id
    
</dd>
</dl>

<dl>
<dd>

**template_name:** `str` — The template version, formatted as {template-name}, any version appended will be ignored
    
</dd>
</dl>

<dl>
<dd>

**preserve_environment_variables_on_migration:** `typing.Optional[bool]` — If true, the environment variables will be preserved in the template version when migrating agents
    
</dd>
</dl>

<dl>
<dd>

**preserve_core_memories_on_migration:** `typing.Optional[bool]` — If true, the core memories will be preserved in the template version when migrating agents
    
</dd>
</dl>

<dl>
<dd>

**preserve_sources_on_migration:** `typing.Optional[bool]` — If true, existing agent folders/sources will be preserved and merged with template sources during migration. If false, agent sources will be replaced with template sources.
    
</dd>
</dl>

<dl>
<dd>

**block_reconciliation_strategy:** `typing.Optional[TemplatesSaveTemplateVersionRequestBlockReconciliationStrategy]` — Strategy for reconciling memory blocks during migration: "reconcile-all" deletes blocks not in the template, "preserve-deleted" keeps them. Defaults to "preserve-deleted".
    
</dd>
</dl>

<dl>
<dd>

**migrate_agents:** `typing.Optional[bool]` — If true, existing agents attached to this template will be migrated to the new template version
    
</dd>
</dl>

<dl>
<dd>

**message:** `typing.Optional[str]` — A message to describe the changes made in this template version
    
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

<details><summary><code>client.templates.<a href="src/fern/templates/client.py">deletetemplate</a>(...) -> TemplatesDeleteTemplateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes all versions of a template with the specified name
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

client.templates.deletetemplate(
    project_id="project_id",
    template_name="template_name",
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

**project_id:** `str` — The project id
    
</dd>
</dl>

<dl>
<dd>

**template_name:** `str` — The template name (without version)
    
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

<details><summary><code>client.templates.<a href="src/fern/templates/client.py">gettemplatesnapshot</a>(...) -> TemplatesGetTemplateSnapshotResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a snapshot of the template version, this will return the template state at a specific version
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

client.templates.gettemplatesnapshot(
    project_id="project_id",
    template_version="template_version",
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

**project_id:** `str` — The project id
    
</dd>
</dl>

<dl>
<dd>

**template_version:** `str` — The template version, formatted as {template-name}:{version-number} or {template-name}:latest
    
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

<details><summary><code>client.templates.<a href="src/fern/templates/client.py">setcurrenttemplatefromsnapshot</a>(...) -> TemplatesSetCurrentTemplateFromSnapshotResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the current working version of a template from a snapshot
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

client.templates.setcurrenttemplatefromsnapshot(
    project_id="project_id",
    template_version="template_version",
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

**project_id:** `str` — The project id
    
</dd>
</dl>

<dl>
<dd>

**template_version:** `str` — The template name with :dev version (e.g., my-template:dev)
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Optional[typing.Any]` — The template snapshot to set as the current version
    
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

<details><summary><code>client.templates.<a href="src/fern/templates/client.py">forktemplate</a>(...) -> TemplatesForkTemplateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Forks a template version into a new template
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

client.templates.forktemplate(
    project_id="project_id",
    template_version="template_version",
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

**project_id:** `str` — The project id
    
</dd>
</dl>

<dl>
<dd>

**template_version:** `str` — The template version, formatted as {template-name}:{version-number} or {template-name}:latest
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Optional custom name for the forked template. If not provided, a random name will be generated.
    
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

<details><summary><code>client.templates.<a href="src/fern/templates/client.py">createtemplate</a>(...) -> TemplatesCreateTemplateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new template from an existing agent or agent file
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
from fern.templates import TemplatesCreateTemplateRequestBody_Agent

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.templates.createtemplate(
    project_id="project_id",
    request=TemplatesCreateTemplateRequestBody_Agent(
        agent_id="agent_id",
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

**project_id:** `str` — The project id
    
</dd>
</dl>

<dl>
<dd>

**request:** `TemplatesCreateTemplateRequestBody` — The type of template to create, currently only agent templates are supported
    
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

<details><summary><code>client.templates.<a href="src/fern/templates/client.py">deletetemplatenoproject</a>(...) -> TemplatesDeleteTemplateNoProjectResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes all versions of a template with the specified name
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

client.templates.deletetemplatenoproject(
    template_name="template_name",
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

**template_name:** `str` — The template name (without version)
    
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

<details><summary><code>client.templates.<a href="src/fern/templates/client.py">updatecurrenttemplatefromagentfilenoproject</a>(...) -> TemplatesUpdateCurrentTemplateFromAgentFileNoProjectResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the current working version of a template from an agent file
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

client.templates.updatecurrenttemplatefromagentfilenoproject(
    template_name="template_name",
    agent_file_json={
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

**template_name:** `str` — The template name (without version)
    
</dd>
</dl>

<dl>
<dd>

**agent_file_json:** `typing.Dict[str, typing.Any]` — The agent file to update the current template version from
    
</dd>
</dl>

<dl>
<dd>

**update_existing_tools:** `typing.Optional[bool]` — If true, update existing custom tools source_code and json_schema (source_type cannot be changed)
    
</dd>
</dl>

<dl>
<dd>

**save_existing_changes:** `typing.Optional[bool]` — If true, Letta will automatically save any changes as a version before updating the template
    
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

<details><summary><code>client.templates.<a href="src/fern/templates/client.py">renametemplate</a>(...) -> TemplatesRenameTemplateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Renames all versions of a template with the specified name. Versions are automatically stripped from the current template name if accidentally included.
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

client.templates.renametemplate(
    project_id="project_id",
    template_name="template_name",
    new_name="new_name",
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

**project_id:** `str` — The project id
    
</dd>
</dl>

<dl>
<dd>

**template_name:** `str` — The current template name (version will be automatically stripped if included)
    
</dd>
</dl>

<dl>
<dd>

**new_name:** `str` — The new name for the template
    
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

<details><summary><code>client.templates.<a href="src/fern/templates/client.py">updatetemplatedescription</a>(...) -> TemplatesUpdateTemplateDescriptionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the description for all versions of a template with the specified name. Versions are automatically stripped from the current template name if accidentally included.
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

client.templates.updatetemplatedescription(
    project_id="project_id",
    template_name="template_name",
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

**project_id:** `str` — The project id
    
</dd>
</dl>

<dl>
<dd>

**template_name:** `str` — The template name (version will be automatically stripped if included)
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The new description for the template
    
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

<details><summary><code>client.templates.<a href="src/fern/templates/client.py">listtemplateversions</a>(...) -> TemplatesListTemplateVersionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all versions of a specific template
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

client.templates.listtemplateversions(
    project_id="project_id",
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

**project_id:** `str` — The project id
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The template name (without version)
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[TemplatesListTemplateVersionsRequestOffset]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[str]` 
    
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

<details><summary><code>client.templates.<a href="src/fern/templates/client.py">migratedeployment</a>(...) -> TemplatesMigrateDeploymentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Migrates a deployment to a specific template version
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

client.templates.migratedeployment(
    project_id="project_id",
    template_name="template_name",
    deployment_id="deployment_id",
    version="version",
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

**project_id:** `str` — The project id
    
</dd>
</dl>

<dl>
<dd>

**template_name:** `str` — The template name (without version)
    
</dd>
</dl>

<dl>
<dd>

**deployment_id:** `str` — The deployment ID to migrate
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` — The target template version to migrate to
    
</dd>
</dl>

<dl>
<dd>

**preserve_tool_variables:** `typing.Optional[bool]` — Whether to preserve existing tool variables during migration
    
</dd>
</dl>

<dl>
<dd>

**preserve_core_memories:** `typing.Optional[bool]` — Whether to preserve existing core memories during migration
    
</dd>
</dl>

<dl>
<dd>

**preserve_sources:** `typing.Optional[bool]` — If true, existing agent sources will be preserved and merged with template sources during migration. If false, agent sources will be replaced with template sources.
    
</dd>
</dl>

<dl>
<dd>

**memory_variables:** `typing.Optional[typing.Dict[str, str]]` — Additional memory variables to apply during migration
    
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

<details><summary><code>client.templates.<a href="src/fern/templates/client.py">updatecurrenttemplatefromagentfile</a>(...) -> TemplatesUpdateCurrentTemplateFromAgentFileResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the current working version of a template from an agent file
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

client.templates.updatecurrenttemplatefromagentfile(
    project_id="project_id",
    template_name="template_name",
    agent_file_json={
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

**project_id:** `str` — The project id
    
</dd>
</dl>

<dl>
<dd>

**template_name:** `str` — The template name (without version)
    
</dd>
</dl>

<dl>
<dd>

**agent_file_json:** `typing.Dict[str, typing.Any]` — The agent file to update the current template version from
    
</dd>
</dl>

<dl>
<dd>

**update_existing_tools:** `typing.Optional[bool]` — If true, update existing custom tools source_code and json_schema (source_type cannot be changed)
    
</dd>
</dl>

<dl>
<dd>

**save_existing_changes:** `typing.Optional[bool]` — If true, Letta will automatically save any changes as a version before updating the template
    
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

<details><summary><code>client.templates.<a href="src/fern/templates/client.py">legacymigration</a>(...) -> TemplatesLegacyMigrationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Migrates a template from a legacy project to the default project. Only works if the template is currently in a legacy project.
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

client.templates.legacymigration(
    template_id="templateId",
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

**template_id:** `str` — The template ID
    
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

## ClientSideAccessTokens
<details><summary><code>client.client_side_access_tokens.<a href="src/fern/client_side_access_tokens/client.py">client_side_access_tokens_list_client_side_access_tokens</a>(...) -> ClientSideAccessTokensListClientSideAccessTokensResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all client side access tokens for the current account. This is only available for cloud users.
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

client.client_side_access_tokens.client_side_access_tokens_list_client_side_access_tokens()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `typing.Optional[str]` — The agent ID to filter tokens by. If provided, only tokens for this agent will be returned.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[float]` — The offset for pagination. Defaults to 0.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — The number of tokens to return per page. Defaults to 10.
    
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

<details><summary><code>client.client_side_access_tokens.<a href="src/fern/client_side_access_tokens/client.py">client_side_access_tokens_create_client_side_access_token</a>(...) -> ClientSideAccessTokensCreateClientSideAccessTokenResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new client side access token with the specified configuration.
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
from fern.client_side_access_tokens import ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItem, ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItemType, ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItemAccessItem

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.client_side_access_tokens.client_side_access_tokens_create_client_side_access_token(
    policy=[
        ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItem(
            type=ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItemType.AGENT,
            id="id",
            access=[
                ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItemAccessItem.READ_MESSAGES
            ],
        )
    ],
    hostname="hostname",
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

**policy:** `typing.List[ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItem]` 
    
</dd>
</dl>

<dl>
<dd>

**hostname:** `str` — The hostname of the client side application. Please specify the full URL including the protocol (http or https).
    
</dd>
</dl>

<dl>
<dd>

**expires_at:** `typing.Optional[str]` — The expiration date of the token. If not provided, the token will expire in 5 minutes
    
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

<details><summary><code>client.client_side_access_tokens.<a href="src/fern/client_side_access_tokens/client.py">client_side_access_tokens_delete_client_side_access_token</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a client side access token.
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

client.client_side_access_tokens.client_side_access_tokens_delete_client_side_access_token(
    token="token",
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

**token:** `str` — The access token to delete
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Any` 
    
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

## Projects
<details><summary><code>client.projects.<a href="src/fern/projects/client.py">listprojects</a>(...) -> ProjectsListProjectsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all projects
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

client.projects.listprojects()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[ProjectsListProjectsRequestOffset]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[str]` 
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">createproject</a>(...) -> ProjectsCreateProjectResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new project
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

client.projects.createproject(
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

**name:** `str` 
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">deleteproject</a>(...) -> ProjectsDeleteProjectResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a project by ID
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

client.projects.deleteproject(
    project_id="projectId",
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

**project_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Optional[typing.Any]` 
    
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

## Metadata
<details><summary><code>client.metadata.<a href="src/fern/metadata/client.py">retrievecurrentbalances</a>() -> MetadataRetrieveCurrentBalancesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the current usage balances for the organization.
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

client.metadata.retrievecurrentbalances()

```
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

<details><summary><code>client.metadata.<a href="src/fern/metadata/client.py">sendfeedback</a>(...) -> MetadataSendFeedbackResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send feedback from users to improve our services.
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

client.metadata.sendfeedback(
    message="message",
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

**message:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**feature:** `typing.Optional[MetadataSendFeedbackRequestFeature]` 
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**session_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**platform:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[str]` 
    
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

<details><summary><code>client.metadata.<a href="src/fern/metadata/client.py">sendtelemetry</a>(...) -> MetadataSendTelemetryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send telemetry events for usage tracking and analysis.
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
from fern.metadata import MetadataSendTelemetryRequestService, MetadataSendTelemetryRequestEventsItem_SessionStart, MetadataSendTelemetryRequestEventsItemSessionStartData

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.metadata.sendtelemetry(
    service=MetadataSendTelemetryRequestService.LETTA_CODE,
    events=[
        MetadataSendTelemetryRequestEventsItem_SessionStart(
            timestamp="timestamp",
            data=MetadataSendTelemetryRequestEventsItemSessionStartData(
                session_id="session_id",
                startup_command="startup_command",
            ),
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

**service:** `MetadataSendTelemetryRequestService` 
    
</dd>
</dl>

<dl>
<dd>

**events:** `typing.List[MetadataSendTelemetryRequestEventsItem]` 
    
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

<details><summary><code>client.metadata.<a href="src/fern/metadata/client.py">getstatus</a>() -> MetadataGetStatusResponse</code></summary>
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

client.metadata.getstatus()

```
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

<details><summary><code>client.metadata.<a href="src/fern/metadata/client.py">getuser</a>() -> MetadataGetUserResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve information about the current authenticated user including email, name, organization, and current project.
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

client.metadata.getuser()

```
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

## ScheduledMessages
<details><summary><code>client.scheduled_messages.<a href="src/fern/scheduled_messages/client.py">scheduled_messages_list_scheduled_messages</a>(...) -> ScheduledMessagesListScheduledMessagesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all scheduled messages for a specific agent.
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

client.scheduled_messages.scheduled_messages_list_scheduled_messages(
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

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` 
    
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

<details><summary><code>client.scheduled_messages.<a href="src/fern/scheduled_messages/client.py">scheduled_messages_schedule_agent_message</a>(...) -> ScheduledMessagesScheduleAgentMessageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Schedule a message to be sent by the agent at a specified time or on a recurring basis.
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
from fern.scheduled_messages import ScheduledMessagesScheduleAgentMessageRequestMessagesItem, ScheduledMessagesScheduleAgentMessageRequestMessagesItemContentZeroItem_Text, ScheduledMessagesScheduleAgentMessageRequestMessagesItemRole, ScheduledMessagesScheduleAgentMessageRequestSchedule_OneTime

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.scheduled_messages.scheduled_messages_schedule_agent_message(
    agent_id="agent_id",
    messages=[
        ScheduledMessagesScheduleAgentMessageRequestMessagesItem(
            content=[
                ScheduledMessagesScheduleAgentMessageRequestMessagesItemContentZeroItem_Text(
                    text="text",
                )
            ],
            role=ScheduledMessagesScheduleAgentMessageRequestMessagesItemRole.USER,
        )
    ],
    schedule=ScheduledMessagesScheduleAgentMessageRequestSchedule_OneTime(
        scheduled_at=1.1,
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

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.List[ScheduledMessagesScheduleAgentMessageRequestMessagesItem]` 
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `ScheduledMessagesScheduleAgentMessageRequestSchedule` 
    
</dd>
</dl>

<dl>
<dd>

**max_steps:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**callback_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**include_return_message_types:** `typing.Optional[typing.List[ScheduledMessagesScheduleAgentMessageRequestIncludeReturnMessageTypesItem]]` 
    
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

<details><summary><code>client.scheduled_messages.<a href="src/fern/scheduled_messages/client.py">scheduled_messages_retrieve_scheduled_message</a>(...) -> ScheduledMessagesRetrieveScheduledMessageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a scheduled message by its ID for a specific agent.
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

client.scheduled_messages.scheduled_messages_retrieve_scheduled_message(
    agent_id="agent_id",
    scheduled_message_id="scheduled_message_id",
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

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**scheduled_message_id:** `str` 
    
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

<details><summary><code>client.scheduled_messages.<a href="src/fern/scheduled_messages/client.py">scheduled_messages_delete_scheduled_message</a>(...) -> ScheduledMessagesDeleteScheduledMessageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a scheduled message by its ID for a specific agent.
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
from fern.scheduled_messages import ScheduledMessagesDeleteScheduledMessageRequestBody

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.scheduled_messages.scheduled_messages_delete_scheduled_message(
    agent_id="agent_id",
    scheduled_message_id="scheduled_message_id",
    request=ScheduledMessagesDeleteScheduledMessageRequestBody(),
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

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**scheduled_message_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Optional[ScheduledMessagesDeleteScheduledMessageRequestBody]` 
    
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

## Feeds
<details><summary><code>client.feeds.<a href="src/fern/feeds/client.py">listfeeds</a>(...) -> FeedsListFeedsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all feeds with optional filters and pagination
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

client.feeds.listfeeds()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**project_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[FeedsListFeedsRequestOffset]` 
    
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

<details><summary><code>client.feeds.<a href="src/fern/feeds/client.py">createfeed</a>(...) -> FeedsCreateFeedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new feed in a project
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

client.feeds.createfeed(
    project_id="project_id",
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

**project_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
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

<details><summary><code>client.feeds.<a href="src/fern/feeds/client.py">getfeed</a>(...) -> FeedsGetFeedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve feed details by ID
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

client.feeds.getfeed(
    feed_id="feed_id",
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

**feed_id:** `str` 
    
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

<details><summary><code>client.feeds.<a href="src/fern/feeds/client.py">deletefeed</a>(...) -> FeedsDeleteFeedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Soft delete a feed and clean up its sequence
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
from fern.feeds import FeedsDeleteFeedRequestBody

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.feeds.deletefeed(
    feed_id="feed_id",
    request=FeedsDeleteFeedRequestBody(),
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

**feed_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Optional[FeedsDeleteFeedRequestBody]` 
    
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

<details><summary><code>client.feeds.<a href="src/fern/feeds/client.py">listmessages</a>(...) -> FeedsListMessagesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List messages from a feed (for debugging/inspection)
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

client.feeds.listmessages(
    feed_id="feed_id",
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

**feed_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**after_sequence:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[str]` 
    
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

<details><summary><code>client.feeds.<a href="src/fern/feeds/client.py">publishmessages</a>(...) -> FeedsPublishMessagesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Batch insert messages into a feed (up to 10,000 per request)
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
from fern.feeds import FeedsPublishMessagesRequestMessagesItem

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.feeds.publishmessages(
    feed_id="feed_id",
    messages=[
        FeedsPublishMessagesRequestMessagesItem(
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

**feed_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.List[FeedsPublishMessagesRequestMessagesItem]` 
    
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

<details><summary><code>client.feeds.<a href="src/fern/feeds/client.py">getmessage</a>(...) -> FeedsGetMessageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get full content of a feed message
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

client.feeds.getmessage(
    feed_id="feed_id",
    message_id="message_id",
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

**feed_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**message_id:** `str` 
    
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

<details><summary><code>client.feeds.<a href="src/fern/feeds/client.py">subscribeagent</a>(...) -> FeedsSubscribeAgentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Subscribe an agent to a feed with polling configuration
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

client.feeds.subscribeagent(
    feed_id="feed_id",
    agent_id="agent_id",
    cron_schedule="cron_schedule",
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

**feed_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**cron_schedule:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**prompt_template:** `typing.Optional[str]` 
    
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

<details><summary><code>client.feeds.<a href="src/fern/feeds/client.py">deletesubscription</a>(...) -> FeedsDeleteSubscriptionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove agent subscription from a feed (by subscription_id)
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
from fern.feeds import FeedsDeleteSubscriptionRequestBody

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.feeds.deletesubscription(
    feed_id="feed_id",
    subscription_id="subscription_id",
    request=FeedsDeleteSubscriptionRequestBody(),
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

**feed_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Optional[FeedsDeleteSubscriptionRequestBody]` 
    
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

<details><summary><code>client.feeds.<a href="src/fern/feeds/client.py">updatesubscription</a>(...) -> FeedsUpdateSubscriptionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update subscription configuration (cron schedule, enable/disable)
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

client.feeds.updatesubscription(
    feed_id="feed_id",
    subscription_id="subscription_id",
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

**feed_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**cron_schedule:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**prompt_template:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**disabled:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.feeds.<a href="src/fern/feeds/client.py">unsubscribeagent</a>(...) -> FeedsUnsubscribeAgentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove agent subscription from a feed (by agent_id)
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

client.feeds.unsubscribeagent(
    feed_id="feed_id",
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

**feed_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `str` 
    
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

<details><summary><code>client.feeds.<a href="src/fern/feeds/client.py">triggersubscription</a>(...) -> FeedsTriggerSubscriptionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Immediately trigger a subscription to process pending messages
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

client.feeds.triggersubscription(
    feed_id="feed_id",
    subscription_id="subscription_id",
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

**feed_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**subscription_id:** `str` 
    
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

<details><summary><code>client.feeds.<a href="src/fern/feeds/client.py">backfillsubscription</a>(...) -> FeedsBackfillSubscriptionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start a background job to send historical messages to an agent subscription. Returns immediately with workflow ID. Does not update last_consumed_sequence.
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

client.feeds.backfillsubscription(
    feed_id="feed_id",
    subscription_id="subscription_id",
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

**feed_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**from_sequence:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**to_sequence:** `typing.Optional[float]` 
    
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

<details><summary><code>client.feeds.<a href="src/fern/feeds/client.py">listsubscriptionhistory</a>(...) -> FeedsListSubscriptionHistoryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the run history for a subscription including scheduled runs, manual triggers, and backfills.
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

client.feeds.listsubscriptionhistory(
    feed_id="feed_id",
    subscription_id="subscription_id",
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

**feed_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**next_page_token:** `typing.Optional[str]` 
    
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

<details><summary><code>client.feeds.<a href="src/fern/feeds/client.py">updateallsubscriptionscron</a>(...) -> FeedsUpdateAllSubscriptionsCronResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the cron schedule for all subscriptions of a feed
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

client.feeds.updateallsubscriptionscron(
    feed_id="feed_id",
    cron_schedule="cron_schedule",
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

**feed_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**cron_schedule:** `str` 
    
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

<details><summary><code>client.feeds.<a href="src/fern/feeds/client.py">listsubscriptions</a>(...) -> FeedsListSubscriptionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all agent subscriptions for a feed
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

client.feeds.listsubscriptions(
    feed_id="feed_id",
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

**feed_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[FeedsListSubscriptionsRequestOffset]` 
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `typing.Optional[str]` 
    
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

## Pipelines
<details><summary><code>client.pipelines.<a href="src/fern/pipelines/client.py">listpipelines</a>(...) -> PipelinesListPipelinesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all pipelines for the organization with optional filtering
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

client.pipelines.listpipelines()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**integration_type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[PipelinesListPipelinesRequestOffset]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[str]` 
    
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

<details><summary><code>client.pipelines.<a href="src/fern/pipelines/client.py">createpipeline</a>(...) -> PipelinesCreatePipelineResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new pipeline (producer + feed + optionally subscribers)
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
from fern.pipelines import PipelinesCreatePipelineRequestIntegrationType, PipelinesCreatePipelineRequestProducerConfig, PipelinesCreatePipelineRequestProducerConfigType, PipelinesCreatePipelineRequestProducerConfigData, PipelinesCreatePipelineRequestProducerConfigDataChannelsItem

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.pipelines.createpipeline(
    name="name",
    project_id="project_id",
    integration_type=PipelinesCreatePipelineRequestIntegrationType.SLACK,
    producer_config=PipelinesCreatePipelineRequestProducerConfig(
        type=PipelinesCreatePipelineRequestProducerConfigType.SLACK_CHANNEL_READER,
        data=PipelinesCreatePipelineRequestProducerConfigData(
            channels=[
                PipelinesCreatePipelineRequestProducerConfigDataChannelsItem(
                    channel_id="channel_id",
                )
            ],
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

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**integration_type:** `PipelinesCreatePipelineRequestIntegrationType` 
    
</dd>
</dl>

<dl>
<dd>

**producer_config:** `PipelinesCreatePipelineRequestProducerConfig` 
    
</dd>
</dl>

<dl>
<dd>

**subscriber_agent_ids:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**subscriber_cron_schedule:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**prompt_template:** `typing.Optional[str]` 
    
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

<details><summary><code>client.pipelines.<a href="src/fern/pipelines/client.py">countpipelines</a>(...) -> PipelinesCountPipelinesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the total count of pipelines, optionally filtered by project and search
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

client.pipelines.countpipelines()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**integration_type:** `typing.Optional[str]` 
    
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

<details><summary><code>client.pipelines.<a href="src/fern/pipelines/client.py">getpipeline</a>(...) -> PipelinesGetPipelineResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a single pipeline with details
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

client.pipelines.getpipeline(
    pipeline_id="pipeline_id",
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

**pipeline_id:** `str` 
    
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

<details><summary><code>client.pipelines.<a href="src/fern/pipelines/client.py">deletepipeline</a>(...) -> PipelinesDeletePipelineResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Soft delete a pipeline and cascade to feed + subscriptions
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

client.pipelines.deletepipeline(
    pipeline_id="pipeline_id",
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

**pipeline_id:** `str` 
    
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

<details><summary><code>client.pipelines.<a href="src/fern/pipelines/client.py">updatepipeline</a>(...) -> PipelinesUpdatePipelineResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update pipeline name or disable/enable it
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

client.pipelines.updatepipeline(
    pipeline_id="pipeline_id",
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

**pipeline_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**disabled:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.pipelines.<a href="src/fern/pipelines/client.py">previewpipeline</a>(...) -> PipelinesPreviewPipelineResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch sample messages from integration to preview what agents will receive
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
from fern.pipelines import PipelinesPreviewPipelineRequestIntegrationType, PipelinesPreviewPipelineRequestProducerConfig, PipelinesPreviewPipelineRequestProducerConfigType, PipelinesPreviewPipelineRequestProducerConfigData, PipelinesPreviewPipelineRequestProducerConfigDataChannelsItem

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.pipelines.previewpipeline(
    integration_type=PipelinesPreviewPipelineRequestIntegrationType.SLACK,
    integration_id="integration_id",
    producer_config=PipelinesPreviewPipelineRequestProducerConfig(
        type=PipelinesPreviewPipelineRequestProducerConfigType.SLACK_CHANNEL_READER,
        data=PipelinesPreviewPipelineRequestProducerConfigData(
            channels=[
                PipelinesPreviewPipelineRequestProducerConfigDataChannelsItem(
                    channel_id="channel_id",
                )
            ],
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

**integration_type:** `PipelinesPreviewPipelineRequestIntegrationType` 
    
</dd>
</dl>

<dl>
<dd>

**integration_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**producer_config:** `PipelinesPreviewPipelineRequestProducerConfig` 
    
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

<details><summary><code>client.pipelines.<a href="src/fern/pipelines/client.py">syncpipeline</a>(...) -> PipelinesSyncPipelineResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manually trigger a pipeline sync to fetch new messages immediately
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

client.pipelines.syncpipeline(
    pipeline_id="pipeline_id",
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

**pipeline_id:** `str` 
    
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

<details><summary><code>client.pipelines.<a href="src/fern/pipelines/client.py">listpipelinesynchistory</a>(...) -> PipelinesListPipelineSyncHistoryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the sync run history for a pipeline from Temporal with error details
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

client.pipelines.listpipelinesynchistory(
    pipeline_id="pipeline_id",
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

**pipeline_id:** `str` 
    
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

